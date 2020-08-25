import dash
import dash_bootstrap_components as dbc
import pandas as pd
from flask import Flask
from flask.helpers import get_root_path
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from config import Config

db = SQLAlchemy()

engine = create_engine("sqlite:///app.db")
conn = engine.raw_connection()
df = pd.read_sql(f"SELECT * FROM SALE", con=conn)


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap(app)

    with app.app_context():
        from property_price_model import routes, models

        register_dashapp(app)

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
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )

    my_dashapp.title = "Dashapp 1"
    my_dashapp.layout = layout
    register_callbacks(my_dashapp)
