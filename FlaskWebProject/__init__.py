"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import os, sys

app = Flask(__name__)
app.config.from_object(Config)
wsgi_app = app.wsgi_app
# TODO: Add any logging levels and handlers with app.logger
# add logging levels
#logger = logging.getLogger('azure.storage')
app.logger.setLevel(logging.INFO)
# adding handler
# Direct logging output to stdout. Without adding a handler,
# no logging output is captured.
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
import FlaskWebProject.views
