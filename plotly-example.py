# -*- coding: utf-8 -*-

#import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

py.init_notebook_mode(connected=True)


trace = go.Bar(x = ['Banana', 'Maçã', 'Uva'], y = [10, 20, 30])

data = [trace]
py.iplot(data)
