from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
from datetime import date
import plotly.express as px




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, title='Dashboard', external_stylesheets=external_stylesheets)

#df = pd.read_csv('00_Aux_files/out.csv')

today = date.today()


app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input 1: ",
        dcc.Input(id='my-input1', value='', type='number'),
        html.Br(),
        "Input 2: ",
        dcc.Input(id='my-input2', value='', type='number'),
        html.Br(),
        "Input 2: ",
        dcc.Input(id='my-input3', value='', type='number'),
        html.Br(),
        "Input 2: ",
        dcc.Input(id='my-input4', value='', type='number')

    ]),
    html.Br(),
    html.Button('Click here', id='my-button', n_clicks=0),
    html.Br(),
    html.Div(id='my-output'),
    html.Br(),
    html.Br(),
    dcc.Graph(id='graph-output', figure={}),


])
#li=[]
#
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Output(component_id='graph-output', component_property='figure'),
    Input(component_id='my-button', component_property='n_clicks'),
    State(component_id='my-input1', component_property='value'),
    State(component_id='my-input2', component_property='value'),
    State(component_id='my-input3', component_property='value'),
    State(component_id='my-input4', component_property='value'),
    prevent_initial_call=True

)

def update_output_div(n, iv1, iv2, iv3, iv4 ):
    df = pd.read_csv('00_Aux_files/out.csv', index_col="ID")
    i = df.last_valid_index()
    li = [today, iv1, iv2, iv3, iv4]
    df_volatyl = pd.DataFrame([li], columns=['Date', 'Input v1', 'Input v2', 'Input v3', 'Input v4'], index=[i+1])
    dff = pd.concat([df, df_volatyl])
    dff.to_csv('00_Aux_files/out.csv', index_label='ID')

    pr_df = precess_df(dff)
    fig = px.line(pr_df, x=pr_df.index, y=['Result 1', 'Result 2'], title='RESULTS')

    return 'Values %s, %s, %s, %s are added!' % (iv1, iv2, iv3, iv4), fig

def precess_df(x):
    new_x = pd.DataFrame()
    new_x['Date'] = x['Date']
    new_x['Result 1'] = x['Input v1'] + x['Input v2']
    new_x['Result 2'] = x['Input v3'] + x['Input v4']
    return new_x

if __name__ == '__main__':
    app.run_server(debug=True)
