import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_canvas
from dash_canvas import DashCanvas
from dash_canvas.utils.io_utils import (image_string_to_PILImage,
                                        array_to_data_url)
import numpy as np
import dash_core_components as dcc
from skimage import io

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

filename = 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Mitochondria%2C_mammalian_lung_-_TEM_%282%29.jpg'
canvas_width = 500
canvas_height = 500
scale = 1
"""
img = io.imread(filename, as_gray=True)
height, width = img.shape
canvas_height = round(height * canvas_width / width)
scale = canvas_width / width
"""


app.layout = html.Div([
    DashCanvas(id='canvas',
               tool='line',
               lineWidth=5,
               filename=filename,
               width=canvas_width,
               height=canvas_height,
               scale=scale),
    dcc.Input(id='input',
              type='text'),
    ])


@app.callback(Output('Input', 'value'),
              [Input('canvas', 'tool')])
def update_width(width):
    return width


if __name__ == '__main__':
    app.run_server(port=8054, debug=True)
