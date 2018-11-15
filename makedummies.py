import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# class MakeDummy(object):
    
#     def fit(self, df, col):
#         self.category = df[col].unique()

#     def transform(self, df, col):
#         for item in self.category:
#             df[item] = df[col] == item


#change categorical data into dummy variables, need to define a function so that 
#when new data comes into the pipeline, it can handle
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
            self.cols_to_dummy = columns 
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





    
# class DummyMaker:
#     """Class takes a categorical variable and returns a DataFrame with a column
#     for each category having values of 0 or 1 for each row.
#     A string passed to the constructor will become a prefix for dummy
#     column names.
#     """

#     def __init__(self, prefix=None):
#         self.levels = None
#         if prefix is None:
#             self.prefix = ""
#         else:
#             self.prefix = prefix + "_"
#         self.colnames = None

#     def fit(self, categorical_column):
#         """Store the levels from categorical_column, a pd.Series (df[colname]).
#         unique_cats is a list of unique categories in that column.
#         self.colnames creates dummy column names with optional prefix.
#         """
#         unique_cats = np.unique(categorical_column)
#         self.levels = unique_cats
#         self.colnames = [self.prefix + level.replace(" ", "-")
#                          for level in self.levels]

#     def transform(self, categorical_column, k_minus_one=False):
#         """If k_minus_one=True, the column representing the first unique category
#         is dropped.
#         The indexing of categorical_column is preserved in the new DataFrame.
#         """
#         num_rows = len(categorical_column)
#         num_features = len(self.levels)
#         dummies = np.zeros(shape=(num_rows, num_features))
#         for i, value in enumerate(self.levels):
#             dummies[:, i] = (categorical_column == value).astype(int)
#         if k_minus_one == True:
#             return pd.DataFrame(dummies[:, 1:], columns=self.colnames[1:],
#                                 index=categorical_column.index)
#         else:
#             return pd.DataFrame(dummies, columns=self.colnames,
#                                  index=categorical_column.index)