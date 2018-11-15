import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class Dummifier(BaseEstimator, TransformerMixin):
    """Dummify certain columns in a DataFrame"""
    def __init__(self, cols_to_dummy=None):
        if cols_to_dummy==None:
            self.cols_to_dummy = ['channels', 
                                  'country', 
                                  'currency', 
                                  'fb_published', 
                                  'has_analytics', 
                                  'has_header', 
                                  'has_logo', 
                                  'listed',
                                  'payout_type', 
                                  'show_map', 
                                  'user_type', 
                                  'has_payee_name', 
                                  'has_previous_payouts',
                                  'has_payout_type', 
                                  'has_facebook', 
                                  'has_twitter']
        else:
            self.cols_to_dummy = cols_to_dummy 
        self.unique_items = {}

    def fit(self, X, y=None):
        df = X
        for col in self.cols_to_dummy:
            self.unique_items[col] = df[col].unique()
        return self
            
    def transform(self, X):
        df = X
        dummy_df = pd.DataFrame()
        for col in self.cols_to_dummy:
            columns = self.unique_items[col]
            for item in columns:
                if item==None:
                    continue
                dummy_df[f'{col}_{item}'] = df[col]==item
            dummy_df = dummy_df.iloc[:,:-1]    
        df = df.drop(self.cols_to_dummy, axis=1)
        dummy_df = dummy_df.astype(int)
        df = pd.concat([df, dummy_df], axis=1)
        return df


