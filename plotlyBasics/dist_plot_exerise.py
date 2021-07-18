import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

df = pd.read_csv('../Data/iris.csv')
print(df.head())

trace0 = df[df['class'] == 'Iris-setosa']['petal_length']
trace1 = df[df['class'] == 'Iris-versicolor']['petal_length']
trace2 = df[df['class'] == 'Iris-virginica']['petal_length']

hist_data = [trace0, trace1, trace2]
group_label = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

fig = ff.create_distplot(hist_data, group_label)
pyo.plot(fig)
