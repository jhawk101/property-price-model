from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import dash
from flask.helpers import get_root_path


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap(app)

    register_dashapp(app)

    with app.app_context():
        from property_price_model import routes, models

    return app


def register_dashapp(app):
    from property_price_model.plotlydash.layout import layout
    from property_price_model.plotlydash.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }

    my_dashapp = dash.Dash(
        __name__,
        server=app,
        url_base_pathname="/dashapp1/",
        assets_folder=get_root_path(__name__) + "/dashapp1/assets/",
        meta_tags=[meta_viewport],
    )

    my_dashapp.title = "Dashapp 1"
    my_dashapp.layout = layout
    register_callbacks(my_dashapp)
