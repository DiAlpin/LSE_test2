from dash import Dash, dcc, html, Input, Output
import pandas as pd



app = Dash(__name__)

app.layout = html.Div([

    dcc.Textarea(value='insert Action1', style={'width': '100%', 'height': 20}),
    dcc.RadioItems(['Unfinished', 'Done'], 'Unfinished'),

    html.Hr(),
    dcc.Textarea(value='insert Action2', style={'width': '100%', 'height': 20}),
    dcc.RadioItems(['Unfinished', 'Done'], 'Unfinished'),

    html.Hr(),
    dcc.Textarea(value='insert Action3', style={'width': '100%', 'height': 20}),
    dcc.RadioItems(['Unfinished', 'Done'], 'Unfinished'),

    html.Hr(),
    dcc.Textarea(value='insert Action4', style={'width': '100%', 'height': 20}),
    dcc.RadioItems(['Unfinished', 'Done'], 'Unfinished'),

    html.Hr(),
    dcc.Textarea(value='insert Action5', style={'width': '100%', 'height': 20}),
    dcc.RadioItems(['Unfinished', 'Done'], 'Unfinished'),

])


if __name__ == '__main__':
    app.run_server(debug=True)

