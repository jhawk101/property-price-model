import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.H1('Postcode Sales'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Bolton', 'value': 'BL6'},
            {'label': 'Archway', 'value': 'N19'},
            {'label': 'Penrith', 'value': 'CA22'}
        ],
        value='BL6'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})