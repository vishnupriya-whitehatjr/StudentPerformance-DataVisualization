import pandas as pd
import plotly.express as px
import statistics

data = pd.read_csv('data.csv')
mean = data.groupby(["student_id","level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x = 'student_id', y = 'level', color = "attempt")
fig.show()