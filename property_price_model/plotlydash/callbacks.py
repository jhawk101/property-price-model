import numpy as np
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from sqlalchemy import create_engine
from property_price_model.postcodes import augment_sales_data
from flask import current_app


def register_callbacks(dashapp):
    @dashapp.callback(
        [
            Output("postcode-sales-hist", "figure"),
            Output("postcode-sales-scatter", "figure"),
            Output("postcode-sales-r-squared", "children"),
            Output("postcode-sales-gradient", "children"),
        ],
        [Input("incode", "hash")],
    )
    def update_histogram(incode):
        if incode:
            incode = incode[1:]
            engine = create_engine(
                current_app.config.get("SQLALCHEMY_DATABASE_URI")
            )
            df = pd.read_sql(
                "SELECT price, incode, saon, paon, street, postcode FROM SALE where incode = %s",
                params=[incode],
                con=engine,
            )
            engine.dispose()
            augmented_df = augment_sales_data(df, incode)
            scatter = px.scatter(
                augmented_df,
                x="total-floor-area",
                y="price",
                color="number-heated-rooms",
                trendline="ols",
            )
            r_squared = scatter._px_trendlines.iloc[0, 0].rsquared
            gradient = int(scatter._px_trendlines.iloc[0, 0].params[1])
            return (
                px.histogram(df, x="price"),
                scatter,
                f"{r_squared:0.1%} of the variance in house prices in this postcode can be explained by the size of the property",
                f"An extra square metre of space costs £{gradient:,} in this postcode",
            )
        else:
            return (
                px.scatter(x=[1, 2, 3], y=[1, 4, 9]),
                px.scatter(x=[1, 2, 3], y=[1, 4, 9]),
                "hello wold",
                "hiya",
            )
