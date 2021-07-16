import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x, y=random_y, mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51,204,153)',
                       symbol='pentagon',
                       line={'width': 2}
                   ))]
layout = go.Layout(title='Hello first plot',
                   xaxis={'title': 'My X axis'},
                   yaxis=dict(title='My Y axis'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='line-plot.html')
