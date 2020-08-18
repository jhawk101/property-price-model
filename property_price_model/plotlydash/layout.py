import dash_core_components as dcc
import dash_html_components as html

layout = html.Div(
    [
        html.H1("Postcode Sales"),
        dcc.Location(id="incode", refresh=True),
        dcc.Graph(id="my-graph"),
    ],
    style={"width": "500"},
)

