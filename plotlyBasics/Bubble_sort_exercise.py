import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Data/mpg.csv')
# dataset has some modifications
df = df[df['horsepower'].apply(lambda x: x.isnumeric())]
df['horsepower'] = df['horsepower'].astype('int64')
print(df)

data = [go.Scatter(x=df['displacement'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight'] / 400))]

layout = go.Layout(hovermode='closest', title='My bubble solution')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
