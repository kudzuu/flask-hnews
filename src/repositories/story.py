""" Defines the User repository """

from flask import abort
from models import Story
from parsers import HackerNewsParser


class StoryRepository:
    """ The repository for the Story model """

    @staticmethod
    def get(order, offset, limit):
        """ Query a story by last and first name """
        stories = Story.query.order_by(order).paginate(offset, limit, False).items

        return [story.json for story in stories]

    @staticmethod
    def create():
        """ Populates new stories from HN """
        hn = HackerNewsParser()
        posts = hn.get_hacker_json()
        data = [{ key: item[key] for key in ['title', 'url', 'time'] } for item in posts]

        try:
            for story in data:
                model = Story(title=story['title'], url=story['url'], created_at=story['time'])
                model.save()
        except Exception as e:
            abort(500, str(e))

        return
