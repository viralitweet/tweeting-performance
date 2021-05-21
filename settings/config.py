# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Import twitter api keys from the .env file.
consumer_key = os.environ.get('API_KEY')
consumer_secret = os.environ.get('API_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')


def environ(name):
    return os.environ.get(name, None)
