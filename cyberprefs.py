import os
import pandas as pd
from collections import defaultdict

def get_files():
    """Collects all .xlsx files in current working directory."""
    return [file for file in os.listdir() if file.endswith('.xlsx')]


def get_name(df):
    """Returns the name of the student from the DataFrame."""
    ROW_IDX, COL_IDX = 2, 1
    name = df.iloc[ROW_IDX][COL_IDX]
    name = name.replace('_', '').replace('Your Name: ', '')
    return name


def get_role_choices(df):
    """Subsets parent DataFrame, yielding student choices for roles."""
    role_choices = pd.DataFrame(df.loc[6:40, df.columns[[1,3,4,5]]]).dropna(how='all').fillna('')
    role_choices = role_choices[role_choices['Unnamed: 1'].str.contains(' Team')==False]
    return role_choices


def count_roles(df, counter, name):
    """Counts role choices."""
    ROLE, FIRST, SECOND, THIRD = range(0, 4)
    for _, row in df.iterrows():
        if row[ROLE] not in counter:
            counter[row[ROLE]] = {'first': [], 'second':[], 'third':[]}
        if row[FIRST]:
            counter[row[ROLE]]['first'].append(name)
        if row[SECOND]:
            counter[row[ROLE]]['second'].append(name)
        if row[THIRD]:
            counter[row[ROLE]]['third'].append(name)

    return counter


print(get_files())
df = pd.read_excel('testing.xlsx')
counter = {}
roles = get_role_choices(df)
print(roles)
print(count_roles(roles, counter, get_name(df)))