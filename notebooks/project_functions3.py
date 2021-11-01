import pandas as pd
import numpy as np

def unprocessed(csv_file):
    df = pd.read_csv(csv_file , delimiter = ';')
    return df

def loadandprocess(path):
    
    #Method chaining 1
    data1 = (pd.read_csv(path , delimiter = ';')
      .dropna(axis=0, inplace=False)
      .drop(labels=['player_id', 'nationality', 'position', 'team'], axis=1, inplace=False)
      .drop_duplicates(subset=['overall','hits','age','potential'], keep='first', inplace=False, ignore_index=True)
      .rename(columns={"overall": "OverallRating", "potential": "PotentialGrowth"},inplace=False)
       )
    
    data1.insert(len(data1.columns), 'Potential-Overall', (data1.PotentialGrowth-data1.OverallRating), allow_duplicates=False)
    return data1
