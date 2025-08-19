from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


def make_dash(server):
    return Dash(
        server=server,
        url_base_pathname='/dash/'
    )


def make_layout(X, Y):
    print('_____________________Функция make_layout начала свою работу_____________________')
    df = pd.read_csv("test.csv")
    centroids = df.groupby('cluster')[['x', 'y']].mean().reset_index()
    scatter = px.scatter(
        df,
        x='x',
        y='y',
        color="color",
        width=1500,
        title="Result:",
        height=1500,
    )
    scatter.update_layout(
        xaxis_title=f'{X}',
        yaxis_title=f'{Y}'
    )
    scatter.add_scatter(x=centroids['x'], y=centroids['y'], mode='markers', marker=dict(size=10, color='black'),
                        name='Centroids')
    left_fig = html.Div(children=dcc.Graph(figure=scatter))
    upper_div = html.Div([left_fig], style={"display": "flex"})
    central_div = html.Div(
        style={"display": "flex", "justify-content": "center"},
    )
    print('_____________________Функция make_layout закончила свою работу_____________________')
    return html.Div([upper_div, central_div])









