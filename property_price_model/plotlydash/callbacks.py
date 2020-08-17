import pandas as pd
from dash.dependencies import Input
from dash.dependencies import Output
import plotly.express as px
import numpy as np
from property_price_model import db


def register_callbacks(dashapp):
    @dashapp.callback(
        Output("my-graph", "figure"), [Input("my-dropdown", "value")]
    )
    def update_graph(selected_dropdown_value):
        df = pd.read_sql(
            f"SELECT * FROM SALE where incode = '{selected_dropdown_value}'",
            db.session.bind,
        )

        return px.histogram(df, x="price")
