#!/bin/usr python

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print("Lancement du script\n")

def to_csv() :
    file1_txt = open('liste_films1.txt','rb')
#file1 = unicode(file1, error='replace')
    df=pd.read_fwf('liste_films1.txt')
    df.to_csv('liste_films1.csv')
    df=pd.read_csv('liste_films1.csv')
    df.columns=["nombre","date","heure","tutu2","noms films", "suppr", "suppr2"]
    df=df.drop(["suppr","tutu2","suppr2"], axis=1)

def fuz(a):
   ratio=fuzz.token_sort_ratio(df['noms films']

#to_csv()
df=pd.read_csv('liste_films1.csv')
df.columns=["nombre","date","heure","tutu2","noms films", "suppr", "suppr2"]
df=df.drop(["suppr","tutu2","suppr2"], axis=1)

csv_1=df['noms films'].values

print ("find duplicate Panda\n")

duplicate=df[df.duplicated(['noms films'])]
print (duplicate)

print ("find duplicate fuzzy")
print ("")

ratio=fuzz.token_sort_ratio("string","string2")
print (ratio)


