from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configuration
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)
    # db.init_app(app)
    # login_manager.init_app(app)
    # mail.init_app(app)
    # simple.init_app(app)

    # Registering the blueprints
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # configure UploadSet
    # configure_uploads(app, # photos)

    return app
