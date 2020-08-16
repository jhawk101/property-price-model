import numpy as np
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

# from .layout import html_layout


def postcode_histogram(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/postcode_histogram/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    
    df = pd.DataFrame(
        data={
            "sqft": [100, 150, 250, 450, 600],
            "price": [200000, 215000, 250000, 345000, 460000],
            "beds": [1, 1, 2, 3, 3],
        }
    )

    # Custom HTML layout
    # dash_app.index_string = html_layout

    fig = px.scatter(df, x="sqft", y="price", color="beds")

    # Create Layout
    dash_app.layout = html.Div(
        children=[dcc.Graph(id="scatter-graph", figure=fig,),],
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
