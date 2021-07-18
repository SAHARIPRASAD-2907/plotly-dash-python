import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("../Data/abalone.csv")

d = np.random.choice(df['rings'],10,replace=False)
d2 = np.random.choice(df['rings'],10,replace=False)

data = [go.Box(y=d,name='Data'),
        go.Box(y=d2,name="data2")]
pyo.plot(data)