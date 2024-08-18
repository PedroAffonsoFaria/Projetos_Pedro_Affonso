#!/usr/bin/env python
# coding: utf-8

# # GESTÃO DE ESTOQUE MILKY MOO

# **INPUT DAS BIBLIOTECAS NECESSÁRIAS**

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().system('pip install pycaret-ts-alpha')


# **DADOS DE DEMANDA DA PRIMEIRA SEMANA DE TODOS OS PERÍODOS DE DEZEMBRO À JUNHO**

# Foi nos fornecido pela empresa dados da primeira semana de Dez/23 à Jun/24, então imputamos os dados

# In[38]:


dados = [{'produto': 'MALHADA 500ML', 'quantidade': 23, 'subtotal': 506.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MIMOSA 500ML', 'quantidade': 37, 'subtotal': 814.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PANDORA 500ML', 'quantidade': 76, 'subtotal': 1672.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'FILO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'EMILIA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'JUDITE 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'LOLITA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MANHOSA 500ML', 'quantidade': 16, 'subtotal': 352.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MISSY 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'XONADA 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MOO 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'BISA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MINEIRA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PRETA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'BOLINHA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'BRANCA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'RUBI 500ML', 'quantidade': 3, 'subtotal': 105.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 47, 'subtotal': 1034.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PODEROSA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':1},  
    {'produto': 'FIONA 500ml', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PEROLA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MALHADA 300ML', 'quantidade': 50, 'subtotal': 900.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MIMOSA 300ML', 'quantidade': 47, 'subtotal': 846.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PANDORA 300ML', 'quantidade': 162, 'subtotal': 2916.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'FILO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'AMERICANA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'EMILIA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'JUDITE 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'LOLITA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MANHOSA 300ML', 'quantidade': 33, 'subtotal': 594.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MISSY 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'XONADA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MOO 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'BISA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'MINEIRA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'PRETA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'BOLINHA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 17, 'subtotal': 306.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'BRANCA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 8, 'subtotal': 200.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'RUBI 300ML', 'quantidade': 16, 'subtotal': 400.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'GINA 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'CACAU 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Janeiro','semana':1},
    {'produto': 'DIVA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Janeiro','semana':1},
    {'produto':'DOMINO 300ML','quantidade':3,'subtotal':54.00, 'mes':'Janeiro','semana':1},
    {'produto': 'DORI 300ML','quantidade':1,'subtotal':18.00,'mes':'Janeiro','semana':1},
    {'produto': 'HOLANDESA 300ML','quantidade':2,'subtotal':36.00,'mes':'Janeiro','semana':1},
    {'produto': 'PRECIOSA 300ML','quantidade':61,'subtotal':1098.00,'mes':'Janeiro','semana':1},
    {'produto': 'TEMPESTADE 300ML','quantidade':3,'subtotal':54.00,'mes':'Janeiro','semana':1},
    {'produto': 'PODEROSA 300ML','quantidade':5,'subtotal':90.00,'mes':'Janeiro','semana':1},
    {'produto': 'FIONA 300ML','quantidade':4, 'subtotal':72.00,'mes':'Janeiro','semana':1},
    {'produto': 'MALHADA 500ML', 'quantidade': 19, 'subtotal': 418.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MIMOSA 500ML', 'quantidade': 19, 'subtotal': 418.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PANDORA 500ML', 'quantidade': 78, 'subtotal': 1716.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'FILO 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'EMILIA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'LOLITA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MANHOSA 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MISSY 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'XONADA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MOO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'BISA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MINEIRA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PRETA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'BRANCA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'RUBI 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'DIVA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'DOMINO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 34, 'subtotal': 748.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PODEROSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'FIONA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'ESTRELA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MALHADA 300ML', 'quantidade': 39, 'subtotal': 702.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MIMOSA 300ML', 'quantidade': 83, 'subtotal': 1494.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PANDORA 300ML', 'quantidade': 153, 'subtotal': 2754.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 18, 'subtotal': 324.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'FILO 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'AMERICANA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'DENGOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'EMILIA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'JUDITE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'LOLITA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MANHOSA 300ML', 'quantidade': 36, 'subtotal': 648.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MISSY 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'XONADA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MOO 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'BISA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'MINEIRA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PRETA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'BOLINHA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'BRANCA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'RUBI 300ML', 'quantidade': 5, 'subtotal': 125.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'DIVA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'DOMINO 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 67, 'subtotal': 1206.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'PODEROSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'FIONA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Janeiro','semana':2},
    {'produto': 'ESTRELA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Janeiro','semana':2},     
    {'produto': 'PEROLA 300 ML','quantidade':1,'subtotal':27.00,'mes':'Janeiro','semana':2 },
    {'produto': 'MALHADA 500ML', 'quantidade': 23, 'subtotal': 506.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MIMOSA 500ML', 'quantidade': 34, 'subtotal': 748.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PANDORA 500ML', 'quantidade': 55, 'subtotal': 1210.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'EMILIA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 13, 'subtotal': 286.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MANHOSA 500ML', 'quantidade': 15, 'subtotal': 330.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MISSY 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'BISA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'BRANCA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'RUBI 500ML', 'quantidade': 3, 'subtotal': 105.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DORI 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 27, 'subtotal': 594.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'FIONA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'ESTRELA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MALHADA 300ML', 'quantidade': 40, 'subtotal': 720.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MIMOSA 300ML', 'quantidade': 49, 'subtotal': 882.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PANDORA 300ML', 'quantidade': 123, 'subtotal': 2214.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'FILO 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'AMERICANA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DENGOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'EMILIA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'LOLITA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MANHOSA 300ML', 'quantidade': 21, 'subtotal': 378.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MISSY 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'XONADA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MOO 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'BISA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MINEIRA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PRETA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'BOLINHA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'BRANCA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'RUBI 300ML', 'quantidade': 5, 'subtotal': 125.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DIVA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DOMINO 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'DORI 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 46, 'subtotal': 828.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'PODEROSA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'FIONA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'ESTRELA 300ML', 'quantidade': 9, 'subtotal': 243.00, 'mes': 'Janeiro','semana':3},
    {'produto': 'MALHADA 500ML', 'quantidade': 24, 'subtotal': 528.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MIMOSA 500ML', 'quantidade': 35, 'subtotal': 770.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PANDORA 500ML', 'quantidade': 81, 'subtotal': 1782.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'FILO 500ML', 'quantidade': 12, 'subtotal': 264.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'DENGOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'EMILIA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'JUDITE 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MANHOSA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MISSY 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'XONADA 500ML', 'quantidade': 6, 'subtotal': 98.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MOO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'BISA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PRETA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'BRANCA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'RUBI 500ML', 'quantidade': 3, 'subtotal': 105.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'DIVA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'DOMINO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'DORI 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 39, 'subtotal': 858.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PODEROSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'ESTRELA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MALHADA 300ML', 'quantidade': 40, 'subtotal': 720.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MIMOSA 300ML', 'quantidade': 64, 'subtotal': 1152.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PANDORA 300ML', 'quantidade': 135, 'subtotal': 2430.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'FILO 300ML', 'quantidade': 18, 'subtotal': 324.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'AMERICANA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'DENGOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'EMILIA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'JUDITE 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'LOLITA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MANHOSA 300ML', 'quantidade': 23, 'subtotal': 414.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MISSY 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'XONADA 300ML', 'quantidade': 23, 'subtotal': 324.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MOO 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'BISA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MINEIRA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PRETA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'BOLINHA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 21, 'subtotal': 378.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'BRANCA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 6, 'subtotal': 150.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'RUBI 300ML', 'quantidade': 6, 'subtotal': 150.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'GINA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'DIVA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'DOMINO 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 51, 'subtotal': 918.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'PODEROSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'ESTRELA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Janeiro','semana':4},
    {'produto': 'MALHADA 500ML', 'quantidade': 18, 'subtotal': 396.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MIMOSA 500ML', 'quantidade': 24, 'subtotal': 528.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PANDORA 500ML', 'quantidade': 65, 'subtotal': 1430.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'FILO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'AMERICANA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'EMILIA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'JUDITE 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'LOLITA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MANHOSA 500ML', 'quantidade': 14, 'subtotal': 308.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MISSY 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'XONADA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MOO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'BISA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MINEIRA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PRETA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Fevereiro'},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'RUBI 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'CACAU 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 25, 'subtotal': 550.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PODEROSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'ESTRELA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PEROLA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MALHADA 300ML', 'quantidade': 66, 'subtotal': 1188.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MIMOSA 300ML', 'quantidade': 70, 'subtotal': 1260.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PANDORA 300ML', 'quantidade': 123, 'subtotal': 2214.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'FILO 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'DENGOSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'EMILIA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'JUDITE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'LOLITA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MANHOSA 300ML', 'quantidade': 21, 'subtotal': 378.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MISSY 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'XONADA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MOO 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'BISA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'MINEIRA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PRETA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'BOLINHA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'BRANCA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 9, 'subtotal': 225.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'RUBI 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'GINA 300ML', 'quantidade': 5, 'subtotal': 125.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'DIVA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'DOMINO 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 49, 'subtotal': 882.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PODEROSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'ESTRELA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':6},
    {'produto': 'PEROLA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':6},     
    {'produto': 'MALHADA 500ML', 'quantidade': 32, 'subtotal': 704.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MIMOSA 500ML', 'quantidade': 42, 'subtotal': 924.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PANDORA 500ML', 'quantidade': 110, 'subtotal': 2420.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'FILO 500ML', 'quantidade': 11, 'subtotal': 242.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'EMILIA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 12, 'subtotal': 264.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'LOLITA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MANHOSA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MISSY 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'XONADA 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'XONADA 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MOO 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'BISA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MINEIRA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PRETA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'BRANCA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 6, 'subtotal': 210.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'RUBI 500ML', 'quantidade': 5, 'subtotal': 175.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'CACAU 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DIVA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DORI 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 39, 'subtotal': 858.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PODEROSA 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'ESTRELA 500ML', 'quantidade': 6, 'subtotal': 192.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MALHADA 300ML', 'quantidade': 63, 'subtotal': 1134.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MIMOSA 300ML', 'quantidade': 82, 'subtotal': 1476.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PANDORA 300ML', 'quantidade': 177, 'subtotal': 3186.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'FILO 300ML', 'quantidade': 18, 'subtotal': 324.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'AMERICANA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DENGOSA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'EMILIA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'JUDITE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'LOLITA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MANHOSA 300ML', 'quantidade': 29, 'subtotal': 522.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MISSY 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'XONADA 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MOO 300ML', 'quantidade': 17, 'subtotal': 306.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'BISA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'MINEIRA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PRETA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'BOLINHA 300ML', 'quantidade': 16, 'subtotal': 288.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 23, 'subtotal': 414.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'BRANCA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'JOIA RARA 300ML', 'quantidade':11 , 'subtotal': 275.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'RUBI 300ML', 'quantidade': 4, 'subtotal': 100.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'GINA 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'CACAU 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DIVA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DOMINO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'DORI 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 84, 'subtotal': 1512.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PODEROSA 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'ESTRELA 300ML', 'quantidade': 10, 'subtotal': 270.00, 'mes': 'Fevereiro','semana':5},
    {'produto': 'PEROLA 300ML','quantidade':4,'subtotal':108.00,'mes':'Fevereiro','semana':5},
    {'produto': 'MALHADA 500ML', 'quantidade': 73, 'subtotal': 748.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MIMOSA 500ML', 'quantidade': 74, 'subtotal': 594.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PANDORA 500ML', 'quantidade': 79, 'subtotal': 1738.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'FILO 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'DENGOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'EMILIA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'LOLITA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MANHOSA 500ML', 'quantidade': 17, 'subtotal': 374.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MISSY 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'XONADA 500ML', 'quantidade': 7, 'subtotal': 137.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MOO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'BISA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MINEIRA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PRETA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'BRANCA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'RUBI 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'DOMINO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 31, 'subtotal': 682.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PODEROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'ESTRELA 500ML', 'quantidade': 3, 'subtotal': 96.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MALHADA 300ML', 'quantidade': 58, 'subtotal': 1044.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MIMOSA 300ML', 'quantidade': 57, 'subtotal': 1026.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PANDORA 300ML', 'quantidade': 107, 'subtotal': 1926.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'FILO 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'DENGOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'EMILIA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'JUDITE 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'LOLITA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MANHOSA 300ML', 'quantidade': 17, 'subtotal': 306.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MISSY 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'XONADA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'MOO 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'BISA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PRETA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'BOLINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'BRANCA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'RUBI 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'GINA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'CACAU 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'DIVA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'DOMINO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 61, 'subtotal': 1098.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'PODEROSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Fevereiro','semana':7},
    {'produto': 'ESTRELA 300ML', 'quantidade': 4, 'subtotal': 108.00, 'mes': 'Fevereiro','semana':7},    
    {'produto': 'MALHADA 500ML', 'quantidade': 45, 'subtotal': 990.00, 'mes': 'Março','semana':8},
    {'produto': 'MIMOSA 500ML', 'quantidade': 74, 'subtotal': 1628.00, 'mes': 'Março','semana':8},
    {'produto': 'PANDORA 500ML', 'quantidade': 167, 'subtotal': 3674.00, 'mes': 'Março','semana':8},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Março','semana':8},
    {'produto': 'FILO 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Março','semana':8},
    {'produto': 'AMERICANA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':8},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':8},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':8},
    {'produto': 'EMILIA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':8},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 21, 'subtotal': 462.00, 'mes': 'Março','semana':8},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Março','semana':8},
    {'produto': 'JUDITE 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':8},
    {'produto': 'LOLITA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':8},
    {'produto': 'MANHOSA 500ML', 'quantidade': 21, 'subtotal': 462.00, 'mes': 'Março','semana':8},
    {'produto': 'MISSY 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':8},
    {'produto': 'XONADA 500ML', 'quantidade': 12, 'subtotal': 264.00, 'mes': 'Março','semana':8},
    {'produto': 'XONADA 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Março','semana':8},
    {'produto': 'MOO 500ML', 'quantidade': 12, 'subtotal': 264.00, 'mes': 'Março','semana':8},
    {'produto': 'BISA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Março','semana':8},
    {'produto': 'MINEIRA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':8},
    {'produto': 'PRETA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Março','semana':8},
    {'produto': 'BOLINHA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':8},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':8},
    {'produto': 'BRANCA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':8},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Março','semana':8},
    {'produto': 'RUBI 500ML', 'quantidade': 3, 'subtotal': 105.00, 'mes': 'Março','semana':8},
    {'produto': 'CACAU 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':8},
    {'produto': 'DIVA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Março','semana':8},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':8},
    {'produto': 'DORI 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':8},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':8},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 71, 'subtotal': 1562.00, 'mes': 'Março','semana':8},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':8},
    {'produto': 'PODEROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':8},
    {'produto': 'ESTRELA 500ML', 'quantidade': 5, 'subtotal': 160.00, 'mes': 'Março','semana':8},
    {'produto': 'CARMELA 500ML', 'quantidade': 15, 'subtotal': 330.00, 'mes': 'Março','semana':8},
    {'produto': 'MALHADA 300ML', 'quantidade': 85, 'subtotal': 1530.00, 'mes': 'Março','semana':8},
    {'produto': 'MIMOSA 300ML', 'quantidade': 102, 'subtotal': 1836.00, 'mes': 'Março','semana':8},
    {'produto': 'PANDORA 300ML', 'quantidade': 229, 'subtotal': 4122.00, 'mes': 'Março','semana':8},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 18, 'subtotal': 324.00, 'mes': 'Março','semana':8},
    {'produto': 'FILO 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Março','semana':8},
    {'produto': 'AMERICANA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':8},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':8},
    {'produto': 'DENGOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':8},
    {'produto': 'EMILIA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':8},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 18, 'subtotal': 324.00, 'mes': 'Março','semana':8},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Março','semana':8},
    {'produto': 'JUDITE 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':8},
    {'produto': 'LOLITA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':8},
    {'produto': 'MANHOSA 300ML', 'quantidade': 51, 'subtotal': 918.00, 'mes': 'Março','semana':8},
    {'produto': 'MISSY 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Março','semana':8},
    {'produto': 'XONADA 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Março','semana':8},
    {'produto': 'MOO 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Março','semana':8},
    {'produto': 'BISA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Março','semana':8},
    {'produto': 'MINEIRA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Março','semana':8},
    {'produto': 'PRETA 300ML', 'quantidade': 19, 'subtotal': 342.00, 'mes': 'Março','semana':8},
    {'produto': 'BOLINHA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Março','semana':8},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 21, 'subtotal': 378.00, 'mes': 'Março','semana':8},
    {'produto': 'BRANCA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Março','semana':8},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 5, 'subtotal': 125.00, 'mes': 'Março','semana':8},
    {'produto': 'RUBI 300ML', 'quantidade': 6, 'subtotal': 150.00, 'mes': 'Março','semana':8},
    {'produto': 'GINA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Março','semana':8},
    {'produto': 'CACAU 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':8},
    {'produto': 'DIVA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Março','semana':8},
    {'produto': 'DOMINO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':8},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':8},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 69, 'subtotal': 1242.00, 'mes': 'Março','semana':8},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Março','semana':8},
    {'produto': 'PODEROSA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Março','semana':8},
    {'produto': 'ESTRELA 300ML', 'quantidade': 9, 'subtotal': 243.00, 'mes': 'Março','semana':8},
    {'produto': 'CARMELA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':8},
    {'produto': 'MALHADA 500ML', 'quantidade': 13, 'subtotal': 286.00, 'mes': 'Março','semana':9},
    {'produto': 'MIMOSA 500ML', 'quantidade': 25, 'subtotal': 550.00, 'mes': 'Março','semana':9},
    {'produto': 'PANDORA 500ML', 'quantidade': 64, 'subtotal': 1408.00, 'mes': 'Março','semana':9},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':9},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':9},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':9},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':9},
    {'produto': 'EMILIA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':9},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':9},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Março','semana':9},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':9},
    {'produto': 'MANHOSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Março','semana':9},
    {'produto': 'MISSY 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':9},
    {'produto': 'XONADA 500ML', 'quantidade': 3, 'subtotal': 49.00, 'mes': 'Março','semana':9},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':9},
    {'produto': 'BISA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Março','semana':9},
    {'produto': 'MINEIRA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':9},
    {'produto': 'PRETA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':9},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':9},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':9},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':9},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 26, 'subtotal': 572.00, 'mes': 'Março','semana':9},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':9},
    {'produto': 'PODEROSA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Março','semana':9},
    {'produto': 'ESTRELA 500ML', 'quantidade': 8, 'subtotal': 256.00, 'mes': 'Março','semana':9},
    {'produto': 'MINEIRA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'BISA 500ml TIME', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':9},
    {'produto': 'BRANCA 500ml TIME', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':9},
    {'produto': 'MISSY 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'PINTADINHA 500ml TIME', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':9},
    {'produto': 'FILO 500ml TIME', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Março','semana':9},
    {'produto': 'CACAU 500ml TIME', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':9},
    {'produto': 'CHICLETIN 500ml TIME', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março'},
    {'produto': 'PRETA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março'},
    {'produto': 'CHEIROSA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'MALHADA 300ML', 'quantidade': 30, 'subtotal': 540.00, 'mes': 'Março','semana':9},
    {'produto': 'MIMOSA 300ML', 'quantidade': 42, 'subtotal': 756.00, 'mes': 'Março','semana':9},
    {'produto': 'PANDORA 300ML', 'quantidade': 123, 'subtotal': 2214.00, 'mes': 'Março','semana':9},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Março','semana':9},
    {'produto': 'FILO 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Março','semana':9},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'DENGOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':9},
    {'produto': 'EMILIA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Março','semana':9},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':9},
    {'produto': 'JUDITE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':9},
    {'produto': 'MANHOSA 300ML', 'quantidade': 24, 'subtotal': 432.00, 'mes': 'Março','semana':9},
    {'produto': 'MISSY 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':9},
    {'produto': 'XONADA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':9},
    {'produto': 'MOO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':9},
    {'produto': 'BISA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Março','semana':9},
    {'produto': 'MINEIRA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':9},
    {'produto': 'PRETA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':9},
    {'produto': 'BOLINHA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Março','semana':9},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Março','semana':9},
    {'produto': 'BRANCA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Março','semana':9},
    {'produto': 'RUBI 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Março','semana':9},
    {'produto': 'GINA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Março','semana':9},
    {'produto': 'CACAU 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'DIVA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Março','semana':9},
    {'produto': 'DOMINO 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':9},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':9},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 43, 'subtotal': 774.00, 'mes': 'Março','semana':9},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':9},
    {'produto': 'PODEROSA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':9},
    {'produto': 'ESTRELA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Março','semana':9},
    {'produto': 'CARMELA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Março','semana':9},
    {'produto': 'MISSY 300ml TIME', 'quantidade': 3, 'subtotal': 42.00, 'mes': 'Março','semana':9},
    {'produto': 'CHICLETIN 300ml TIME', 'quantidade': 6, 'subtotal': 84.00, 'mes': 'Março','semana':9},
    {'produto': 'PRETA 300ml TIME', 'quantidade': 4, 'subtotal': 56.00, 'mes': 'Março','semana':9},
    {'produto': 'CHEIROSA 300ml TIME', 'quantidade': 1, 'subtotal': 14.00, 'mes': 'Março','semana':9},
    {'produto': 'MALHADA 500ML', 'quantidade': 18, 'subtotal': 396.00, 'mes': 'Março','semana':10},
    {'produto': 'MIMOSA 500ML', 'quantidade': 30, 'subtotal': 660.00, 'mes': 'Março','semana':10},
    {'produto': 'PANDORA 500ML', 'quantidade': 77, 'subtotal': 1694.00, 'mes': 'Março','semana':10},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Março','semana':10},
    {'produto': 'FILO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':10},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':10},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Março','semana':10},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':10},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':10},
    {'produto': 'MANHOSA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Março','semana':10},
    {'produto': 'MISSY 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':10},
    {'produto': 'XONADA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':10},
    {'produto': 'MOO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Março','semana':10},
    {'produto': 'BISA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':10},
    {'produto': 'MINEIRA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':10},
    {'produto': 'PRETA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':10},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':10},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':10},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 39, 'subtotal': 858.00, 'mes': 'Março','semana':10},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':10},
    {'produto': 'PODEROSA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Março','semana':10},
    {'produto': 'ESTRELA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Março','semana':10},
    {'produto': 'PEROLA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Março','semana':10},
    {'produto': 'CARMELA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':10},
    {'produto': 'MINEIRA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':10},
    {'produto': 'BISA 500ml TIME', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'BRANCA 500ml TIME', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':10},
    {'produto': 'MISSY 500ml TIME', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':10},
    {'produto': 'LOLITA 500ml TIME', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'PINTADINHA 500ml TIME', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'FILO 500ml TIME', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':10},
    {'produto': 'CHICLETIN 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':10},
    {'produto': 'PRETA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':10},
    {'produto': 'CHEIROSA 500ml TIME', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'MALHADA 300ML', 'quantidade': 37, 'subtotal': 630.00, 'mes': 'Março','semana':10},
    {'produto': 'MIMOSA 300ML', 'quantidade': 38, 'subtotal': 756.00, 'mes': 'Março','semana':10},
    {'produto': 'PANDORA 300ML', 'quantidade': 77, 'subtotal': 1386.00, 'mes': 'Março','semana':10},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Março','semana':10},
    {'produto': 'FILO 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':10},
    {'produto': 'AMERICANA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':10},
    {'produto': 'DENGOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':10},
    {'produto': 'EMILIA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':10},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Março','semana':10},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'JUDITE 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':10},
    {'produto': 'LOLITA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'MANHOSA 300ML', 'quantidade': 18, 'subtotal': 324.00, 'mes': 'Março','semana':10},
    {'produto': 'MISSY 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':10},
    {'produto': 'XONADA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':10},
    {'produto': 'MOO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':10},
    {'produto': 'BISA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':10},
    {'produto': 'PRETA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'BOLINHA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Março','semana':10},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Março','semana':10},
    {'produto': 'RUBI 300ML', 'quantidade': 5, 'subtotal': 125.00, 'mes': 'Março','semana':10},
    {'produto': 'GINA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Março','semana':10},
    {'produto': 'CACAU 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'DIVA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':10},
    {'produto': 'DOMINO 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':10},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':10},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 42, 'subtotal': 756.00, 'mes': 'Março','semana':10},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':10},
    {'produto': 'PODEROSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':10},
    {'produto': 'ESTRELA 300ML', 'quantidade': 7, 'subtotal': 189.00, 'mes': 'Março','semana':10},
    {'produto': 'CARMELA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':10},
    {'produto': 'MISSY 300ml TIME', 'quantidade': 2, 'subtotal': 28.00, 'mes': 'Março','semana':10},
    {'produto': 'CHICLETIN 300ml TIME', 'quantidade': 3, 'subtotal': 42.00, 'mes': 'Março','semana':10},
    {'produto': 'PRETA 300ml TIME', 'quantidade': 5, 'subtotal': 70.00, 'mes': 'Março','semana':10},
    {'produto': 'CHEIROSA 300ml TIME', 'quantidade': 3, 'subtotal': 42.00, 'mes': 'Março','semana':10},
    {'produto': 'MALHADA 500ML', 'quantidade': 15, 'subtotal': 330.00, 'mes': 'Março','semana':11},
    {'produto': 'MIMOSA 500ML', 'quantidade': 19, 'subtotal': 418.00, 'mes': 'Março','semana':11},
    {'produto': 'PANDORA 500ML', 'quantidade': 73, 'subtotal': 1606.00, 'mes': 'Março','semana':11},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':11},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':11},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':11},
    {'produto': 'EMILIA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':11},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':11},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':11},
    {'produto': 'JUDITE 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':11},
    {'produto': 'LOLITA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':11},
    {'produto': 'MANHOSA 500ML', 'quantidade': 11, 'subtotal': 242.00, 'mes': 'Março','semana':11},
    {'produto': 'MISSY 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Março','semana':11},
    {'produto': 'XONADA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Março','semana':11},
    {'produto': 'MOO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':11},
    {'produto': 'BISA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Março','semana':11},
    {'produto': 'PRETA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Março','semana':11},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':11},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':11},
    {'produto': 'BRANCA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':11},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Março','semana':11},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 5, 'subtotal': 175.00, 'mes': 'Março','semana':11},
    {'produto': 'RUBI 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Março','semana':11},
    {'produto': 'GINA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Março','semana':11},
    {'produto': 'DOMINO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Março','semana':11},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':11},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 13, 'subtotal': 286.00, 'mes': 'Março','semana':11},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Março','semana':11},
    {'produto': 'PODEROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':11},
    {'produto': 'ESTRELA 500ML', 'quantidade': 3, 'subtotal': 96.00, 'mes': 'Março','semana':11},
    {'produto': 'PEROLA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Março','semana':11},
    {'produto': 'CARMELA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Março','semana':11},
    {'produto': 'MALHADA 300ML', 'quantidade': 36, 'subtotal': 648.00, 'mes': 'Março','semana':11},
    {'produto': 'MIMOSA 300ML', 'quantidade': 50, 'subtotal': 900.00, 'mes': 'Março','semana':11},
    {'produto': 'PANDORA 300ML', 'quantidade': 91, 'subtotal': 1638.00, 'mes': 'Março','semana':11},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':11},
    {'produto': 'FILO 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':11},
    {'produto': 'AMERICANA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':11},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':11},
    {'produto': 'DENGOSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':11},
    {'produto': 'EMILIA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':11},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Março','semana':11},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Março','semana':11},
    {'produto': 'JUDITE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':11},
    {'produto': 'LOLITA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':11},
    {'produto': 'MANHOSA 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Março','semana':11},
    {'produto': 'MISSY 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':11},
    {'produto': 'XONADA 300ML', 'quantidade': 7, 'subtotal': 108.00, 'mes': 'Março','semana':11},
    {'produto': 'MOO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':11},
    {'produto': 'BISA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Março','semana':11},
    {'produto': 'MINEIRA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':11},
    {'produto': 'PRETA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':11},
    {'produto': 'BOLINHA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':11},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Março','semana':11},
    {'produto': 'BRANCA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':11},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Março','semana':11},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 8, 'subtotal': 200.00, 'mes': 'Março','semana':11},
    {'produto': 'RUBI 300ML', 'quantidade': 4, 'subtotal': 100.00, 'mes': 'Março','semana':11},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':11},
    {'produto': 'DIVA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Março','semana':11},
    {'produto': 'DOMINO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Março','semana':11},
    {'produto': 'DORI 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Março','semana':11},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Março','semana':11},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 41, 'subtotal': 738.00, 'mes': 'Março','semana':11},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Março','semana':11},
    {'produto': 'PODEROSA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Março','semana':11},
    {'produto': 'ESTRELA 300ML', 'quantidade': 9, 'subtotal': 243.00, 'mes': 'Março','semana':11},
    {'produto': 'PEROLA 300ML', 'quantidade': 1, 'subtotal': 27.00, 'mes': 'Março','semana':11},
    {'produto': 'CARMELA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Março','semana':11},
    {'produto': 'MALHADA 500ML', 'quantidade': 14, 'subtotal': 308.00, 'mes': 'Abril','semana':12},
    {'produto': 'MIMOSA 500ML', 'quantidade': 12, 'subtotal': 264.00, 'mes': 'Abril','semana':12},
    {'produto': 'PANDORA 500ML', 'quantidade': 69, 'subtotal': 1518.00, 'mes': 'Abril','semana':12},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':12},
    {'produto': 'FILO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Abril','semana':12},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':12},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'LOLITA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':12},
    {'produto': 'MANHOSA 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Abril','semana':12},
    {'produto': 'MISSY 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':12},
    {'produto': 'XONADA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':12},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':12},
    {'produto': 'BISA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Abril','semana':12},
    {'produto': 'MINEIRA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'PRETA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':12},
    {'produto': 'BOLINHA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':12},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':12},
    {'produto': 'BRANCA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':12},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':12},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Abril','semana':12},
    {'produto': 'RUBI 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Abril','semana':12},
    {'produto': 'CACAU 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'DIVA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':12},
    {'produto': 'DOMINO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':12},
    {'produto': 'DORI 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':12},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 25, 'subtotal': 550.00, 'mes': 'Abril','semana':12},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':12},
    {'produto': 'PODEROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':12},
    {'produto': 'ESTRELA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Abril','semana':12},
    {'produto': 'CARMELA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':12},
    {'produto': 'BISA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'PINTADINHA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'FILO 500ml TIME', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':12},
    {'produto': 'PRETA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'CHEIROSA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'MALHADA 300ML', 'quantidade': 32, 'subtotal': 576.00, 'mes': 'Abril','semana':12},
    {'produto': 'MIMOSA 300ML', 'quantidade': 38, 'subtotal': 684.00, 'mes': 'Abril','semana':12},
    {'produto': 'PANDORA 300ML', 'quantidade': 115, 'subtotal': 2070.00, 'mes': 'Abril','semana':12},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':12},
    {'produto': 'FILO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':12},
    {'produto': 'AMERICANA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':12},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':12},
    {'produto': 'DENGOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':12},
    {'produto': 'EMILIA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':12},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Abril','semana':12},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'JUDITE 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'LOLITA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':12},
    {'produto': 'MANHOSA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Abril','semana':12},
    {'produto': 'MISSY 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':12},
    {'produto': 'XONADA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Abril','semana':12},
    {'produto': 'MOO 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':12},
    {'produto': 'BISA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'MINEIRA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':12},
    {'produto': 'PRETA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':12},
    {'produto': 'BOLINHA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Abril','semana':12},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 16, 'subtotal': 288.00, 'mes': 'Abril','semana':12},
    {'produto': 'BRANCA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':12},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 4, 'subtotal': 100.00, 'mes': 'Abril','semana':12},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 6, 'subtotal': 150.00, 'mes': 'Abril','semana':12},
    {'produto': 'RUBI 300ML', 'quantidade': 10, 'subtotal': 250.00, 'mes': 'Abril','semana':12},
    {'produto': 'GINA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Abril','semana':12},
    {'produto': 'CACAU 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Abril','semana':12},
    {'produto': 'DIVA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':12},
    {'produto': 'DOMINO 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':12},
    {'produto': 'DORI 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':12},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 41, 'subtotal': 738.00, 'mes': 'Abril','semana':12},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':12},
    {'produto': 'PODEROSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':12},
    {'produto': 'ESTRELA 300ML', 'quantidade': 7, 'subtotal': 189.00, 'mes': 'Abril','semana':12},
    {'produto': 'CARMELA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':12},
    {'produto': 'MISSY 300ml TIME', 'quantidade': 1, 'subtotal': 14.00, 'mes': 'Abril','semana':12},
    {'produto': 'CHICLETIN 300ml TIME', 'quantidade': 1, 'subtotal': 14.00, 'mes': 'Abril','semana':12},
    {'produto': 'PRETA 300ml TIME', 'quantidade': 2, 'subtotal': 28.00, 'mes': 'Abril','semana':12},
    {'produto': 'CHEIROSA 300ml TIME', 'quantidade': 1, 'subtotal': 14.00, 'mes': 'Abril','semana':12},
    {'produto': 'MALHADA 500ML', 'quantidade': 16, 'subtotal': 352.00, 'mes': 'Abril','semana':13},
    {'produto': 'MIMOSA 500ML', 'quantidade': 21, 'subtotal': 462.00, 'mes': 'Abril','semana':13},
    {'produto': 'PANDORA 500ML', 'quantidade': 62, 'subtotal': 1364.00, 'mes': 'Abril','semana':13},
    {'produto': 'FILO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':13},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Abril','semana':13},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':13},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'LOLITA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':13},
    {'produto': 'MANHOSA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Abril','semana':13},
    {'produto': 'MISSY 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Abril','semana':13},
    {'produto': 'XONADA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':13},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':13},
    {'produto': 'MINEIRA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'BRANCA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':13},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':13},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Abril','semana':13},
    {'produto': 'RUBI 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':13},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':13},
    {'produto': 'CACAU 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'DIVA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':13},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':13},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 24, 'subtotal': 528.00, 'mes': 'Abril','semana':13},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':13},
    {'produto': 'PODEROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':13},
    {'produto': 'ESTRELA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Abril','semana':13},
    {'produto': 'CARMELA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':13},
    {'produto': 'BISA 500ml TIME', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':13},
    {'produto': 'BRANCA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':13},
    {'produto': 'FILO 500ml TIME', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':13},
    {'produto': 'PRETA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':13},
    {'produto': 'MALHADA 300ML', 'quantidade': 42, 'subtotal': 756.00, 'mes': 'Abril','semana':13},
    {'produto': 'MIMOSA 300ML', 'quantidade': 42, 'subtotal': 756.00, 'mes': 'Abril','semana':13},
    {'produto': 'PANDORA 300ML', 'quantidade': 95, 'subtotal': 1710.00, 'mes': 'Abril','semana':13},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':13},
    {'produto': 'FILO 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':13},
    {'produto': 'AMERICANA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':13},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':13},
    {'produto': 'DENGOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':13},
    {'produto': 'EMILIA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':13},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Abril','semana':13},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Abril','semana':13},
    {'produto': 'JUDITE 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':13},
    {'produto': 'LOLITA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Abril','semana':13},
    {'produto': 'MANHOSA 300ML', 'quantidade': 23, 'subtotal': 414.00, 'mes': 'Abril','semana':13},
    {'produto': 'MISSY 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':13},
    {'produto': 'XONADA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Abril','semana':13},
    {'produto': 'MOO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':13},
    {'produto': 'BISA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':13},
    {'produto': 'PRETA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':13},
    {'produto': 'BOLINHA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Abril','semana':13},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':13},
    {'produto': 'BRANCA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':13},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Abril','semana':13},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Abril','semana':13},
    {'produto': 'RUBI 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Abril','semana':13},
    {'produto': 'GINA 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Abril','semana':13},
    {'produto': 'CACAU 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':13},
    {'produto': 'DIVA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':13},
    {'produto': 'DORI 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':13},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':13},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 38, 'subtotal': 684.00, 'mes': 'Abril','semana':13},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Abril','semana':13},
    {'produto': 'PODEROSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':13},
    {'produto': 'ESTRELA 300ML', 'quantidade': 1, 'subtotal': 27.00, 'mes': 'Abril','semana':13},
    {'produto': 'CARMELA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':13},
    {'produto': 'CHICLETIN 300ml TIME', 'quantidade': 2, 'subtotal': 28.00, 'mes': 'Abril','semana':13},
    {'produto': 'MALHADA 500ML', 'quantidade': 25, 'subtotal': 550.00, 'mes': 'Abril','semana':14},
    {'produto': 'MIMOSA 500ML', 'quantidade': 18, 'subtotal': 396.00, 'mes': 'Abril','semana':14},
    {'produto': 'PANDORA 500ML', 'quantidade': 56, 'subtotal': 1232.00, 'mes': 'Abril','semana':14},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':14},
    {'produto': 'AMERICANA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'DENGOSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':14},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Abril','semana':14},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'JUDITE 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'LOLITA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':14},
    {'produto': 'MANHOSA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Abril','semana':14},
    {'produto': 'MISSY 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':14},
    {'produto': 'XONADA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Abril','semana':14},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'BISA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':14},
    {'produto': 'MINEIRA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'PRETA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':14},
    {'produto': 'BRANCA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':14},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Abril','semana':14},
    {'produto': 'RUBI 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':14},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':14},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':14},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 26, 'subtotal': 572.00, 'mes': 'Abril','semana':14},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Abril','semana':14},
    {'produto': 'PODEROSA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Abril','semana':14},
    {'produto': 'CARMELA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':14},
    {'produto': 'MISSY 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':14},
    {'produto': 'LOLITA 500ml TIME', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':14},
    {'produto': 'PINTADINHA 500ml TIME', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':14},
    {'produto': 'FILO 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':14},
    {'produto': 'CHICLETIN 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':14},
    {'produto': 'CHEIROSA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':14},
    {'produto': 'MALHADA 300ML', 'quantidade': 45, 'subtotal': 810.00, 'mes': 'Abril','semana':14},
    {'produto': 'MIMOSA 300ML', 'quantidade': 49, 'subtotal': 882.00, 'mes': 'Abril','semana':14},
    {'produto': 'PANDORA 300ML', 'quantidade': 117, 'subtotal': 2106.00, 'mes': 'Abril','semana':14},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Abril','semana':14},
    {'produto': 'FILO 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Abril','semana':14},
    {'produto': 'AMERICANA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Abril','semana':14},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':14},
    {'produto': 'EMILIA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':14},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Abril','semana':14},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Abril','semana':14},
    {'produto': 'JUDITE 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':14},
    {'produto': 'LOLITA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Abril','semana':14},
    {'produto': 'MANHOSA 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Abril','semana':14},
    {'produto': 'MISSY 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':14},
    {'produto': 'XONADA 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Abril','semana':14},
    {'produto': 'MOO 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':14},
    {'produto': 'BISA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':14},
    {'produto': 'MINEIRA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':14},
    {'produto': 'PRETA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':14},
    {'produto': 'BOLINHA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':14},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Abril','semana':14},
    {'produto': 'BRANCA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':14},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Abril','semana':14},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Abril','semana':14},
    {'produto': 'RUBI 300ML', 'quantidade': 7, 'subtotal': 175.00, 'mes': 'Abril','semana':14},
    {'produto': 'GINA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Abril','semana':14},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':14},
    {'produto': 'DIVA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Abril','semana':14},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':14},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 40, 'subtotal': 720.00, 'mes': 'Abril','semana':14},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':14},
    {'produto': 'PODEROSA 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Abril','semana':14},
    {'produto': 'ESTRELA 300ML', 'quantidade': 1, 'subtotal': 27.00, 'mes': 'Abril','semana':14},
    {'produto': 'CARMELA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':14},
    {'produto': 'CHEIROSA 300ml TIME', 'quantidade': 3, 'subtotal': 42.00, 'mes': 'Abril','semana':14},
    {'produto': 'MALHADA 500ML', 'quantidade': 15, 'subtotal': 330.00, 'mes': 'Abril','semana':15},
    {'produto': 'MIMOSA 500ML', 'quantidade': 28, 'subtotal': 616.00, 'mes': 'Abril','semana':15},
    {'produto': 'PANDORA 500ML', 'quantidade': 49, 'subtotal': 1078.00, 'mes': 'Abril','semana':15},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':15},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'EMILIA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':15},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':15},
    {'produto': 'JUDITE 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':15},
    {'produto': 'MANHOSA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Abril','semana':15},
    {'produto': 'MISSY 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'XONADA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':15},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':15},
    {'produto': 'BISA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Abril','semana':15},
    {'produto': 'MINEIRA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':15},
    {'produto': 'PRETA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':15},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Abril','semana':15},
    {'produto': 'RUBI 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':15},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Abril','semana':15},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Abril','semana':15},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 14, 'subtotal': 308.00, 'mes': 'Abril','semana':15},
    {'produto': 'PODEROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Abril','semana':15},
    {'produto': 'ESTRELA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Abril','semana':15},
    {'produto': 'CARMELA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Abril','semana':15},
    {'produto': 'PINTADINHA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':15},
    {'produto': 'FILO 500ml TIME', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':15},
    {'produto': 'PRETA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':15},
    {'produto': 'CHEIROSA 500ml TIME', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':15},
    {'produto': 'MALHADA 300ML', 'quantidade': 30, 'subtotal': 540.00, 'mes': 'Abril','semana':15},
    {'produto': 'MIMOSA 300ML', 'quantidade': 35, 'subtotal': 630.00, 'mes': 'Abril','semana':15},
    {'produto': 'PANDORA 300ML', 'quantidade': 89, 'subtotal': 1602.00, 'mes': 'Abril','semana':15},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':15},
    {'produto': 'FILO 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Abril','semana':15},
    {'produto': 'AMERICANA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':15},
    {'produto': 'DENGOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':15},
    {'produto': 'EMILIA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':15},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':15},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':15},
    {'produto': 'JUDITE 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':15},
    {'produto': 'LOLITA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':15},
    {'produto': 'MANHOSA 300ML', 'quantidade': 19, 'subtotal': 342.00, 'mes': 'Abril','semana':15},
    {'produto': 'MISSY 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':15},
    {'produto': 'XONADA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Abril','semana':15},
    {'produto': 'MOO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Abril','semana':15},
    {'produto': 'BISA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':15},
    {'produto': 'MINEIRA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':15},
    {'produto': 'PRETA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Abril','semana':15},
    {'produto': 'BOLINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':15},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Abril','semana':15},
    {'produto': 'BRANCA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':15},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Abril','semana':15},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 4, 'subtotal': 100.00, 'mes': 'Abril','semana':15},
    {'produto': 'RUBI 300ML', 'quantidade': 9, 'subtotal': 225.00, 'mes': 'Abril','semana':15},
    {'produto': 'DIVA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Abril','semana':15},
    {'produto': 'DOMINO 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':15},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Abril','semana':15},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 50, 'subtotal': 900.00, 'mes': 'Abril','semana':15},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Abril','semana':15},
    {'produto': 'PODEROSA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Abril','semana':15},
    {'produto': 'ESTRELA 300ML', 'quantidade': 4, 'subtotal': 108.00, 'mes': 'Abril','semana':15},
    {'produto': 'CARMELA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Abril','semana':15},
    {'produto': 'MISSY 300ml TIME', 'quantidade': 2, 'subtotal': 28.00, 'mes': 'Abril','semana':15},
    {'produto': 'CHICLETIN 300ml TIME', 'quantidade': 2, 'subtotal': 28.00, 'mes': 'Abril','semana':15},
    {'produto': 'MALHADA 500ML', 'quantidade': 13, 'subtotal': 286.00, 'mes': 'Maio','semana':16},
    {'produto': 'MIMOSA 500ML', 'quantidade': 25, 'subtotal': 550.00, 'mes': 'Maio','semana':16},
    {'produto': 'PANDORA 500ML', 'quantidade': 59, 'subtotal': 1298.00, 'mes': 'Maio','semana':16},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':16},
    {'produto': 'FILO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':16},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':16},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Maio','semana':16},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':16},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':16},
    {'produto': 'MANHOSA 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Maio','semana':16},
    {'produto': 'MISSY 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':16},
    {'produto': 'XONADA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':16},
    {'produto': 'MOO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':16},
    {'produto': 'BISA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':16},
    {'produto': 'MINEIRA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':16},
    {'produto': 'PRETA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':16},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':16},
    {'produto': 'BRANCA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':16},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Maio','semana':16},
    {'produto': 'RUBI 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Maio','semana':16},
    {'produto': 'CACAU 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':16},
    {'produto': 'DIVA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':16},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':16},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 40, 'subtotal': 880.00, 'mes': 'Maio','semana':16},
    {'produto': 'PODEROSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':16},
    {'produto': 'ESTRELA 500ML', 'quantidade': 7, 'subtotal': 224.00, 'mes': 'Maio','semana':16},
    {'produto': 'CARMELA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Maio','semana':16},
    {'produto': 'MALHADA 300ML', 'quantidade': 29, 'subtotal': 522.00, 'mes': 'Maio','semana':16},
    {'produto': 'MIMOSA 300ML', 'quantidade': 43, 'subtotal': 774.00, 'mes': 'Maio','semana':16},
    {'produto': 'PANDORA 300ML', 'quantidade': 119, 'subtotal': 2142.00, 'mes': 'Maio','semana':16},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':16},
    {'produto': 'FILO 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':16},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':16},
    {'produto': 'DENGOSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':16},
    {'produto': 'EMILIA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':16},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 18, 'subtotal': 324.00, 'mes': 'Maio','semana':16},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Maio','semana':16},
    {'produto': 'JUDITE 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':16},
    {'produto': 'LOLITA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':16},
    {'produto': 'MANHOSA 300ML', 'quantidade': 16, 'subtotal': 288.00, 'mes': 'Maio','semana':16},
    {'produto': 'MISSY 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Maio','semana':16},
    {'produto': 'XONADA 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Maio','semana':16},
    {'produto': 'MOO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':16},
    {'produto': 'BISA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':16},
    {'produto': 'MINEIRA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':16},
    {'produto': 'PRETA 300ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':16},
    {'produto': 'BOLINHA 300ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':16},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 13, 'subtotal': 234.00, 'mes': 'Maio','semana':16},
    {'produto': 'BRANCA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':16},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Maio','semana':16},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Maio','semana':16},
    {'produto': 'RUBI 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Maio','semana':16},
    {'produto': 'DIVA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':16},
    {'produto': 'DOMINO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':16},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':16},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 45, 'subtotal': 810.00, 'mes': 'Maio','semana':16},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':16},
    {'produto': 'PODEROSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':16},
    {'produto': 'ESTRELA 300ML', 'quantidade': 5, 'subtotal': 135.00, 'mes': 'Maio','semana':16},
    {'produto': 'CARMELA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':16},
    {'produto': 'MALHADA 500ML', 'quantidade': 31, 'subtotal': 682.00, 'mes': 'Maio','semana':17},
    {'produto': 'MIMOSA 500ML', 'quantidade': 25, 'subtotal': 550.00, 'mes': 'Maio','semana':17},
    {'produto': 'PANDORA 500ML', 'quantidade': 102, 'subtotal': 2244.00, 'mes': 'Maio','semana':17},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':17},
    {'produto': 'AMERICANA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':17},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'EMILIA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':17},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Maio','semana':17},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':17},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'LOLITA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':17},
    {'produto': 'MANHOSA 500ML', 'quantidade': 13, 'subtotal': 286.00, 'mes': 'Maio','semana':17},
    {'produto': 'MISSY 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':17},
    {'produto': 'XONADA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':17},
    {'produto': 'MOO 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Maio','semana':17},
    {'produto': 'BISA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':17},
    {'produto': 'MINEIRA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':17},
    {'produto': 'PRETA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Maio','semana':17},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'BRANCA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 5, 'subtotal': 175.00, 'mes': 'Maio','semana':17},
    {'produto': 'RUBI 500ML', 'quantidade': 3, 'subtotal': 105.00, 'mes': 'Maio','semana':17},
    {'produto': 'GINA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Maio','semana':17},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':17},
    {'produto': 'DORI 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':17},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 52, 'subtotal': 1144.00, 'mes': 'Maio','semana':17},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':17},
    {'produto': 'PODEROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':17},
    {'produto': 'ESTRELA 500ML', 'quantidade': 5, 'subtotal': 160.00, 'mes': 'Maio','semana':17},
    {'produto': 'CARMELA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':17},
    {'produto': 'RAINHA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Maio','semana':17},
    {'produto': 'MALHADA 300ML', 'quantidade': 49, 'subtotal': 882.00, 'mes': 'Maio','semana':17},
    {'produto': 'MIMOSA 300ML', 'quantidade': 61, 'subtotal': 1098.00, 'mes': 'Maio','semana':17},
    {'produto': 'PANDORA 300ML', 'quantidade': 123, 'subtotal': 2214.00, 'mes': 'Maio','semana':17},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':17},
    {'produto': 'FILO 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Maio','semana':17},
    {'produto': 'AMERICANA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':17},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Maio','semana':17},
    {'produto': 'DENGOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':17},
    {'produto': 'EMILIA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':17},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Maio','semana':17},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':17},
    {'produto': 'JUDITE 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':17},
    {'produto': 'LOLITA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':17},
    {'produto': 'MANHOSA 300ML', 'quantidade': 32, 'subtotal': 576.00, 'mes': 'Maio','semana':17},
    {'produto': 'MISSY 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':17},
    {'produto': 'XONADA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':17},
    {'produto': 'MOO 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Maio','semana':17},
    {'produto': 'BISA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':17},
    {'produto': 'MINEIRA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':17},
    {'produto': 'PRETA 300ML', 'quantidade': 16, 'subtotal': 288.00, 'mes': 'Maio','semana':17},
    {'produto': 'BOLINHA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Maio','semana':17},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 16, 'subtotal': 288.00, 'mes': 'Maio','semana':17},
    {'produto': 'BRANCA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':17},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Maio','semana':17},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 11, 'subtotal': 275.00, 'mes': 'Maio','semana':17},
    {'produto': 'RUBI 300ML', 'quantidade': 4, 'subtotal': 100.00, 'mes': 'Maio','semana':17},
    {'produto': 'GINA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Maio','semana':17},
    {'produto': 'CACAU 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':17},
    {'produto': 'DIVA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':17},
    {'produto': 'DOMINO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':17},
    {'produto': 'DORI 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':17},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':17},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 59, 'subtotal': 1062.00, 'mes': 'Maio','semana':17},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':17},
    {'produto': 'PODEROSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':17},
    {'produto': 'ESTRELA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Maio','semana':17},
    {'produto': 'CARMELA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':17},
    {'produto': 'RAINHA 300ML', 'quantidade': 7, 'subtotal': 189.00, 'mes': 'Maio','semana':17},
    {'produto': 'MALHADA 500ML', 'quantidade': 16, 'subtotal': 352.00, 'mes': 'Maio','semana':18},
    {'produto': 'MIMOSA 500ML', 'quantidade': 22, 'subtotal': 484.00, 'mes': 'Maio','semana':18},
    {'produto': 'PANDORA 500ML', 'quantidade': 52, 'subtotal': 1144.00, 'mes': 'Maio','semana':18},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Maio','semana':18},
    {'produto': 'FILO 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':18},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':18},
    {'produto': 'EMILIA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Maio','semana':18},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':18},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'MANHOSA 500ML', 'quantidade': 14, 'subtotal': 308.00, 'mes': 'Maio','semana':18},
    {'produto': 'MISSY 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':18},
    {'produto': 'XONADA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':18},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':18},
    {'produto': 'BISA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Maio','semana':18},
    {'produto': 'MINEIRA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':18},
    {'produto': 'PRETA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'BRANCA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Maio','semana':18},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 4, 'subtotal': 140.00, 'mes': 'Maio','semana':18},
    {'produto': 'GINA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Maio','semana':18},
    {'produto': 'DIVA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':18},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 18, 'subtotal': 396.00, 'mes': 'Maio','semana':18},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':18},
    {'produto': 'PODEROSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':18},
    {'produto': 'ESTRELA 500ML', 'quantidade': 4, 'subtotal': 128.00, 'mes': 'Maio','semana':18},
    {'produto': 'CARMELA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':18},
    {'produto': 'RAINHA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Maio','semana':18},
    {'produto': 'MALHADA 300ML', 'quantidade': 33, 'subtotal': 594.00, 'mes': 'Maio','semana':18},
    {'produto': 'MIMOSA 300ML', 'quantidade': 45, 'subtotal': 810.00, 'mes': 'Maio','semana':18},
    {'produto': 'PANDORA 300ML', 'quantidade': 129, 'subtotal': 2322.00, 'mes': 'Maio','semana':18},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Maio','semana':18},
    {'produto': 'FILO 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':18},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':18},
    {'produto': 'DENGOSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Maio','semana':18},
    {'produto': 'EMILIA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':18},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Maio','semana':18},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':18},
    {'produto': 'LOLITA 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Maio','semana':18},
    {'produto': 'MANHOSA 300ML', 'quantidade': 23, 'subtotal': 414.00, 'mes': 'Maio','semana':18},
    {'produto': 'MISSY 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Maio','semana':18},
    {'produto': 'XONADA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':18},
    {'produto': 'MOO 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':18},
    {'produto': 'BISA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':18},
    {'produto': 'MINEIRA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':18},
    {'produto': 'PRETA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Maio','semana':18},
    {'produto': 'BOLINHA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':18},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':18},
    {'produto': 'BRANCA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':18},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 2, 'subtotal': 50.00, 'mes': 'Maio','semana':18},
    {'produto': 'RUBI 300ML', 'quantidade': 6, 'subtotal': 150.00, 'mes': 'Maio','semana':18},
    {'produto': 'GINA 300ML', 'quantidade': 4, 'subtotal': 100.00, 'mes': 'Maio','semana':18},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':18},
    {'produto': 'DIVA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Maio','semana':18},
    {'produto': 'DOMINO 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':18},
    {'produto': 'DORI 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':18},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Maio','semana':18},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 39, 'subtotal': 702.00, 'mes': 'Maio','semana':18},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Maio','semana':18},
    {'produto': 'PODEROSA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Maio','semana':18},
    {'produto': 'ESTRELA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Maio','semana':18},
    {'produto': 'CARMELA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':18},
    {'produto': 'RAINHA 300ML', 'quantidade': 3, 'subtotal': 81.00, 'mes': 'Maio','semana':18},
    {'produto': 'MALHADA 500ML', 'quantidade': 31, 'subtotal': 682.00, 'mes': 'Maio','semana':19},
    {'produto': 'MIMOSA 500ML', 'quantidade': 36, 'subtotal': 792.00, 'mes': 'Maio','semana':19},
    {'produto': 'PANDORA 500ML', 'quantidade': 106, 'subtotal': 2332.00, 'mes': 'Maio','semana':19},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':19},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':19},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':19},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':19},
    {'produto': 'EMILIA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':19},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 16, 'subtotal': 352.00, 'mes': 'Maio','semana':19},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Maio','semana':19},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':19},
    {'produto': 'LOLITA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':19},
    {'produto': 'MANHOSA 500ML', 'quantidade': 12, 'subtotal': 264.00, 'mes': 'Maio','semana':19},
    {'produto': 'MISSY 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Maio','semana':19},
    {'produto': 'XONADA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':19},
    {'produto': 'MOO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':19},
    {'produto': 'BISA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Maio','semana':19},
    {'produto': 'MINEIRA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':19},
    {'produto': 'PRETA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Maio','semana':19},
    {'produto': 'BOLINHA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Maio','semana':19},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':19},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Maio','semana':19},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Maio','semana':19},
    {'produto': 'RUBI 500ML', 'quantidade': 6, 'subtotal': 210.00, 'mes': 'Maio','semana':19},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Maio','semana':19},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':19},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Maio','semana':19},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Maio','semana':19},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 48, 'subtotal': 1056.00, 'mes': 'Maio','semana':19},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Maio','semana':19},
    {'produto': 'PODEROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Maio','semana':19},
    {'produto': 'ESTRELA 500ML', 'quantidade': 7, 'subtotal': 224.00, 'mes': 'Maio','semana':19},
    {'produto': 'RAINHA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Maio','semana':19},
    {'produto': 'MALHADA 300ML', 'quantidade': 39, 'subtotal': 702.00, 'mes': 'Maio','semana':19},
    {'produto': 'MIMOSA 300ML', 'quantidade': 64, 'subtotal': 1152.00, 'mes': 'Maio','semana':19},
    {'produto': 'PANDORA 300ML', 'quantidade': 165, 'subtotal': 2970.00, 'mes': 'Maio','semana':19},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 17, 'subtotal': 306.00, 'mes': 'Maio','semana':19},
    {'produto': 'FILO 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':19},
    {'produto': 'AMERICANA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':19},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':19},
    {'produto': 'DENGOSA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':19},
    {'produto': 'EMILIA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':19},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Maio','semana':19},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Maio','semana':19},
    {'produto': 'JUDITE 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':19},
    {'produto': 'LOLITA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':19},
    {'produto': 'MANHOSA 300ML', 'quantidade': 25, 'subtotal': 450.00, 'mes': 'Maio','semana':19},
    {'produto': 'MISSY 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Maio','semana':19},
    {'produto': 'XONADA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':19},
    {'produto': 'MOO 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Maio','semana':19},
    {'produto': 'BISA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Maio','semana':19},
    {'produto': 'MINEIRA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Maio','semana':19},
    {'produto': 'PRETA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Maio','semana':19},
    {'produto': 'BOLINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':19},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 14, 'subtotal': 252.00, 'mes': 'Maio','semana':19},
    {'produto': 'BRANCA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':19},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Maio','semana':19},
    {'produto': 'RUBI 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Maio','semana':19},
    {'produto': 'GINA 300ML', 'quantidade': 1, 'subtotal': 25.00, 'mes': 'Maio','semana':19},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':19},
    {'produto': 'DIVA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Maio','semana':19},
    {'produto': 'DOMINO 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Maio','semana':19},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Maio','semana':19},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 56, 'subtotal': 1008.00, 'mes': 'Maio','semana':19},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Maio','semana':19},
    {'produto': 'PODEROSA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Maio','semana':19},
    {'produto': 'ESTRELA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Maio','semana':19},
    {'produto': 'RAINHA 300ML', 'quantidade': 7, 'subtotal': 189.00, 'mes': 'Maio','semana':19}, 
    {'produto': 'MALHADA 500ML', 'quantidade': 23, 'subtotal': 506.00, 'mes': 'Junho','semana':20},
    {'produto': 'MIMOSA 500ML', 'quantidade': 45, 'subtotal': 990.00, 'mes': 'Junho','semana':20},
    {'produto': 'PANDORA 500ML', 'quantidade': 110, 'subtotal': 2420.00, 'mes': 'Junho','semana':20},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':20},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':20},
    {'produto': 'AMERICANA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':20},
    {'produto': 'EMILIA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':20},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Junho','semana':20},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Junho','semana':20},
    {'produto': 'JUDITE 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':20},
    {'produto': 'MANHOSA 500ML', 'quantidade': 13, 'subtotal': 286.00, 'mes': 'Junho','semana':20},
    {'produto': 'MISSY 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':20},
    {'produto': 'XONADA 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Junho','semana':20},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':20},
    {'produto': 'BISA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Junho','semana':20},
    {'produto': 'MINEIRA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':20},
    {'produto': 'PRETA 500ML', 'quantidade': 9, 'subtotal': 198.00, 'mes': 'Junho','semana':20},
    {'produto': 'BOLINHA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':20},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':20},
    {'produto': 'BRANCA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':20},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Junho','semana':20},
    {'produto': 'RUBI 500ML', 'quantidade': 7, 'subtotal': 245.00, 'mes': 'Junho','semana':20},
    {'produto': 'GINA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Junho','semana':20},
    {'produto': 'CACAU 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':20},
    {'produto': 'DIVA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':20},
    {'produto': 'DOMINO 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':20},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':20},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 48, 'subtotal': 1056.00, 'mes': 'Junho','semana':20},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Junho','semana':20},
    {'produto': 'PODEROSA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Junho','semana':20},
    {'produto': 'ESTRELA 500ML', 'quantidade': 6, 'subtotal': 192.00, 'mes': 'Junho','semana':20},
    {'produto': 'RAINHA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Junho','semana':20},
    {'produto': 'MALHADA 300ML', 'quantidade': 41, 'subtotal': 738.00, 'mes': 'Junho','semana':20},
    {'produto': 'MIMOSA 300ML', 'quantidade': 73, 'subtotal': 1314.00, 'mes': 'Junho','semana':20},
    {'produto': 'PANDORA 300ML', 'quantidade': 172, 'subtotal': 3096.00, 'mes': 'Junho','semana':20},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Junho','semana':20},
    {'produto': 'FILO 300ML', 'quantidade': 11, 'subtotal': 198.00, 'mes': 'Junho','semana':20},
    {'produto': 'AMERICANA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':20},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':20},
    {'produto': 'DENGOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':20},
    {'produto': 'EMILIA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':20},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 26, 'subtotal': 468.00, 'mes': 'Junho','semana':20},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Junho','semana':20},
    {'produto': 'JUDITE 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':20},
    {'produto': 'LOLITA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Junho','semana':20},
    {'produto': 'MANHOSA 300ML', 'quantidade': 28, 'subtotal': 504.00, 'mes': 'Junho','semana':20},
    {'produto': 'MISSY 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Junho','semana':20},
    {'produto': 'XONADA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Junho','semana':20},
    {'produto': 'MOO 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Junho','semana':20},
    {'produto': 'BISA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Junho','semana':20},
    {'produto': 'MINEIRA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':20},
    {'produto': 'PRETA 300ML', 'quantidade': 16, 'subtotal': 288.00, 'mes': 'Junho','semana':20},
    {'produto': 'BOLINHA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':20},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 19, 'subtotal': 342.00, 'mes': 'Junho','semana':20},
    {'produto': 'BRANCA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':20},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 6, 'subtotal': 150.00, 'mes': 'Junho','semana':20},
    {'produto': 'RUBI 300ML', 'quantidade': 6, 'subtotal': 150.00, 'mes': 'Junho','semana':20},
    {'produto': 'GINA 300ML', 'quantidade': 3, 'subtotal': 75.00, 'mes': 'Junho','semana':20},
    {'produto': 'CACAU 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Junho','semana':20},
    {'produto': 'DIVA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Junho','semana':20},
    {'produto': 'DOMINO 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':20},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':20},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 53, 'subtotal': 954.00, 'mes': 'Junho','semana':20},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Junho','semana':20},
    {'produto': 'PODEROSA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Junho','semana':20},
    {'produto': 'ESTRELA 300ML', 'quantidade': 9, 'subtotal': 243.00, 'mes': 'Junho','semana':20},
    {'produto': 'CARMELA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':20},
    {'produto': 'RAINHA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Junho','semana':20},
    {'produto': 'MALHADA 500ML', 'quantidade': 17, 'subtotal': 408.00, 'mes': 'Junho','semana':21},
    {'produto': 'MIMOSA 500ML', 'quantidade': 23, 'subtotal': 552.00, 'mes': 'Junho','semana':21},
    {'produto': 'PANDORA 500ML', 'quantidade': 82, 'subtotal': 1968.00, 'mes': 'Junho','semana':21},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Junho','semana':21},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':21},
    {'produto': 'DENGOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':21},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 4, 'subtotal': 96.00, 'mes': 'Junho','semana':21},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':21},
    {'produto': 'JUDITE 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':21},
    {'produto': 'LOLITA 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':21},
    {'produto': 'MANHOSA 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Junho','semana':21},
    {'produto': 'MISSY 500ML', 'quantidade': 4, 'subtotal': 96.00, 'mes': 'Junho','semana':21},
    {'produto': 'XONADA 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':21},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':21},
    {'produto': 'BISA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':21},
    {'produto': 'MINEIRA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':21},
    {'produto': 'PRETA 500ML', 'quantidade': 8, 'subtotal': 176.00, 'mes': 'Junho','semana':21},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':21},
    {'produto': 'BRANCA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':21},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 1, 'subtotal': 35.00, 'mes': 'Junho','semana':21},
    {'produto': 'RUBI 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Junho','semana':21},
    {'produto': 'DIVA 500ML', 'quantidade': 7, 'subtotal': 154.00, 'mes': 'Junho','semana':21},
    {'produto': 'DOMINO 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':21},
    {'produto': 'DORI 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':21},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':21},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 18, 'subtotal': 432.00, 'mes': 'Junho','semana':21},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 10, 'subtotal': 240.00, 'mes': 'Junho','semana':21},
    {'produto': 'PODEROSA 500ML', 'quantidade': 4, 'subtotal': 96.00, 'mes': 'Junho','semana':21},
    {'produto': 'ESTRELA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Junho','semana':21},
    {'produto': 'PEROLA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Junho','semana':21},
    {'produto': 'RAINHA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Junho','semana':21},
    {'produto': 'MALHADA 300ML', 'quantidade': 25, 'subtotal': 500.00, 'mes': 'Junho','semana':21},
    {'produto': 'MIMOSA 300ML', 'quantidade': 48, 'subtotal': 960.00, 'mes': 'Junho','semana':21},
    {'produto': 'PANDORA 300ML', 'quantidade': 107, 'subtotal': 2140.00, 'mes': 'Junho','semana':21},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 24, 'subtotal': 432.00, 'mes': 'Junho','semana':21},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':21},
    {'produto': 'DENGOSA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':21},
    {'produto': 'EMILIA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Junho','semana':21},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 8, 'subtotal': 160.00, 'mes': 'Junho','semana':21},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':21},
    {'produto': 'JUDITE 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Junho','semana':21},
    {'produto': 'LOLITA 300ML', 'quantidade': 3, 'subtotal': 60.00, 'mes': 'Junho','semana':21},
    {'produto': 'MANHOSA 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Junho','semana':21},
    {'produto': 'XONADA 300ML', 'quantidade': 6, 'subtotal': 120.00, 'mes': 'Junho','semana':21},
    {'produto': 'MOO 300ML', 'quantidade': 3, 'subtotal': 60.00, 'mes': 'Junho','semana':21},
    {'produto': 'BISA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':21},
    {'produto': 'MINEIRA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':21},
    {'produto': 'PRETA 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Junho','semana':21},
    {'produto': 'BOLINHA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Junho','semana':21},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':21},
    {'produto': 'BRANCA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Junho','semana':21},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 4, 'subtotal': 108.00, 'mes': 'Junho','semana':21},
    {'produto': 'RUBI 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Junho','semana':21},
    {'produto': 'GINA 300ML', 'quantidade': 1, 'subtotal': 27.00, 'mes': 'Junho','semana':21},
    {'produto': 'CACAU 300ML', 'quantidade': 1, 'subtotal': 20.00, 'mes': 'Junho','semana':21},
    {'produto': 'DIVA 300ML', 'quantidade': 17, 'subtotal': 306.00, 'mes': 'Junho','semana':21},
    {'produto': 'DOMINO 300ML', 'quantidade': 4, 'subtotal': 80.00, 'mes': 'Junho','semana':21},
    {'produto': 'DORI 300ML', 'quantidade': 2, 'subtotal': 40.00, 'mes': 'Junho','semana':21},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 2, 'subtotal': 40.00, 'mes': 'Junho','semana':21},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 51, 'subtotal': 1020.00, 'mes': 'Junho','semana':21},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 6, 'subtotal': 120.00, 'mes': 'Junho','semana':21},
    {'produto': 'PODEROSA 300ML', 'quantidade': 4, 'subtotal': 80.00, 'mes': 'Junho','semana':21},
    {'produto': 'ESTRELA 300ML', 'quantidade': 11, 'subtotal': 297.00, 'mes': 'Junho','semana':21},
    {'produto': 'PEROLA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Junho','semana':21},
    {'produto': 'RAINHA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Junho','semana':21},
    {'produto': 'MALHADA 500ML', 'quantidade': 10, 'subtotal': 240.00, 'mes': 'Junho','semana':22},
    {'produto': 'MIMOSA 500ML', 'quantidade': 22, 'subtotal': 528.00, 'mes': 'Junho','semana':22},
    {'produto': 'PANDORA 500ML', 'quantidade': 83, 'subtotal': 1992.00, 'mes': 'Junho','semana':22},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Junho','semana':22},
    {'produto': 'FILO 500ML', 'quantidade': 4, 'subtotal': 96.00, 'mes': 'Junho','semana':22},
    {'produto': 'CHEIROSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':22},
    {'produto': 'DENGOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':22},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':22},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':22},
    {'produto': 'JUDITE 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':22},
    {'produto': 'MANHOSA 500ML', 'quantidade': 10, 'subtotal': 220.00, 'mes': 'Junho','semana':22},
    {'produto': 'MISSY 500ML', 'quantidade': 3, 'subtotal': 72.00, 'mes': 'Junho','semana':22},
    {'produto': 'XONADA 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':22},
    {'produto': 'MOO 500ML', 'quantidade': 5, 'subtotal': 120.00, 'mes': 'Junho','semana':22},
    {'produto': 'BISA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':22},
    {'produto': 'MINEIRA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Junho','semana':22},
    {'produto': 'PRETA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':22},
    {'produto': 'BOLINHA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':22},
    {'produto': 'CHICLETIN 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':22},
    {'produto': 'BRANCA 500ML', 'quantidade': 6, 'subtotal': 132.00, 'mes': 'Junho','semana':22},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 1, 'subtotal': 30.00, 'mes': 'Junho','semana':22},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Junho','semana':22},
    {'produto': 'RUBI 500ML', 'quantidade': 3, 'subtotal': 105.00, 'mes': 'Junho','semana':22},
    {'produto': 'DIVA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':22},
    {'produto': 'DOMINO 500ML', 'quantidade': 5, 'subtotal': 120.00, 'mes': 'Junho','semana':22},
    {'produto': 'DORI 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':22},
    {'produto': 'HOLANDESA 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':22},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 37, 'subtotal': 888.00, 'mes': 'Junho','semana':22},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 6, 'subtotal': 144.00, 'mes': 'Junho','semana':22},
    {'produto': 'PODEROSA 500ML', 'quantidade': 3, 'subtotal': 72.00, 'mes': 'Junho','semana':22},
    {'produto': 'ESTRELA 500ML', 'quantidade': 2, 'subtotal': 64.00, 'mes': 'Junho','semana':22},
    {'produto': 'PEROLA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Junho','semana':22},
    {'produto': 'CARMELA 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':22},
    {'produto': 'MALHADA 300ML', 'quantidade': 19, 'subtotal': 380.00, 'mes': 'Junho','semana':22},
    {'produto': 'MIMOSA 300ML', 'quantidade': 21, 'subtotal': 420.00, 'mes': 'Junho','semana':22},
    {'produto': 'PANDORA 300ML', 'quantidade': 69, 'subtotal': 1380.00, 'mes': 'Junho','semana':22},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 21, 'subtotal': 378.00, 'mes': 'Junho','semana':22},
    {'produto': 'FILO 300ML', 'quantidade': 2, 'subtotal': 40.00, 'mes': 'Junho','semana':22},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':22},
    {'produto': 'DENGOSA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':22},
    {'produto': 'EMILIA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Junho','semana':22},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 7, 'subtotal': 140.00, 'mes': 'Junho','semana':22},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 9, 'subtotal': 162.00, 'mes': 'Junho','semana':22},
    {'produto': 'JUDITE 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':22},
    {'produto': 'LOLITA 300ML', 'quantidade': 2, 'subtotal': 40.00, 'mes': 'Junho','semana':22},
    {'produto': 'MANHOSA 300ML', 'quantidade': 19, 'subtotal': 342.00, 'mes': 'Junho','semana':22},
    {'produto': 'MISSY 300ML', 'quantidade': 2, 'subtotal': 40.00, 'mes': 'Junho','semana':22},
    {'produto': 'XONADA 300ML', 'quantidade': 9, 'subtotal': 180.00, 'mes': 'Junho','semana':22},
    {'produto': 'MOO 300ML', 'quantidade': 5, 'subtotal': 100.00, 'mes': 'Junho','semana':22},
    {'produto': 'BISA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Junho','semana':22},
    {'produto': 'MINEIRA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':22},
    {'produto': 'PRETA 300ML', 'quantidade': 7, 'subtotal': 126.00, 'mes': 'Junho','semana':22},
    {'produto': 'BOLINHA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':22},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 12, 'subtotal': 216.00, 'mes': 'Junho','semana':22},
    {'produto': 'BRANCA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':22},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Junho','semana':22},
    {'produto': 'RUBI 300ML', 'quantidade': 4, 'subtotal': 108.00, 'mes': 'Junho','semana':22},
    {'produto': 'CACAU 300ML', 'quantidade': 2, 'subtotal': 40.00, 'mes': 'Junho','semana':22},
    {'produto': 'DIVA 300ML', 'quantidade': 23, 'subtotal': 414.00, 'mes': 'Junho','semana':22},
    {'produto': 'DOMINO 300ML', 'quantidade': 4, 'subtotal': 80.00, 'mes': 'Junho','semana':22},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 3, 'subtotal': 60.00, 'mes': 'Junho','semana':22},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 60, 'subtotal': 1200.00, 'mes': 'Junho','semana':22},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 14, 'subtotal': 280.00, 'mes': 'Junho','semana':22},
    {'produto': 'PODEROSA 300ML', 'quantidade': 4, 'subtotal': 80.00, 'mes': 'Junho','semana':22},
    {'produto': 'ESTRELA 300ML', 'quantidade': 8, 'subtotal': 216.00, 'mes': 'Junho','semana':22},
    {'produto': 'PEROLA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Junho','semana':22},
    {'produto': 'CARMELA 300ML', 'quantidade': 5, 'subtotal': 100.00, 'mes': 'Junho','semana':22},
    {'produto': 'RAINHA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Junho','semana':22},
    {'produto': 'MALHADA 500ML', 'quantidade': 10, 'subtotal': 240.00, 'mes': 'Junho','semana':23},
    {'produto': 'MIMOSA 500ML', 'quantidade': 24, 'subtotal': 576.00, 'mes': 'Junho','semana':23},
    {'produto': 'PANDORA 500ML', 'quantidade': 87, 'subtotal': 2088.00, 'mes': 'Junho','semana':23},
    {'produto': 'PINTADINHA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':23},
    {'produto': 'FILO 500ML', 'quantidade': 3, 'subtotal': 72.00, 'mes': 'Junho','semana':23},
    {'produto': 'DENGOSA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':23},
    {'produto': 'FLOCOS DE NEVE 500ML', 'quantidade': 3, 'subtotal': 72.00, 'mes': 'Junho','semana':23},
    {'produto': 'GRACIOSA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':23},
    {'produto': 'JUDITE 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':23},
    {'produto': 'LOLITA 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':23},
    {'produto': 'MANHOSA 500ML', 'quantidade': 4, 'subtotal': 88.00, 'mes': 'Junho','semana':23},
    {'produto': 'MISSY 500ML', 'quantidade': 4, 'subtotal': 96.00, 'mes': 'Junho','semana':23},
    {'produto': 'XONADA 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':23},
    {'produto': 'MOO 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':23},
    {'produto': 'BISA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':23},
    {'produto': 'MINEIRA 500ML', 'quantidade': 2, 'subtotal': 44.00, 'mes': 'Junho','semana':23},
    {'produto': 'PRETA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':23},
    {'produto': 'BOLINHA 500ML', 'quantidade': 3, 'subtotal': 66.00, 'mes': 'Junho','semana':23},
    {'produto': 'BRANCA 500ML', 'quantidade': 1, 'subtotal': 22.00, 'mes': 'Junho','semana':23},
    {'produto': 'ESMERALDA 500ML', 'quantidade': 2, 'subtotal': 60.00, 'mes': 'Junho','semana':23},
    {'produto': 'JOIA RARA 500ML', 'quantidade': 2, 'subtotal': 70.00, 'mes': 'Junho','semana':23},
    {'produto': 'CACAU 500ML', 'quantidade': 1, 'subtotal': 24.00, 'mes': 'Junho','semana':23},
    {'produto': 'DIVA 500ML', 'quantidade': 5, 'subtotal': 110.00, 'mes': 'Junho','semana':23},
    {'produto': 'DOMINO 500ML', 'quantidade': 4, 'subtotal': 96.00, 'mes': 'Junho','semana':23},
    {'produto': 'DORI 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':23},
    {'produto': 'PRECIOSA 500ML', 'quantidade': 30, 'subtotal': 720.00, 'mes': 'Junho','semana':23},
    {'produto': 'TEMPESTADE 500ML', 'quantidade': 5, 'subtotal': 120.00, 'mes': 'Junho','semana':23},
    {'produto': 'PODEROSA 500ML', 'quantidade': 4, 'subtotal': 96.00, 'mes': 'Junho','semana':23},
    {'produto': 'ESTRELA 500ML', 'quantidade': 1, 'subtotal': 32.00, 'mes': 'Junho','semana':23},
    {'produto': 'CARMELA 500ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':23},
    {'produto': 'RAINHA 500ML', 'quantidade': 3, 'subtotal': 96.00, 'mes': 'Junho','semana':23},
    {'produto': 'MALHADA 300ML', 'quantidade': 21, 'subtotal': 420.00, 'mes': 'Junho','semana':23},
    {'produto': 'MIMOSA 300ML', 'quantidade': 40, 'subtotal': 800.00, 'mes': 'Junho','semana':23},
    {'produto': 'PANDORA 300ML', 'quantidade': 122, 'subtotal': 2440.00, 'mes': 'Junho','semana':23},
    {'produto': 'PINTADINHA 300ML', 'quantidade': 10, 'subtotal': 180.00, 'mes': 'Junho','semana':23},
    {'produto': 'FILO 300ML', 'quantidade': 2, 'subtotal': 40.00, 'mes': 'Junho','semana':23},
    {'produto': 'CHEIROSA 300ML', 'quantidade': 1, 'subtotal': 18.00, 'mes': 'Junho','semana':23},
    {'produto': 'DENGOSA 300ML', 'quantidade': 5, 'subtotal': 90.00, 'mes': 'Junho','semana':23},
    {'produto': 'EMILIA 300ML', 'quantidade': 2, 'subtotal': 36.00, 'mes': 'Junho','semana':23},
    {'produto': 'FLOCOS DE NEVE 300ML', 'quantidade': 8, 'subtotal': 160.00, 'mes': 'Junho','semana':23},
    {'produto': 'GRACIOSA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':23},
    {'produto': 'JUDITE 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':23},
    {'produto': 'LOLITA 300ML', 'quantidade': 3, 'subtotal': 60.00, 'mes': 'Junho','semana':23},
    {'produto': 'MANHOSA 300ML', 'quantidade': 16, 'subtotal': 288.00, 'mes': 'Junho','semana':23},
    {'produto': 'MISSY 300ML', 'quantidade': 5, 'subtotal': 100.00, 'mes': 'Junho','semana':23},
    {'produto': 'XONADA 300ML', 'quantidade': 4, 'subtotal': 80.00, 'mes': 'Junho','semana':23},
    {'produto': 'MOO 300ML', 'quantidade': 1, 'subtotal': 20.00, 'mes': 'Junho','semana':23},
    {'produto': 'BISA 300ML', 'quantidade': 3, 'subtotal': 54.00, 'mes': 'Junho','semana':23},
    {'produto': 'MINEIRA 300ML', 'quantidade': 6, 'subtotal': 108.00, 'mes': 'Junho','semana':23},
    {'produto': 'PRETA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Junho','semana':23},
    {'produto': 'BOLINHA 300ML', 'quantidade': 4, 'subtotal': 72.00, 'mes': 'Junho','semana':23},
    {'produto': 'CHICLETIN 300ML', 'quantidade': 15, 'subtotal': 270.00, 'mes': 'Junho','semana':23},
    {'produto': 'BRANCA 300ML', 'quantidade': 8, 'subtotal': 144.00, 'mes': 'Junho','semana':23},
    {'produto': 'ESMERALDA 300ML', 'quantidade': 2, 'subtotal': 48.00, 'mes': 'Junho','semana':23},
    {'produto': 'JOIA RARA 300ML', 'quantidade': 7, 'subtotal': 189.00, 'mes': 'Junho','semana':23},
    {'produto': 'RUBI 300ML', 'quantidade': 5, 'subtotal': 135.00, 'mes': 'Junho','semana':23},
    {'produto': 'CACAU 300ML', 'quantidade': 1, 'subtotal': 20.00, 'mes': 'Junho','semana':23},
    {'produto': 'DIVA 300ML', 'quantidade': 22, 'subtotal': 396.00, 'mes': 'Junho','semana':23},
    {'produto': 'DOMINO 300ML', 'quantidade': 3, 'subtotal': 60.00, 'mes': 'Junho','semana':23},
    {'produto': 'DORI 300ML', 'quantidade': 4, 'subtotal': 80.00, 'mes': 'Junho','semana':23},
    {'produto': 'HOLANDESA 300ML', 'quantidade': 3, 'subtotal': 60.00, 'mes': 'Junho','semana':23},
    {'produto': 'PRECIOSA 300ML', 'quantidade': 40, 'subtotal': 800.00, 'mes': 'Junho','semana':23},
    {'produto': 'TEMPESTADE 300ML', 'quantidade': 11, 'subtotal': 220.00, 'mes': 'Junho','semana':23},
    {'produto': 'PODEROSA 300ML', 'quantidade': 7, 'subtotal': 140.00, 'mes': 'Junho','semana':23},
    {'produto': 'ESTRELA 300ML', 'quantidade': 6, 'subtotal': 162.00, 'mes': 'Junho','semana':23},
    {'produto': 'PEROLA 300ML', 'quantidade': 2, 'subtotal': 54.00, 'mes': 'Junho','semana':23},
    {'produto': 'CARMELA 300ML', 'quantidade': 6, 'subtotal': 120.00, 'mes': 'Junho','semana':23},
    {'produto': 'RAINHA 300ML', 'quantidade': 1, 'subtotal': 27.00, 'mes': 'Junho','semana':23},]


