#!/usr/bin/python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLALchemy(app)

from app import view, models
