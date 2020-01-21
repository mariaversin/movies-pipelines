import pandas as pd
def cleaning_oscar(oscar):
    oscar = oscar.drop(columns=['ratings'], axis=1)
    return oscar

def oscars_per_year(oscar_clean,year):
    oscar = oscar_clean
    oscar=oscar[(oscar['release']==year)]
    oscar['title'].values
    for title in oscar['title'].values:
        print(title)
    return oscar
   
