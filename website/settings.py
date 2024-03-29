# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import os
import dotenv

# load environment variables
project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(os.path.abspath(project_dir), '.env')
dotenv.load_dotenv(dotenv_path)
# ---------------------------------

ENV = os.getenv("FLASK_ENV", "production")
DEBUG = ENV == "development"

MONGO_DB_SCRAPER = 'web_scraper'
MONGO_DB_SITE = 'website'
MONGO_DB_HOST = os.getenv('MONGO_DB_HOST')
MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD')
MONGO_URI = os.getenv('MONGO_DB_URI')
if not MONGO_URI:
    MONGO_URI = f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}'

SECRET_KEY = os.getenv("SECRET_KEY")
LOG_FILE = 'live.log'
LOG_PATH = os.path.join(project_dir, 'logs', 'website', LOG_FILE)
SEND_FILE_MAX_AGE_DEFAULT = int(os.getenv("SEND_FILE_MAX_AGE_DEFAULT"))
BCRYPT_LOG_ROUNDS = os.getenv("BCRYPT_LOG_ROUNDS", 13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "SimpleCache"  # Can be "MemcachedCache", "RedisCache", etc.
