"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7rmm4dadc9vm0j720-a.oregon-postgres.render.com",
        database="vishwastodo_4lop",
        user="vishwastodo_4lop_user",
        password="W7T7R6VkusYDYCLfMdHt6UpDbVNdzyG9")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
