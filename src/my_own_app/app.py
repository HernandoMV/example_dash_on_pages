# create an interactive plot with dash and plotly
# use panel to serve the app
# use the fast template
# use the awesome-panel favicon
# use the awesome-panel site_url

import panel as pn
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Create a Dash app
app = dash.Dash(__name__)

# create a plotly figure
df = pd.DataFrame(np.random.randn(1000, 2), columns=["a", "b"])
fig = go.Figure(data=[go.Histogram2dContour(x=df["a"], y=df["b"], contours=dict(coloring="heatmap"))])


# Create a Dash layout
app.layout = html.Div(
    [
        html.H1("Hello Dash"),
        html.Div(
            "Dash: A web application framework for Python."
        ),
        # Add the plotly figure to the Dash layout
        dcc.Graph(
            id="example-graph",
            figure=fig,
        ),
    ]
)

# Create a Panel layout
pn.extension(sizing_mode="stretch_width", template="fast")
pn.state.template.param.update(
    site_url="https://awesome-panel.org",
    site="Awesome Panel",
    title="My awesome app",
    favicon="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico",
)

# Serve the app with Panel
pn.panel(app).servable()

# Path: src\my_own_app\app.py

