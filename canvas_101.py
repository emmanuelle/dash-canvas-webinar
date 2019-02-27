import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
from dash_canvas import DashCanvas
import dash_core_components as dcc

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    DashCanvas(id='canvas'),
    dcc.Input(id='input', type='text'),
    ])


@app.callback(Output('Input', 'value'),
              [Input('canvas', 'tool')])
def update_width(width):
    return width


if __name__ == '__main__':
    app.run_server(debug=True)
