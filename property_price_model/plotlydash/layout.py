import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        html.H1("Sales in your postcode, last 3 years"),
        dcc.Location(id="incode", refresh=True),
        dbc.Row(
            [
                dbc.Col(html.Div(id="postcode-sales-r-squared")),
                dbc.Col(html.Div(id="postcode-sales-gradient")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="postcode-sales-hist")),
                dbc.Col(dcc.Graph(id="postcode-sales-scatter")),
            ]
        ),
    ]
)

