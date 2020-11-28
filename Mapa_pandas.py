#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import folium
import pandas as pd
import json

train_dataset = pd.read_csv('taxa_br.csv')
print(train_dataset.head())
br_estados = 'br_states.json'
geo_json_data = json.load(open(br_estados))


# In[19]:


taxa_coments = pd.read_csv('taxa_br.csv', sep=';', decimal=',', usecols=['Sigla', 'Num_Coments'])
taxa_coments.head(3)
taxa_coments.rename(columns={
     'Sigla': 'estado', 
     'Num_Coments': '2020'}, inplace=True)
taxa_coments.head(3)
taxa_coments.describe()

from branca.colormap import linear
colormap = linear.YlOrRd_09.scale(6,20)
colormap

taxa_comentario_estado = taxa_coments.set_index('estado')['2020']
#desemprego_br_2018 = desemprego_br.set_index('estado')['Num_Coments_Estado']
mapa = folium.Map(
    width=600, height=400,
    location=[-15.77972, -47.92972], 
    zoom_start=4
)
folium.GeoJson(
    geo_json_data,
    name='2020',
    style_function=lambda feature: {
        'fillColor': colormap(taxa_comentario_estado[feature['id']]),
        'color': 'black',
        'weight': 0.3,
    }
    
).add_to(mapa)
colormap.caption = 'Numero de Comentarios por Estado 2020'
colormap.add_to(mapa)
folium.LayerControl(collapsed=False).add_to(mapa)
mapa.save('taxa_br_2020.html')
mapa


# In[ ]:




