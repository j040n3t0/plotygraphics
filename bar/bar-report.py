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

index_list = open("example2018.txt").read().splitlines()
types = ['Worms', 'Vírus', 'Trojans']
values = []

for i in range(len(index_list)):
   #print("Entrou no FOR")
   aux = index_list[i]
   #print aux.split(";")
   values.append(int(aux.split(";")[1]))


trace1 = go.Bar(x = types, y = [5, 8, 15], name = "2016")

trace2 = go.Bar(x = types, y = [10, 7, 12], name = "2017")

trace3 = go.Bar(x=types, y=values, name="2018")

data = [trace1, trace2, trace3]

py.plot({"data": data, "layout": go.Layout(title="Relatório de Malwares | Created by: João Neto")}, filename="index.html", auto_open=True)