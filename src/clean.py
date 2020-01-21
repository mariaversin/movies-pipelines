import pandas as pd
import json

def cleaning(data):
    data = data.drop(columns=['director','origin'], axis=1)
    data =data.rename(columns={
                            'Release Year': 'release',
                            'Title':'title',
                            'Origin/Ethnicity': 'origin',
                            'Director':'director',
                            'Genre': 'genre', 
                            'Cast':'cast'})
    return data

def movies_per_year(data_clean,year,genre):
    data_clean=titleGenre(data_clean)
    data=data_clean[(data_clean['release']==year) & (data_clean['genre'] == genre)]
    data['title'].values
    for title in data['title'].values:
        print(title)
    return data

def compare_df(data,oscar):
    for peli in data['title']:
        for premio in oscar['title']:
            if peli == premio:
                print("The movie -{}- won an oscar!!!".format(peli))


def titleGenre(data_clean):
    data_clean = data_clean.apply(lambda x: x.astype(str).str.title())
    return data_clean