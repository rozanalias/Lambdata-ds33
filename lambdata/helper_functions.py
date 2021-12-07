import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

Adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
Nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrase(Adjectives,Nouns): 
    """random combination of adjectives and nouns"""
  
    return np.random.choice(Adjectives) + " " + np.random.choice(Nouns)

rphrase = random_phrase(Adjectives,Nouns)
print (rphrase)

def random_float(min_val, max_val):
    rf = np.arange(min_val , max_val, 0.1)
    return np.random.choice(rf)
min_val = 1
max_val = 5 
rfloat = random_float(min_val,max_val)
print(rfloat)

def random_bowling_score(int):
    rint = np.random.randint(int)
    return rint
int = 300

def silly_tuple():
    return random_phrase(Adjectives,Nouns), random_float(min_val,max_val), random_bowling_score(int)
   
print(silly_tuple())

def silly_tuple_list(num_tuples):
    return np.random.randint(( silly_tuple()), num_tuples)


print(random_bowling_score(int))
def  null_count(df):
    '''returns the number of null values 
    across the entire dataframe'''
    return df.isnull().sum().sum()

df = null_count(pd.DataFrame({'x': [1,2,np.NaN], 'y':[np.NaN,np.NaN,6]}))
print(df)

    
    
