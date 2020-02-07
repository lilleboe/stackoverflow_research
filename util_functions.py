import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def get_description(column_name, schema):
    """
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT -
            desc - string - the description of the column
    """
    desc = list(schema[schema['Column'] == column_name]['QuestionText'])[0]
    return desc


def total_count(df, col1, col2, look_for, delim=';'):
    """
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col1]
    delim - string delimiter value to break up the string by

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    """
    new_df = defaultdict(int)
    # loop through list of ed types
    for val in look_for:
        # loop through rows
        for idx in range(df.shape[0]):
            # if the type is in the row add 1
            if val in df[col1][idx].split(delim):
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df


def clean_and_plot(df, possible_vals, col='LanguageWorkedWith', title='Method of Educating Suggested', plot=True):
    '''
    INPUT
        df - a dataframe holding the CousinEducation column
        possible_vals - list of possible values to search for
        title - string the title of your plot
        axis - axis object
        plot - bool providing whether or not you want a plot back

    OUTPUT
        study_df - a dataframe with the count of how many individuals
        Displays a plot of pretty things related to the CousinEducation column.
    '''
    study = df[col].value_counts().reset_index()
    study.rename(columns={'index': 'method', col: 'count'}, inplace=True)
    study_df = total_count(study, 'method', 'count', possible_vals)

    study_df.set_index('method', inplace=True)
    if plot:
        (study_df / study_df.sum()).plot(kind='bar', legend=None);
        plt.title(title);
        plt.show()
    props_study_df = study_df / study_df.sum()
    return props_study_df


def count_lists(df, col, delim=';'):
    """
    INPUT:
    df - the pandas dataframe you want to search
    col - the column name you want to look through
    delim - string delimiter value to break up the string by

    OUTPUT:
   index_set = set of items found from the lists
    """
    my_list = []

    df = df[col].value_counts()
    for index, value in df.items():
        my_list += index.split(delim)
    index_set = list(set(my_list))
    return index_set
