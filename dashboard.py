import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "dataset.csv")))

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Dance movements'),
                ],
            ),
        ],
    )


def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['Frame'][:30],
                    'y': df['Just_Person_In_Frame'][:30],
                    'name': 'Just_Person_In_Frame',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Frame'][:30],
                    'y': df['Left_Hand_Is_Up'][:30],
                    'name': 'Left_Hand_Is_Up',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Frame'][:30],
                    'y': df['Right_Hand_Is_Up'][:30],
                    'name': 'Right_Hand_Is_Up',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Frame'][:30],
                    'y': df['Both_Hands_Are_Up'][:30],
                    'name': 'Both_Hands_Are_Up',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Frame'][:30],
                    'y': df['There_Is_No_Person'][:30],
                    'name': 'There_Is_No_Person',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]
)
