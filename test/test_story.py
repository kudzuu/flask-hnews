import json
import unittest

from models import Story
from datetime import datetime
from models.abc import db
from repositories import StoryRepository
from server import server


class TestStory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/user` should return an user """
        response = self.client.get("/api/posts/?order=created_at")

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(Story.query.count(), 30)

    def test_create(self):
        """ The POST on `/user` should create an user """
        response = self.client.post(
            "/api/posts/",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(Story.query.count(), 30)
