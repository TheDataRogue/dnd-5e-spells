# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:05:42 2022

@author: Data Rogue
"""

import pandas as pd

df = pd.read_excel("D&D 5E Spells.xlsx")
spells = df.sort_values('name').reset_index().drop('index',axis=1)
spells

def spells_level(data,level:int):
    """
    Finds all of the spells of a given level from a DataFrame and returns a
    DataFrame object containing them.

    Parameters
    ----------
    data : Selects the DataFrame object you want to use for this function.
        
    level : int
        Used to choose the level of the spells you want to select.

    Returns
    -------
    leveled :
        DataFrame object with spells filtered from the DataFrame object used as
        the argument.

    """
    if level >= 0 and level <=9:
        leveled = data[data['level'] == level]
        return leveled
    else:
        raise ValueError("No spells of this level.")
        return


def main():
    print("and YOU get a Fireball, and YOU get a Fireball, and-")
    return

if __name__ == '__main__':
    main()