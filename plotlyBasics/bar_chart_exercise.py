import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("../Data/mocksurvey.csv")
print(df.head())

columns = list(df.columns)
columns.remove('Unnamed: 0')
print(columns)
data = []
for col in columns:
    trace = go.Bar(y=df['Unnamed: 0'], x=df[col],orientation='h', name=col)
    data.append(trace)

layout = go.Layout(title='Mock survey results', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
