from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap(app)

    with app.app_context():
        from property_price_model import routes, models

        from property_price_model.plotlydash.dashboard import create_dashboard

        app = create_dashboard(app)

        # from property_price_model.assets import compile_assets

        # compile_assets(app)

        return app

