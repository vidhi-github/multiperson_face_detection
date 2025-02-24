'''This module contains the function to merge two dataframes by removing duplicates on a common column'''

import pandas as pd


def merge_and_remove_duplicates(df1, df2, common_column):
    '''This function merges two dataframes based on a common column and removes duplicates'''
    df_merged = pd.merge(df1, df2, on=common_column, how = 'outer')
    df_merged = df_merged.drop_duplicates(subset=common_column, keep='first')
    return df_merged

def merge_dataframes(df1, df2, common_column):  
    '''This function merges two dataframes based on a common column'''
    df_merged = pd.merge(df1, df2, on=common_column)
    return df_merged

if __name__ == '__main__':
    df1 = pd.read_csv('src/reports/inferred_faces_glb_large_gate_left_cam.csv')
    df2 = pd.read_csv('src/reports/inferred_faces_glb_large_gate_right_cam.csv')
    df_merged = merge_and_remove_duplicates(df1, df2, 'name/id')
    df_merged.to_csv('src/reports/inferred_faces_glb_large_gate_merged.csv')