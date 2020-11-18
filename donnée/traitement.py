import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
##

where = '/Users/IcloudElliott/Desktop/ENSAE/2A/STATAPP/velib_358.csv'
velib = pd.read_csv(where, sep=';')

##
from json import loads
station = velib.loc[0]
jour = station['10/19/20;18:01:51'] #exemple de ce qu'est un jour

def dico(jour):
    if isinstance(jour, str):
        dia = '{' + jour[2:-2].replace('{','').replace('}','').replace("'",'"') + '}'
        return(loads(dia))
    else:
        print(jour)
        return(jour)

test = dico(jour)
test


##
col_vide = '[{}, {}]'
colonnes_vides = []
for j in velib.columns:
    if velib[j][0] == col_vide:
        print(j)
        colonnes_vides.append(j)

velib=velib.drop(colonnes_vides, axis=1)

##
tete = velib.head()
print(tete)
cols = velib.columns
te = tete[cols[:5]]
te #sous-sections de la database sur lesquelles travailler pour tester

##
for j in velib.columns[1:]: #sans la colonne station_id
    velib[j] = [dico(i) for i in velib[j]] #ça serait ptet mieux avec un map



velib.to_csv('/Users/IcloudElliott/Desktop/ENSAE/2A/STATAPP/velib_clean.csv')
