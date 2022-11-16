# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:17:02 2022

@author: Data Rogue
"""

import pandas as pd

df = pd.read_excel("D&D 5E Spells.xlsx")
spells = df.sort_values('name').reset_index().drop('index',axis=1)
spells

def school_of_magic(data, school:str):
    """
    Finds all of the spells of a given school of magic from a DataFrame and
    returns a DataFrame object containing them.

    Parameters
    ----------
    data : Selects the DataFrame object you want to use for this function.
    Choose between the following: ['Abjuration','Conjuration','Divination',
                                   'Enchantment','Evocation','Illusion',
                                   'Necromancy','Transmutation']
    
    school : str
        Used to choose the school of magic of the spells you want to select.

    Returns
    -------
    school_all : DataFrame object with spells filtered from the DataFrame
    object used as the argument.

    """
    list_of_schools = ['Abjuration','Conjuration','Divination','Enchantment',
                       'Evocation','Illusion','Necromancy','Transmutation']
    if school in list_of_schools:
        school_all = data[data['school'] == f'{school}']
        return school_all
    else:
        raise NameError("No school of magic with this name.")
        return

def main():
    print("Utility spells can't TPK your party.")
    return

if __name__ == '__main__':
    main()
