# dnd-5e-spells
## Datasets and analysis of Dungeons &amp; Dragons 5th Edition spells.
## For D&D players
### How to use these assets
**Hello! Are you a D&D Player? Don't know how to use Python? Don't worry, you're exactly the kind of person I want to help.**

First of all, ***you don't need to know Python to use the Spells dataset.*** You can simply download the 'D&D 5E Spells.xlsx' file, open it on Excel, Google Sheets, or another app like it, and you're good to go.

However, if you want to use the dataset to its full potential, I recommend installing [Anaconda Navigator](https://www.anaconda.com/products/distribution). It will save you a ton of time and effort by creating an environment with loads of useful Python libraries already installed. For .py files, I recommend using the Spyder application, and Jupyter Notebook for .ipynb files (for these, you can also use Google Colab, but I can't recommend Google for anyone who wants to protect their data). If you do decide to use Anaconda, remember to launch the applications through the Anaconda Navigator app.

When you download this repository (you can do that by clicking the green dropdown button with 'Code' written on it at the top of the page), it will come as a zipped file. After you extract it, you will find the folders inside exactly as they are organized on Github. Now, I've separated the datasets from the other files to make things more organized, but if you want to run any scripts (either .py or .ipynb files), **you have to put the dataset you're trying to look at in the same folder as the script.** Personally, I'd just move all the files into the same folder to avoid any problems later.

For the .py files, if you do decide to use Spyder through Anaconda, after you run the file, you will notice that... **nothing happens**. Don't worry, you didn't do anything wrong. What happened here is that the function was saved to your system memory. To actually use the function, you have to call it. You can do that either by typing the function on a new line or in the console window. After you do that and run the code, or enter the command, the function will return you the result on the console window. However, the correct way to use the function is to assign it to a variable. To do that, you should write a line that looks something like this:
> wizard_spells = class_spells('Wizard')

This is just an example, you can do that with any of the classes. This saves the result of the function to your system memory, and now you can easily access it through the variable explorer on Spyder, or by entering the variable name in the console window. Usually, though, Python will shorten anything that has more than 60 items. So you will only be able to see the very first and very last items, which is why variable explorer is so useful: you can look at all the information stored within the variables.

For Jupyter Notebooks, when you launch the app, it will open a new tab on your browser (don't worry, this is normal). There, you will see all the folders on your computer. Find the one with your notebooks (the .ipynb files) and click on the file to open it. Once you have the file open, run all of the cells (there's a button at the top, or you can press either Ctrl+return or Shift+return to run the cell). If you do this right, you will see that the very first cell with code in it has text on the left that says: "In [1]:". That means it was your first input after you opened the file.

~~A quick note: **on the spells_analysis.ipynb file, there is a cell you should not run, or it _will_ give you an error.** It's the cell right before you see the _Infestation_ spell. When I was creating the dataset, I spelled 'Instataneous' instead of 'Instantaneous' on the 'duration' column. That cell was me trying to find out which spell I did that on. After I did, I corrected the spelling mistake in the .xlsx file.~~
> Accidently ran the cell when making the analysis, which then returned an empty DataFrame. Still, I wanted to keep a record here.

## Details
### On the datasets
These datasets were meant to be a resource for both players and data scientists alike. The goal was to make all the information about D&D spells readily available and easily accessible to all, ***for free.*** Basically, I was tired of having to look up spells in the physical books or third-party websites, while DND Beyond has an excellent filtering system that can find you exactly what spell or spells you're looking for, with the *small* caveat of having to pay hundreds of US dollars for the digital assets that include certain spells.

These datasets were all created by hand. I manually transcribed all the information about these spells. Naturally, as I am human, I may have made some mistakes. If you find any, please do let me know.

The one containing all the spells is 'D&D 5E Spells.xlsx'. The other datasets are all tables for specific spells, such as *Teleport* and *Control Weather*, for example.

The spells are all named as they appear in the pages of the books that describe them. That means they all start with capital letters, if they have more than one word, the other words also start with capital letters, but **words such as 'into', 'and', 'of', 'from', etc. and articles _do not_.** The columns 'V', 'S', 'M' stand for verbal, somatic and material components, respectively. On the 'book' column, I considered that each spell was unique to that book. Certain spells do appear in other books (like the _Chaos Bolt_ spell), but I decided to not include them here because I had already added the spell to the dataset, and didn't think it was something extremely relevant (proven right by the percentage of spells found in expansion books when compared to the Player's Handbook).

There are other datasets to add to the /datasets folder. They are datasets with the stat blocks for creatures summoned or created by spells. I haven't settled on a standard format for all of them, since some creatures have very different attributes (some have damage immunities, condition immunities, or even bonus actions, where others do not). Since this work was primarily focused on spells, I did put too much effort into creatures. I am working on deciding the structure for a dataset of creatures, but until then, I will refrain from posting those datasets. When I do, all creature stat blocks will be in a single dataset.

**An important note on spells from the _Explorer's Guide To Wildemount_:** Most of the spells from that book are either chronurgy or graviturgy spells, two different dunamancy schools of magic created by Matt Mercer. I made a conscious choice to omit this information from those spells. Technically, this is missing information. But, for most of them, you can figure out which one of those schools the spell belongs to either by its name or description. There are a few spells that are neither chronurgy or graviturgy, though.

### On the analysis
This is a work in progress. Right now, I will work towards making the general analysis of all the spells (that is, the full dataset). Eventually, when time allows it, I will analyze more specific items, such as: spells with material components, spells of a certain class, spells from a certain school of magic, etc. If you have any suggestions for things that I should look for during these, feel free to send them my way.

### On the other scripts
The /other_scripts folder is where I'll be posting things like functions, so I can easily import them into other files (especially to make my analysis more consistent).

**When I first uploaded these files, there was one file called spells_function.py. _It is no longer there._ I have since updated it to be classes_function.py, to make it clearer (the name of the function was also updated accordingly). The functionality is the same, the name was changed because I thought it was insufficient to explain what it does.**

### For the future
The end goal is not only to create a script that lets users look up spells with a filtering system as good as what DND Beyond has available, but also to make a script that lets users easily consult their known spells and select their prepared spells.

## Disclaimer
***This work was not authorized by Hasbro, Wizards of the Coast LLC, Dungeons & Dragons, or DND Beyond.***
