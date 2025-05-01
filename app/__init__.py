import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# instantiate but don’t bind to app yet
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(
        __name__,
        static_folder="../static",
        template_folder="../templates"
    )

    # load config
    from .config import Config
    app.config.from_object(Config)

    # enable CORS on /api/*
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # bind extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # import models so migrations see them
    from . import models  # noqa: F401

    # register blueprints
    from .views    import main_bp
    from .auth     import auth_bp
    from .profiles import profiles_bp
    from .users    import users_bp
    from .search   import search_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profiles_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(search_bp)

    return app
