import clustering_code
import os

def clean_t_dataset():
    try:
        os.remove('Dataset.csv')
    except:
        pass

def get_Movie_name():
    input_Movie=input("Enter the name of the Movie: ")
    Movies=clustering_code.cluster_everything(input_Movie)
    if type(Movies)==int:
        pass
    else:
        print(Movies)