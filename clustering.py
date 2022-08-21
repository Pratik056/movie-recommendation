from decimal import Clamped
import pre_processing
from sklearn.cluster import KMeans

def clustered_final_df(df):
    df['cluster_id']=None

    KMeans=KMeans(n_clusters=200)

    features=df[['P_Genre','S_Genre','T_Genre']]
    KMeans.fit(features)
    df['cluster_id']=KMeans.predict(features)
    return df

def cluster_everything(input_Movie):
    df=pre_processing.pre_process_all()
    print(df)
    df=clustered_final_df(df)
    print(df)
    df.to_csv('Dataset.csv')
    #Check if the Movie is present or not:
    input_Movie.lower()
    try:
        Movie_not_found=df.loc[~df['Movie'].str.contains(input_Movie)]
        if len(Movie_not_found)==0:
            print('Movie not found')
            return 0

        get_cluster=df['cluster_id'].loc[df['Movie'].str.contains(input_Movie)].values[0]
        similar_Movies_list=df['Movie'].loc[df['cluster_id']==get_cluster].values
        return similar_Movies_list
    except:
        print('Movie not found')
        return 0