#!/bin/usr python

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print("Lancement du script\n")

def to_csv() :
    file1_txt = open('liste_films2.txt','rb')
    df2=pd.read_fwf('liste_films2.txt')
    df2.to_csv('liste_films2.csv')
#    df=pd.read_csv('liste_films1.csv')
#    df.columns=["nombre","date","heure","tutu2","noms films", "suppr", "suppr2"]
#    df=df.drop(["suppr","tutu2","suppr2"], axis=1)


#to_csv()
df=pd.read_csv('liste_films1.csv')
df.columns=["nombre","date","heure","tutu2","noms films", "suppr", "suppr2"]
df=df.drop(["nombre","date","heure","tutu2", "suppr", "suppr2"], axis=1)
print (df)

df2=pd.read_csv('liste_films2.csv')
df2.columns=["nombre","date","heure","tutu2","noms films"]
df2=df2.drop(["nombre","date","heure","tutu2"], axis=1)
print (df2)

#csv_1=df['noms films'].values

#print ("find duplicate Panda\n")

#duplicate=df[df.duplicated(['noms films'])]
#print (duplicate)

print ("find duplicate fuzzy\n")

#df2=df.copy()
#print (df2)
compare = pd.MultiIndex.from_product([df['noms films'],df2['noms films']]).to_series()


def metrics(tup):
    return pd.Series([fuzz.ratio(*tup),
                      fuzz.token_sort_ratio(*tup)],
                     ['ratio', 'token'])

matched_vendors = []

for row in df.index:
    noms1 = df.get_value(row,"noms films")
#    noms1 = df.at['noms films']
    for columns in df2.index:
        noms2=df2.get_value(columns,"noms films")
        matched_token=fuzz.token_sort_ratio(noms1,noms2)
        if matched_token> 85:
            matched_vendors.append([noms1,noms2,matched_token])
print (matched_vendors)
