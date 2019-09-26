# -*- coding: utf-8 -*-

import plotly.offline as py
import plotly.graph_objs as go
import os, time

print "[*] Iniciando script..."
time.sleep(2)
print "[*] Gerando gráficos..."
time.sleep(1)
print "[!] Gráficos gerados com sucesso!! \o/"
time.sleep(1)
print "[*] Abrindo a visualização..."
time.sleep(1)

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

data = go.Pie(labels=labels, values=values)

py.plot({"data": data, \
	"layout": go.Layout(title="Relatório de Malwares | Created by: João Neto")}, \
	filename="index.html", \
	auto_open=True)