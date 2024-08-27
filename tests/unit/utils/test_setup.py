from unittest import TestCase

from flask import Flask

from src import create_app


class TestSetup(TestCase):
    def test_create_app(self):
        self.assertIsInstance(create_app(), Flask)
