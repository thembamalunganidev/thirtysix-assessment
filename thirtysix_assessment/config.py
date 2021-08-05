import os


class Config:
    # Database
    DATABASE_NAME = os.environ.get('DATABASE_NAME', 'postgres')
    DATABASE_HOST = os.environ.get('DATABASE_HOST', 'db')
    DATABASE_PORT = os.environ.get('DATABASE_PORT', 5432)
    DATABASE_USER = os.environ.get('DATABASE_USER', 'postgres')
    DATABASE_PASSWORD = os.environ.get('DATABASE_USER', 'postgres')

    # Redis
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    REDIS_MAX_CONNECTIONS = os.environ.get('REDIS_MAX_CONNECTIONS', 20)

    # API Credentials
    DISCOGS_API_BASE = os.environ.get(
        'DISCOGS_API_BASE', 'https://api.discogs.com')
    DISCOGS_API_KEY = os.environ.get(
        'DISCOGS_API_KEY', 'NJeAKaYFgjNuPJkaYFXM')
    DISCOGS_API_SECRET = os.environ.get(
        'DISCOGS_API_SECRET', 'YHlQFuZNbIrDUGqbSyvmxGBObLHHqyeZ')

    # Filter sync parameters
    DISCOGS_SYNC_FILTER_PARAMS = {
        'artist': '36',
        'style': 'ambient',
        'genre': 'electronic'
    }

    # Test
    TESTING = os.environ.get('TESTING', True)
