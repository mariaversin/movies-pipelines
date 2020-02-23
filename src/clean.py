import pandas as pd
import json
import numpy as np
import PDF as pdf

def cleaning_movies():

    '''Function 1 to clean data '''
    data = pd.read_csv('../input/movies/movies.csv')
    data = data.drop(columns=['Cast', 'Wiki Page'], axis=1)
    data = data.rename(columns={
                'Release Year':'year',
                'Title':'title_movie',
                'Origin/Ethnicity':'origin',
                'Director':'director',
                'Genre':'genres',
                'Plot':'plot'
    })
    data['genres']=data['genres'].replace('unknown',np.nan)
    data=data.dropna(axis=0, subset=['genres'])
    pdf.creaPDF(data)
    return data

def cleaning(data):

    '''Function 2 to clean data '''

    data = data.drop(columns=['director','origin'], axis=1)
    data =data.rename(columns={
                            'Release Year': 'year',
                            'Title':'title_movie',
                            'Origin/Ethnicity': 'origin',
                            'Director':'director',
                            'Genre': 'genres', 
                            'Cast':'cast'})
    return data

def movies_per_year(data_clean,year,genre):
    data_clean=titleGenre(data_clean)
    
    data=data_clean[(data_clean['release']==year)  & (data_clean['genre'] == genre)]
    data['title'].values
    for title in data['title'].values:
        print(title)
    
    return data

def compare_df(data,oscar,wiki):

    '''Compare 2 dataframes, one from IMDb 
        and the other from web scraping '''

    for peli in data['title']:
        for premio in oscar['title']:
            if peli == premio:
                return ( "\n\n The movie -{}- won an oscar!!!\n\n".format(peli))
            for col,row in wiki.iteritems():
                if col == 'Title':
                    if row == peli:
                        return ('\n\n Plot of this movie: *')


def titleGenre(data_clean):

    ''' Returns a string with first letter 
        of each word capitalized '''

    data_clean = data_clean.apply(lambda x: x.astype(str).str.title())
    return data_clean


