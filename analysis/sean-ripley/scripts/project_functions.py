
def load_n_wrangle (path):
    
    #imports
    import pandas as pd
    import seaborn as sns
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    import statistics as stat
    
    #function to load data
    data = pd.read_csv(path)
    
    
    #removing two columns and excluding unwanted variables.
    df1 = ( 
        data
        .drop('bmi' , 1)
        .drop('region' , 1)
        [data['smoker'] == 'no']
        [data['age'] > 25 ] 
    )
    
    
    #making values numberic and re-indexing.
    df2 = ( 
        df1
        .replace(to_replace = 'yes' , value = 1)
        .replace(to_replace = 'no' , value = 0)
        .reset_index()
        .drop('index' , 1)  
    )  
    
    return df2

