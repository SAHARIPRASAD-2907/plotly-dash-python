import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# normal bar chart
# stacked bar chart
# Nested bar chart

df = pd.read_csv('../Data/2018WinterOlympics.csv')
print(df.head())

trace1 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker={'color': "#FFD700"})
trace2 = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver', marker={'color': "#9EA0A1"})
trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze', marker={'color': "#CD7F32"})

data = [trace1, trace2, trace3]
layout = go.Layout(title='Medals',barmode='stack') # for stacking bar code one over the other
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
