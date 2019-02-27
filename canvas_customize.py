import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_canvas
from dash_canvas import DashCanvas
from dash_canvas.utils.io_utils import (image_string_to_PILImage,
                                        array_to_data_url)
import numpy as np
import dash_core_components as dcc

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    DashCanvas(id='canvas',
               tool='line',
               lineWidth=5,
               lineColor='red',
               width=700,
               height=400,),
    dcc.Input(id='input',
              type='text'),
    ])


@app.callback(Output('Input', 'value'),
              [Input('canvas', 'tool')])
def update_width(width):
    return width

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
