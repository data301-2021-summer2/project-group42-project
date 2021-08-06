#Libraries
import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt
import statistics as stat

#Functions
def wranglemania2K21(datapath): #Loads and wrangles data for my research question
    
    data = pd.read_csv(datapath) #Load dataframe from path E.g. wranglemania2K21("insurance.csv")

    df1 = (
        data
        .drop('children' , 1)  #Drops the children
        .drop('region' , 1)    #Drops the region
        [data['bmi'] <= 45]    #Removes people with BMIs greater than 45
    )

    df2 = (
        df1
        .reset_index()          #Resets the index
        .drop('index' , 1)      #Removes the od index
    )
    
    return df2                  #Returns the processed dataframe