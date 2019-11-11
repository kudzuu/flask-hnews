"""
Defines the blueprint for the users
"""
from flask import Blueprint, Flask, jsonify
from flask_restful import Api

from resources import StoryResource


STORY_BLUEPRINT = Blueprint("story", __name__)
Api(STORY_BLUEPRINT).add_resource(
    StoryResource, "/posts"
)
