import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

# from flask import session

from property_price_model import db

# from .layout import html_layout


def create_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    df = pd.read_sql(
        "SELECT * FROM SALE where incode = 'BL6'", db.session.bind,
    )

    # Custom HTML layout
    # dash_app.index_string = html_layout

    fig = px.histogram(df, x="price")

    # Create Layout
    dash_app.layout = html.Div(
        children=[dcc.Graph(id="histogram-graph", figure=fig,),],
        id="dash-container",
    )
    return dash_app.server


def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table
