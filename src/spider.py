#┏━━━┓━━━━━━━━━━━┓━━━━━━━┓━━━┓━━━━━━━━━━━━━━━━
#┃┏━┓┃━━━━━━━━━━━┃━━━━┓┏┓┃━━━┃━━━━━━━━━━━━━━━━
#┃┃━┗┛━━┓━┓━┓━━━┓┃━━━━┃┃┃┃┓┏┓┗━┓━━┓━━┓━━━┓┓━┏┓
#┃┃━┏┓┏┓┃┏┛┏┓┓┏┓┃┃━━━━┃┃┃┃┃┃┃┏┓┃━┓┃━┏┓┓┏┓┃┃━┃┃
#┃┗━┛┃┗┛┃┃━┃┃┃┃━┫┗┓━━━┛┗┛┃┗┛┃┃┃┃┗┛┗┓┃┃┃┃━┫┗━┛┃
#┗━━━┛━━┛┛━┛┗┛━━┛━┛━━━━━━┛━━┛┛┗┛━━━┛┛┗┛━━┛━┓┏┛
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┃━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛━

import os
from helpers import word_count, mood
from shelf import Shelf
from tome import Tome

# Creating the spider class. Spiders will do the bulk of the work in setting attributes. 
class Spider:
    def __init__(self, shelf=None, tome=None):
        self.shelf  = shelf
        self.tome   = tome
        self.report = {}

        if type(tome) != Tome and tome != None:
            raise TypeError('Librarian spiders can only crawl Tomes and Shelves')
        elif type(shelf) != Shelf and shelf != None:
            raise TypeError('Librarian spiders can only crawl Tomes and Shelves')

    # Go into every item in the list returned by os.listdir(). 
    # It is a list of strings containing the names of all of our files in the directory we give it.

    # We will calculate word count, text sentiment (mood), and the names of all our files.
    
    def crawl(self):
     # If the object passed to us is of type shelf, then deal with it the following way.   
     if self.shelf != None:
        for file in os.listdir(self.shelf.path):
            print(f'{file}')
            with open(f'{self.shelf.path}\\{file}', 'r', encoding='utf-8') as f:
                r = f.read()
                w = word_count(r)
                m = mood(r)
                self.shelf.vols.append(f'{file}')
                self.report[f'{file}'] = [w,m]

     # If the object passed to us is a single text file, run its native methods and report back.
     if self.tome != None:
         with open(f'{self.tome.path}', 'r', encoding='utf-8') as f:
             self.tome.count = word_count(f.read())
             self.tome.mood  = mood(self.tome.txt)  
             self.tome.non_triv
             self.tome.unique
             self.tome.freq
         

#SPIDERS.HELP.EXPLORE.LANGUAGE.FILES
#  / _ \_____________/`/\+-/\'\'\
#\_\(_)/_/           -+-    -+-+-
# _//o\\_            \'\/+-\/`/`/
#  /   \              \/-+--\/`/
# S.H.E.L.F            
#┏━━━┓━━━━━━━━━━━┓━━━━━━━┓━━━┓━━━━━━━━━━━━━━━━
#┃┏━┓┃━━━━━━━━━━━┃━━━━┓┏┓┃━━━┃━━━━━━━━━━━━━━━━
#┃┃━┗┛━━┓━┓━┓━━━┓┃━━━━┃┃┃┃┓┏┓┗━┓━━┓━━┓━━━┓┓━┏┓
#┃┃━┏┓┏┓┃┏┛┏┓┓┏┓┃┃━━━━┃┃┃┃┃┃┃┏┓┃━┓┃━┏┓┓┏┓┃┃━┃┃
#┃┗━┛┃┗┛┃┃━┃┃┃┃━┫┗┓━━━┛┗┛┃┗┛┃┃┃┃┗┛┗┓┃┃┃┃━┫┗━┛┃
#┗━━━┛━━┛┛━┛┗┛━━┛━┛━━━━━━┛━━┛┛┗┛━━━┛┛┗┛━━┛━┓┏┛
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┃━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛━   