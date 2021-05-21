# tmdbwrapper/__init__.py
from settings import config
import requests
TMDB_API_KEY = config.environ("TMDB_API_KEY")


class APIKeyMissingError(Exception):
    pass


if TMDB_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://developers.themoviedb.org/3/getting-started/introduction "
        "for how to retrieve an authentication token from "
        "The Movie Database"
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = TMDB_API_KEY
from .tv import TV
