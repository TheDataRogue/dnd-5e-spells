# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 00:40:44 2022

@author: Data Rogue
"""
import pandas as pd

df = pd.read_excel("D&D 5E Spells.xlsx")
spells = df.sort_values('name').reset_index().drop('index',axis=1)
spells

def class_spells(char_class:str):
    """
    Filters the spells of a given D&D 5E character class and organizes them
    into a DataFrame object, in the same way they would be organized in an
    official book, by level and alphabetically for each spell level.
    
    Parameters
    --------
    char_class : string object that must be one D&D 5E spellcasting class
    (Artificer, Bard, Cleric, Druid, Paladin, Ranger, Sorcerer, Warlock, or
    Wizard).
    
    Returns
    --------
    char_class_spells : DataFrame object with the spells of the class chosen by
    the argument.
    """
    char_class_spells = [] # creates an empty list
    for i in range(0,len(spells)): # with the next line, iterates through the entire DataFrame by index
        name = spells['name'][i] # creates a string object equal to the name of the spell 
        spell = spells[spells['name'] == name] # creates a single DataFrame object using the name of the spell as a filter
        if f"{char_class}" in spell['classes'].values[0]: # if the argument matches one of the character classes of the spell
            char_class_spells.append(spell) # appends the DataFrame object to the list
    char_class_spells = pd.concat(char_class_spells, ignore_index=True) # turns the list of DataFrames into a single DataFrame
    cantrips = char_class_spells[char_class_spells['level'] == 0] # separates all the cantrips
    cantrips = cantrips.sort_values('name').reset_index().drop('index',axis=1) # orders them alphabetically
    first_level = char_class_spells[char_class_spells['level'] == 1] # does the same for the other levels of spells
    first_level = first_level.sort_values('name').reset_index().drop('index',
                                                                     axis=1)
    second_level = char_class_spells[char_class_spells['level'] == 2]
    second_level = second_level.sort_values('name').reset_index().drop('index',
                                                                       axis=1)
    third_level = char_class_spells[char_class_spells['level'] == 3]
    third_level = third_level.sort_values('name').reset_index().drop('index',
                                                                     axis=1)
    fourth_level = char_class_spells[char_class_spells['level'] == 4]
    fourth_level = fourth_level.sort_values('name').reset_index().drop('index',
                                                                       axis=1)
    fifth_level = char_class_spells[char_class_spells['level'] == 5]
    fifth_level = fifth_level.sort_values('name').reset_index().drop('index',
                                                                     axis=1)
    sixth_level = char_class_spells[char_class_spells['level'] == 6]
    sixth_level = sixth_level.sort_values('name').reset_index().drop('index',
                                                                     axis=1)
    seventh_level = char_class_spells[char_class_spells['level'] == 7]
    seventh_level = seventh_level.sort_values('name').reset_index().drop('index',
                                                                         axis=1)
    eighth_level = char_class_spells[char_class_spells['level'] == 8]
    eighth_level = eighth_level.sort_values('name').reset_index().drop('index',
                                                                       axis=1)
    ninth_level = char_class_spells[char_class_spells['level'] == 9]
    ninth_level = ninth_level.sort_values('name').reset_index().drop('index',
                                                                     axis=1)
    char_class_spells = pd.concat([cantrips,first_level,second_level, # Takes all the different DataFrames and
                                   third_level,fourth_level,fifth_level, # orders them into a single DataFrame object,
                                   sixth_level,seventh_level,eighth_level, # organized in ascending order by level and
                                   ninth_level], ignore_index=True) # each level ordered alphabetically
    return char_class_spells

def main():
    print("Druids >>>>")
    return

if __name__ == '__main__':
    main()