# **MANIPULAÇÃO DOS DADOS**

# Criamos um dataframe para podermos manipularmos melhor os dados relacionados a quantidade de pedidos, o subtotal e o mês em que ocorreu a demanda

# In[39]:


df = pd.DataFrame(dados)


# In[40]:


df


# In[45]:


soma_Pandora_300ml = df[df['produto'] =='PANDORA 300ML']['subtotal'].sum()
soma_Pandora_300ml


# In[47]:


soma_Pandora_500ml = df[df['produto'] =='PANDORA 500ML']['subtotal'].sum()
soma_Pandora_500ml


# In[48]:


soma_Preciosa_300ml = df[df['produto'] =='PRECIOSA 300ML']['subtotal'].sum()
soma_Preciosa_300ml


# In[49]:


soma_Mimosa_300ml = df[df['produto'] =='MIMOSA 300ML']['subtotal'].sum()
soma_Mimosa_300ml


# In[50]:


soma_Malhada_300ml = df[df['produto'] =='MALHADA 300ML']['subtotal'].sum()
soma_Malhada_300ml


# Agrupar dados por mês e produto para calcular a quantidade total vendida de cada produto por mês

# In[6]:


df_agrupado = df.groupby(['mes','produto'])['quantidade'].sum().reset_index()
df_agrupado


