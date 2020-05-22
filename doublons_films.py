#!/bin/usr python

import pandas as pd
from fuzzywuzzy import fuzz

print("Lancement du script\n")

df = pd.read_fwf('films_1.txt', names=["Noms"], skip_blank_lines=True)
df2 = pd.read_fwf('films_2.txt', names=["Noms"], skip_blank_lines=True)


def pattern(df):
    df['Noms'] = df['Noms'].str.replace("FRENCH", "")
    df['Noms'] = df['Noms'].str.replace("BDRip", "")
    df['Noms'] = df['Noms'].str.replace("BDRiP", "")
    df['Noms'] = df['Noms'].str.replace("x624", "")
    df['Noms'] = df['Noms'].str.replace("XviD", "")
    df['Noms'] = df['Noms'].str.replace("BluRay", "")
    df['Noms'] = df['Noms'].str.replace("DVDRiP", "")
    df['Noms'] = df['Noms'].str.replace("Multi", "")
    df['Noms'] = df['Noms'].str.replace("DTS", "")
    df['Noms'] = df['Noms'].str.replace("AC3", "")
    df['Noms'] = df['Noms'].str.replace("French", "")
    df['Noms'] = df['Noms'].str.replace(".avi", "")
    df['Noms'] = df['Noms'].str.replace(".mkv", "")
    df['Noms'] = df['Noms'].str.replace(".WEBRip.", "")


def fuzzy(df, df_copy, films):
    longeur = df.shape[0]
    longeur2 = df_copy.shape[0]
    for i in range(longeur):
        noms_1 = (df['Noms'][i])
        for f in range(longeur2):
            noms_2 = df_copy['Noms'][f]
            ratio = fuzz.ratio(noms_1, noms_2)
            if ratio > 85:
                # films.append("Doublon {} || {} ==>  ratio de {}".format(noms_1, noms_2, ratio))
                print("Doublon {} || {} ==>  ratio de {}".format(noms_1, noms_2, ratio))
                with open('Doublons.txt', 'a') as the_file:
                    the_file.write("Doublon {} || {} ==>  ratio de {}".format(noms_1, noms_2, ratio) + '\n')

    return films


pattern(df)
pattern(df2)
df_copy = df
df2_copy = df2

films = []
films2 = []
films = fuzzy(df, df_copy, films)
films2 = fuzzy(df2, df2_copy, films2)
films = fuzzy(df, df2, films)

print("Script fini")
