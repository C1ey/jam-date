# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate
from .config      import Config

app    = Flask(__name__)
app.config.from_object(Config)

# register extensions on the global `app`
db     = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views
