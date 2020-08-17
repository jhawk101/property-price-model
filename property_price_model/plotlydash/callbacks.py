import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from property_price_model import db

df = pd.read_sql("SELECT * FROM SALE", db.session.bind,)


def register_callbacks(dashapp):
    @dashapp.callback(
        Output("my-graph", "figure"), [Input("my-dropdown", "value")]
    )
    def update_graph(selected_dropdown_value):
        filtered_df = df[df["incode"] == selected_dropdown_value]
        return px.histogram(filtered_df, x="price")
