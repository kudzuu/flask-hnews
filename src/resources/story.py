"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask import request
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import StoryRepository
from util import parse_params


class StoryResource(Resource):
    """ Verbs relative to the Stories """

    @staticmethod
    @swag_from("../swagger/posts/GET.yml")
    def get():
        order = request.args.get('order')
        offset = request.args.get('offset', 1, type=int)
        limit = request.args.get('limit', 5, type=int)

        """ Return an user key information based on his name """
        posts = StoryRepository.get(order, offset, limit)

        return jsonify({"posts": posts})

    @staticmethod
    @swag_from("../swagger/posts/POST.yml")
    def post():
        """ Create an user based on the sent information """
        posts = StoryRepository.create()
        return jsonify({"posts": posts})
