import pandas as pd

def preprocess(eve,reg):
    eve=eve[eve['Season']=='Summer']
    eve = eve.merge(reg, on='NOC', how='left')
    eve.drop_duplicates(inplace=True)
    eve = pd.concat([eve, pd.get_dummies(eve['Medal'], dtype=int)], axis=1)
    return eve