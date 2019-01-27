CSRF_ENABLED = True
SECRET_KEY = "Really-diffcult-key"

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    
    
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['fengyangcs@gmail.com']

# pagination
POSTS_PER_PAGE=3

WHOOSH_BASE=os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

class Auth:
    CLIENT_ID = '547482321420-lnh5n057jfs4p6ucjavpa5vskf6hoiid.apps.googleusercontent.com'
    CLIENT_SECRET = 'pS0i0kHNBQA9BxXaBLRMm-8E'
    REDIRECT_URI = 'https://127.0.0.1:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']