# Ordenando por mês e quantidade vendida em ordem descrescente

# In[7]:


# Ordenando por mês e quantidade vendida em ordem decrescente
df_agrupado = df_agrupado.sort_values(by=['mes', 'quantidade'], ascending=[True, False])


# In[8]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[9]:


df_agrupado['Percentual Acumulado'] = df_agrupado.groupby('mes')['quantidade'].cumsum() / df_agrupado.groupby('mes')['quantidade'].transform('sum') * 100


# Ordenamos o DataFrame pelo Percentual Acumulado

# In[10]:


df_ordenado = df_agrupado.sort_values(by='Percentual Acumulado')


# **IDENTIFICAÇÃO DO MIX DE PRODUTOS COM MAIOR VALOR AGREGADO DA EMPRESA**

# In[11]:


df_unico = df_ordenado.drop_duplicates(subset='produto')
df_unico.head()


# Definindo função para categorizar os produtos A, B ou C de acordo com os percentuais acumulados

# In[12]:


def categorizar_ABC(percentual_acumulado):
    if percentual_acumulado <= 80:
        return 'A'
    elif percentual_acumulado <= 95:
        return 'B'
    else:
        return 'C'


# In[13]:


pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')


# **Ordenar o dataframe por mês e percentual de acordo com cada categoria para melhor visualização da Curva ABC**

