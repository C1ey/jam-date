# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS    # if you’re using cors

from .config import Config

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.config.from_object(Config)
CORS(app)    # if you need cross‐origin

db      = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt     = JWTManager(app)

# bring in the models so Alembic sees them
from . import models  # noqa: F401

# now register each blueprint
from .auth     import auth_bp;     app.register_blueprint(auth_bp)
from .profiles import profiles_bp; app.register_blueprint(profiles_bp)
from .users    import users_bp;    app.register_blueprint(users_bp)
