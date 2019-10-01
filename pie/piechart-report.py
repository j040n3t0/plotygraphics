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

def createGraph(a,b,c,d,filename): 
	labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
	values = [a,b,c,d]

	data = go.Pie(labels=labels, values=values)

	py.plot({"data": data, \
	        "layout": go.Layout(title="Relatório de Malwares | Created by: João Neto"), \

	        }, \
	        #},
	        filename=filename, \
	        auto_open=False)

print "Criando o 1º gráfico..."
createGraph(5000, 2000, 1053, 500,"graph.html")
print "Criando o 2º gráfico..."
createGraph(4500, 2500, 1753, 1000,"graph3.html")
"""
time.sleep(5)

time.sleep(5)
print "Criando o 3º gráfico..."
createGraph(4000, 3300, 1953, 1500)
time.sleep(5)
print "Criando o ultimo gráfico..."
createGraph(3700, 4100, 1453, 2000)
"""