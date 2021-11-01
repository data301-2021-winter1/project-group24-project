import pandas as pd
import numpy as np

def unprocessed(csv_file):
    df = pd.read_csv(csv_file , delimiter = ';')
    return df

def load_and_process(csv_file):
    df = pd.read_csv(csv_file , delimiter = ';')
     ##Loads and cleans data by removing redundancy, unused columns and null values
    df1=(df.copy().drop(['player_id','team' , 'nationality'] , axis = 1) 
        .sort_values("overall", ascending = False)
        .reset_index(drop=True)
        )
    conditions = [
    (df['overall'] > 85),
    (df['overall'] > 70) & (df['overall'] <= 85),
    (df['overall'] > 0) & (df['overall'] <= 70),]

    values = ['Gold', 'Silver', 'Bronze']

    df1['Rating'] = np.select(conditions, values)
    return df1

