# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:02:04 2022

@author: Data Rogue
"""

import pandas as pd

df = pd.read_excel("D&D 5E Spells.xlsx")
spells = df.sort_values('name').reset_index().drop('index',axis=1)

def find_materials(data, spell_name:str):
    """
    Searches for the material components of a spell when given its name.
    
    Parameters
    --------
    data : Selects the DataFrame object you want to use for this function.
    
    spell_name : str
        String object that must be a spell name.
    
    Returns
    --------
    None.
    """
    material_components = data[data["M"].notna()]
    spell_list = [i for i in material_components["name"]]
    if spell_name not in spell_list:
        raise NameError("Spell has no material components, or name was typed incorrectly.")
    else:
        spell = material_components[material_components["name"] == spell_name]
        print("Spell:",spell["name"].values[0],"\n",
              "Materials:",spell["M"].values[0],"\n")
    return

def main():
    print("Why is it bat guano?")
    return

if __name__ == '__main__':
    main()
