# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10WxEABIRE8EoS1xCWfu3GU9xwLI1PxrM
"""

import pandas as pd

#importation de la dataset lieux
lieux = pd.read_csv('/content/lieux.csv')

#lecture de la dataset lieux
lieux

#importation de la dataset peapole
people = pd.read_csv('/content/people.csv')

#lecture de la dataset peapole
people

#jointure entre les deux datasets Lieux et Peapole en se basant sur la colonne Commune
Jointure = pd.merge(lieux, people, on='commune')

#Lecture de la table Jointure
Jointure

#Calcul le nombre de personnes nées région
REGION = Jointure['region'].value_counts()
#Calcul le nombre de personnes nées departement
DEPARTEMENT = Jointure['departement'].value_counts()

#exporter le fichier Region en json
with open('REGION', 'w', encoding='utf-8') as file:
    REGION.to_json(file, force_ascii=False)

#exporter le fichier Departement en json
with open('DEPARTEMENT', 'w', encoding='utf-8') as file:
    DEPARTEMENT.to_json(file, force_ascii=False)