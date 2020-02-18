import clean as clean
import pandas as pd
import PDF as pdf

def Data():
    
    pelis=clean.cleaning_movies()
    year = pelis['year']
    genre =pelis['genres']
    oscars = oscars_data()
    print('\n*********************DATA***********************\n')
    
    return pelis, oscars

def oscars_data():
    oscars= pd.read_csv('../output/oscar.csv')
    oscars = oscars.rename(columns={
                'title':'title_movie',
                'release':'year'
    })
    print('\n****************************************************\n')
    return oscars