# In[14]:


df_agrupado['Categoria ABC'] = df_agrupado['Percentual Acumulado'].apply(categorizar_ABC)
df_agrupado.head()


# In[15]:


maior_valor = df_unico['quantidade'].max()
maior_valor


# **Gráfico de Curva ABC por Mês**

# A análise ABC permite que os gerentes se concentrem nos itens mais importantes (Categoria A), assegurando que esses itens estejam sempre disponíveis, e otimizem os recursos e esforços em relação aos itens menos críticos (Categoria B e C).

# In[15]:


# Gráfico de curvas ABC por mês ordenado
plt.figure(figsize=(14, 10))
cores = {'A': 'green', 'B': 'blue', 'C': 'orange'}
marcadores = {'A': 'o', 'B': 's', 'C': 'D'}

for mes in df_agrupado['mes'].unique():
    df_mes = df_agrupado[df_agrupado['mes'] == mes]
    for categoria in ['A', 'B', 'C']:
        dados_categoria = df_mes[df_mes['Categoria ABC'] == categoria]
        plt.scatter(dados_categoria['produto'], dados_categoria['Percentual Acumulado'], 
                    color=cores[categoria], label=f'{mes} - Categoria {categoria}', 
                    marker=marcadores[categoria], s=100)

plt.title('Curva ABC dos Milkshakes Mais Vendidos por Mês')
plt.xlabel('Produto')
plt.ylabel('Percentual Acumulado (%)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[16]:


# Filtrando apenas os produtos classificados como 'A' (os mais vendidos) em cada mês
produtos_categoria_A = df_agrupado[df_agrupado['Categoria ABC'] == 'A']


# In[17]:


# Ordenar o DataFrame pelo Percentual Acumulado
produtos_categoria_A = produtos_categoria_A.sort_values(by='Percentual Acumulado')


# In[18]:


maior_valor = produtos_categoria_A['quantidade'].max()
maior_valor


# Identificar o produto de maior valor de quantidade

# In[19]:


# Ordenar o DataFrame df_agrupado pelo maior valor de quantidade ao menor
df_agrupado_ordenado = df_agrupado.sort_values(by='quantidade', ascending=False)

df_agrupado_ordenado


# Ordenar os produtos da categoria A por quantidade vendida em cada mês, do maior ao menor

# In[20]:


# Ordenando os produtos da categoria A por quantidade vendida em cada mês
produtos_categoria_A_ordenados = produtos_categoria_A.sort_values(by=['mes', 'quantidade'], ascending=[True, False])


# In[21]:


# Filtrar apenas os produtos classificados como 'A' (os mais vendidos) em cada mês
top_milkshakes_A_por_mes = df_agrupado[df_agrupado['Categoria ABC'] == 'A']

# Ordenar os produtos da categoria A por quantidade vendida em cada mês, do maior ao menor
top_milkshakes_A_ordenado = top_milkshakes_A_por_mes.sort_values(by=['mes', 'quantidade'], ascending=[True, False])


# **Quantidade de Milkshake vendidos por mês**

# In[23]:


# Exemplo de como plotar um gráfico de barras para visualizar as quantidades por mês
plt.figure(figsize=(10, 6))
df.groupby(['mes'])['quantidade'].sum().plot(kind='bar', color='skyblue')
plt.title('Quantidade de Milkshakes Vendidos por Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[22]:


# Agrupando por mês para calcular a quantidade total vendida em cada mês
df_meses = df.groupby('mes')['quantidade'].sum().reset_index()

# Ordenando os meses pela quantidade total vendida em ordem decrescente
df_meses_ordenado = df_meses.sort_values(by='quantidade', ascending=False)

print("Meses que mais venderam:")
df_meses_ordenado


# **Análises e Resultados**

# Ao analisarmos o gráfico da curva ABC, identificamos que o produto "PANDORA 500ML" e "PANDORA 300ML", 'PRECIOSA 300ML","MIMOSA 300ML" e "MALHADA 300ML" são os de maiores quantidades de demanda ao longo dos meses, sendo os menores percentuais acumulados da curva, demonstrando maior valor. Utilizaremos destes produtos core, para realizar a nossa Gestão de Estoque.

# # PREVISÃO DE DEMANDA UTILIZANDO SÉRIE TEMPORAL A PARTIR DOS DADOS DE DEMANDA

# In[23]:


produtos_desejados = ['PANDORA 500ML', 'PANDORA 300ML', 'PRECIOSA 300ML', 'MIMOSA 300ML', 'MALHADA 300ML']
print(produtos_desejados)


# In[24]:


df_filtrado = df[df['produto'].isin(produtos_desejados)]
df_filtrado


# In[25]:


df_agrupado = df_filtrado.groupby(['mes','produto'])['quantidade'].sum().reset_index()
df_agrupado


# In[26]:


def converter_mes_para_data(mes_str, ano_atual):
    meses = {
        'Janeiro': '01',
        'Fevereiro': '02',
        'Março': '03',
        'Abril': '04',
        'Maio': '05',
        'Junho': '06',
        'Julho': '07',
        'Agosto': '08',
        'Setembro': '09',
        'Outubro': '10',
        'Novembro': '11',
        'Dezembro': '12'
    }
    
    if mes_str in meses:
        return f"{meses[mes_str]}-{ano_atual}"
    else:
        raise ValueError(f"Nome do mês inválido: {mes_str}")

# Função para aplicar a conversão de meses em um DataFrame
def aplicar_converter_mes(df, coluna_mes, ano_atual):
    df[coluna_mes] = df[coluna_mes].apply(lambda mes: converter_mes_para_data(mes, ano_atual))
    return df

# Dados de vendas mensais dos milkshakes
data_vendas = {
    'Mes': ['Abril', 'Abril', 'Abril', 'Abril', 'Abril', 'Fevereiro', 'Fevereiro', 'Fevereiro', 'Fevereiro', 'Fevereiro',
            'Janeiro', 'Janeiro', 'Janeiro', 'Janeiro', 'Janeiro', 'Junho', 'Junho', 'Junho', 'Junho', 'Junho',
            'Maio', 'Maio', 'Maio', 'Maio', 'Maio', 'Março', 'Março', 'Março', 'Março', 'Março'],
    'Milkshake': ['MALHADA 300ML', 'MIMOSA 300ML', 'PANDORA 300ML', 'PANDORA 500ML', 'PRECIOSA 300ML',
                  'MALHADA 300ML', 'MIMOSA 300ML', 'PANDORA 300ML', 'PANDORA 500ML', 'PRECIOSA 300ML',
                  'MALHADA 300ML', 'MIMOSA 300ML', 'PANDORA 300ML', 'PANDORA 500ML', 'PRECIOSA 300ML',
                  'MALHADA 300ML', 'MIMOSA 300ML', 'PANDORA 300ML', 'PANDORA 500ML', 'PRECIOSA 300ML',
                  'MALHADA 300ML', 'MIMOSA 300ML', 'PANDORA 300ML', 'PANDORA 500ML', 'PRECIOSA 300ML',
                  'MALHADA 300ML', 'MIMOSA 300ML', 'PANDORA 300ML', 'PANDORA 500ML', 'PRECIOSA 300ML'],
    'Quantidade_Vendida': [149, 164, 416, 236, 169, 187, 209, 407, 254, 194, 169, 243, 573, 290, 225, 106, 182, 470, 362, 204,
                           150, 213, 536, 319, 199, 188, 232, 520, 381, 195]
}

# Criando DataFrame para vendas
df_vendas = pd.DataFrame(data_vendas)

# Aplicando a conversão dos meses no DataFrame de vendas
ano_atual = 2024  # Define o ano atual
df_vendas = aplicar_converter_mes(df_vendas, 'Mes', ano_atual)

# Definindo os ingredientes e suas quantidades por milkshake
ingredientes = {
    'PANDORA 500ML': {'Nutella': 30, 'Brigadeiro de Leite Ninho': 30, 'Leite Ninho': 3.5, 'Sorvete': 1},
    'PANDORA 300ML': {'Nutella': 20, 'Brigadeiro de Leite Ninho': 20, 'Leite Ninho': 2.5, 'Sorvete': 1},
    'PRECIOSA 300ML': {'Nutella': 40, 'Ferreiro Roche': 1, 'Sorvete': 1},
    'MIMOSA 300ML': {'Brigadeiro de Leite Ninho': 40, 'Calda de Morango': 1.33, 'Leite Ninho': 1, 'Sorvete': 1},
    'MALHADA 300ML': {'Brigadeiro de Leite Ninho': 40, 'Oreo': 2.5, 'Leite Ninho': 1, 'Sorvete': 1}
}

# Inicializando DataFrame para estoque de ingredientes por mês
df_estoque_mensal = pd.DataFrame(columns=['Mes', 'Ingrediente', 'Quantidade_Consumida', 'Unidade'])

# Calculando a quantidade de cada ingrediente consumido por mês
for milkshake, ingredientes_info in ingredientes.items():
    # Filtra as vendas para o milkshake específico
    vendas_milkshake = df_vendas[df_vendas['Milkshake'] == milkshake]
    
    for ingrediente, quantidade in ingredientes_info.items():
        for _, row in vendas_milkshake.iterrows():
            quantidade_total = quantidade * row['Quantidade_Vendida']
            mes = row['Mes']
            
            # Verifica se o ingrediente já foi adicionado para o mês corrente
            if not ((df_estoque_mensal['Mes'] == mes) & (df_estoque_mensal['Ingrediente'] == ingrediente)).any():
                df_estoque_mensal = df_estoque_mensal.append({
                    'Mes': mes,
                    'Ingrediente': ingrediente,
                    'Quantidade_Consumida': quantidade_total,
                    'Unidade': 'g' if ingrediente not in ['Oreo', 'Ferreiro Roche', 'Calda de Morango'] else 'unidades'
                }, ignore_index=True)
            else:
                df_estoque_mensal.loc[(df_estoque_mensal['Mes'] == mes) & (df_estoque_mensal['Ingrediente'] == ingrediente),
                                      'Quantidade_Consumida'] += quantidade_total

# Verificando o DataFrame de estoque mensal
df_estoque_mensal

# Não é necessário aplicar a conversão dos meses novamente, já que eles já estão no formato correto
# Se a conversão foi aplicada acidentalmente, remova ou comente a linha abaixo

# Exibindo o DataFrame atualizado
df_estoque_mensal


# In[27]:


df_estoque_mensal['Mes'] = pd.to_datetime(df_estoque_mensal['Mes'])


# In[28]:


df_estoque_mensal.info()


# In[29]:


# Suponha que df seja seu DataFrame e 'coluna' seja a coluna que você deseja converter
df_estoque_mensal['Quantidade_Consumida'] = df_estoque_mensal['Quantidade_Consumida'].astype(float)


# In[30]:


df_estoque_mensal.info()


# In[31]:


df_estoque_mensal.set_index('Mes',drop=True,inplace=True)


# In[32]:


df_estoque_mensal


# In[33]:


pip install jinja2==3.0.3


# In[34]:


import sklearn
import sktime

print("scikit-learn version:", sklearn.__version__)
print("sktime version:", sktime.__version__)


# In[50]:


pip install pycaret==3.0.0 sktime==0.18.0 scikit-learn==1.1.3


# In[52]:


pip check


# In[35]:


pip install --upgrade pycaret-ts


# In[36]:


from pycaret.time_series import *


# In[ ]:


print(df_pivot.isnull().sum())


# In[ ]:


print(df_pivot.dtypes)


# In[ ]:


df_pivot['Mes'] = pd.to_datetime(df_pivot['Me], format='%m-%Y')  # Use o formato correto aqui


# In[ ]:


from pycaret.regression import setup, compare_models

# Configuração simplificada para garantir que tudo está funcionando
reg_setup = setup(
    data=df_pivot,
    target='Nutella',
    session_id=123,
    fold_strategy='timeseries', 
    fold=3,  # Usando um número menor de folds para simplificar
    data_split_shuffle=False, 
    fold_shuffle=False
)

# Comparando modelos
best_model = compare_models()
print(f'Melhor modelo:{best_model})


# O melhor modelo para prevermos a demanda do próximo mês é o Passive Aggressive Regressor
# 

# In[92]:


from pycaret.regression import finalize_model


# In[103]:


final_model = finalize_model(best_model)
final_model


# In[104]:


# Fazer previsões com os dados históricos
# Se você quiser prever valores para o próximo período, você pode precisar estender seus dados históricos
historical_data = df_pivot.copy()
historical_data['Predicted'] = None  # Placeholder para previsões


# In[106]:


# Adicionar previsões ao histórico
predictions = predict_model(final_model, data=historical_data)

# Verificar as colunas do DataFrame de previsões
predictions.head()


# In[108]:


# Encontrar o nome da coluna com as previsões
predicted_col = [col for col in predictions.columns if 'Label' in col or 'prediction' in col.lower()][0]


# In[109]:


# Adicionar previsões ao histórico
historical_data['Predicted'] = predictions[predicted_col]


# In[114]:


# Dados históricos
if 'Date' in historical_data.columns:
    plt.plot(historical_data['Date'], historical_data['Nutella'], label='Dados Reais', marker='o')
else:
    plt.plot(historical_data.index, historical_data['Nutella'], label='Dados Reais', marker='o')

# Previsões
if 'Date' in historical_data.columns:
    plt.plot(historical_data['Mes'], historical_data['Predicted'], label='Previsões', marker='x', linestyle='--')
else:
    plt.plot(historical_data.index, historical_data['Predicted'], label='Previsões', marker='x', linestyle='--')

# Configurações do gráfico
plt.title('Previsão de Demanda de Nutella')
plt.xlabel('Mes')
plt.ylabel('Demanda de Nutella')
plt.legend()
plt.grid(True)

# Mostrar o gráfico
plt.show()


# In[ ]:




