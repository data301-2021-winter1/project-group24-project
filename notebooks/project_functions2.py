import pandas as pd
import numpy as np

def unprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df

def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
     ##Loads and cleans data by removing redundancy, unused columns and null values
    df1=(df.copy().drop(["player_id","nationality","team","potential","Overall rating"] , axis = 1) 
        .sort_values("overall", ascending = False)
        .reset_index(drop=True)
        ) 
    
    conditions = [
    (df['overall'] >= 85),
    (df['overall'] < 85) & (df['overall'] >=70),
    (df['overall'] < 70)
    ]
    values = ['Gold', 'Silver', 'Bronze']
    df2=(df1.copy())
    df2['Rating'] = np.select(conditions, values)
    
    df3=(df2.copy().rename(columns={"potential": "potential growth"}))
    return df3
         
    