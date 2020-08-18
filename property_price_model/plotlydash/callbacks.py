import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

from property_price_model import db

df = pd.read_sql("SELECT * FROM SALE", db.session.bind,)


def register_callbacks(dashapp):
    @dashapp.callback(Output("my-graph", "figure"), [Input("incode", "hash")])
    def update_graph(incode):
        incode = incode[1:]
        filtered_df = df[df["incode"] == incode]
        return px.histogram(filtered_df, x="price")
