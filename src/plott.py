import seaborn as sns
import pandas as pd
import clean as clean
import matplotlib.pyplot as plt

def image_movies(data):
    print('\n\n-----------------PLOT--------------------\n\n')
    print(data.head())
    sns.set(style="white")
    plt.figure(figsize=(15,10))
    sns.barplot(y="release", x="title", data=data,palette=("RdBu"))
    path_image='../output/movies.png'
    plt.savefig(path_image)
    return path_image


