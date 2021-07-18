import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../Data/mpg.csv')
# dataset has some modifications
df = df[df['horsepower'].apply(lambda x: x.isnumeric())]
df['horsepower'] = df['horsepower'].astype('int64')
print(df)
print(df.columns)

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=(df['weight'] / 100),
                   color=df['cylinders'],
                   showscale=True))]

layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
