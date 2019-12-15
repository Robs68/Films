#!/bin/usr python

import pandas as pd

print("Lancement du script\n")

def to_csv() :
    file1_txt = open('liste_films1.txt','rb')
#file1 = unicode(file1, error='replace')
    df=pd.read_fwf('liste_films1.txt')
    df.to_csv('liste_films1.csv')
    df=pd.read_csv('liste_films1.csv')
    df.columns=["nombre","date","heure","tutu2","noms films", "suppr", "suppr2"]
    df=df.drop(["suppr","tutu2","suppr2"], axis=1)

#to_csv()
df=pd.read_csv('liste_films1.csv')
df.columns=["nombre","date","heure","tutu2","noms films", "suppr", "suppr2"]
df=df.drop(["suppr","tutu2","suppr2"], axis=1)

print ("find duplicate\n")

duplicate=df[df.duplicated(['noms films'])]
print (duplicate)
