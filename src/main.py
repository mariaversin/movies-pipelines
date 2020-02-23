#!/usr/bin/env python3 
import sys
import argparse
import subprocess
import pandas as pd
import clean
import scraper

def recibeConfig():
    parser = argparse.ArgumentParser(description='''
    Oscar winner:
    1) Elige un año (entre 1960 y 2017) y un género y descubrirás si hay alguna película
    que tenga un Óscar.
    2) Ejemplos de género:
     --Romance, 
     --Comedy, 
     --Drama, 
     --Musical, 
     --Biographical, 
     --Adventure...
    ''')
    
    parser.add_argument('--year',
                        help='Año de estreno, desde 1960 hasta el 2017.',
                        default="1997"
                        )
    parser.add_argument('--genre',
                            help='A qué genero pertenece la película, por favor, sea específico',
                            default="Comedy"
                            )
                    
    args = parser.parse_args()
    print(args)
    return args


def main():
    # Pipeline
    print(sys.argv)

    config = recibeConfig()
    year = config.year
    genre =config.genre
    print(year)
    print(genre)
    data1, data2, wiki=importDataSet() # data
  
  
    print('\n ************************************************\n')
    # Cleaning data
    data_clean = clean.cleaning(data1) 
    lista_movies=clean.movies_per_year(data_clean,year,genre)
 
    
    print('\n-----------------------------\n')
    print('\n-----------------------------\n')
    # Data from Imdb page web scraping 
    oscar_clean = scraper.cleaning_oscar(data2) 
    lista_movies_oscar= scraper.oscars_per_year(oscar_clean,year)
    oscar = clean.compare_df(lista_movies,lista_movies_oscar,wiki)
    print(oscar)
    
    
    

def importDataSet():
    data_films = pd.read_csv('../output/peliculas.csv')
    pelis_wiki = pd.read_csv('../input/movies/movies.csv')
    data_oscar = pd.read_csv('../output/oscar.csv')
    return data_films, data_oscar, pelis_wiki

if __name__ == "__main__":
    main()
    