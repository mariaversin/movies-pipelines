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
                        default="1995"
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

    # PASO 1 - Recibir flags y estandarizarlos en un dict
    config = recibeConfig()
    year = config.year
    genre =config.genre
    print(year)
    print(genre)
    data1, data2 =importDataSet() # data
    #print("PELICULAS:" ) 
    #print(data1.shape)
    #print("OSCAR:" )
    #print(data2.title[100])
    print('\n --------------------*****---------------------\n')
    data_clean = clean.cleaning(data1) 
    lista_movies=clean.movies_per_year(data_clean,year,genre)
    #print(lista_movies)
    
    print('\n-----------------------------\n')
    print('\n-----------------------------\n')
    
    oscar_clean = scraper.cleaning_oscar(data2) 
    lista_movies_oscar= scraper.oscars_per_year(oscar_clean,year)
    oscar = clean.compare_df(lista_movies,lista_movies_oscar)
    

def importDataSet():
    data_films = pd.read_csv('../output/peliculas.csv')
    data_oscar = pd.read_csv('../output/oscar.csv')
    return data_films, data_oscar

if __name__ == "__main__":
    main()
    