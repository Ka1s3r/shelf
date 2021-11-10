#┏━━━┓━━━━━━━━━━━┓━━━━━━━┓━━━┓━━━━━━━━━━━━━━━━
#┃┏━┓┃━━━━━━━━━━━┃━━━━┓┏┓┃━━━┃━━━━━━━━━━━━━━━━
#┃┃━┗┛━━┓━┓━┓━━━┓┃━━━━┃┃┃┃┓┏┓┗━┓━━┓━━┓━━━┓┓━┏┓
#┃┃━┏┓┏┓┃┏┛┏┓┓┏┓┃┃━━━━┃┃┃┃┃┃┃┏┓┃━┓┃━┏┓┓┏┓┃┃━┃┃
#┃┗━┛┃┗┛┃┃━┃┃┃┃━┫┗┓━━━┛┗┛┃┗┛┃┃┃┃┗┛┗┓┃┃┃┃━┫┗━┛┃
#┗━━━┛━━┛┛━┛┗┛━━┛━┛━━━━━━┛━━┛┛┗┛━━━┛┛┗┛━━┛━┓┏┛
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┃━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛━

from collections import Counter

stop_words = ['i',
 'me', 'my', 'myself', 'we', 'our','ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll",
 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to',
 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
 "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've',
 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't",
 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',
 "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

class Tome:
    def __init__(self, path):
        self.path  = path
        self.count = None
        self.frq   = {}
        self.mood  = None
        self.txt   = open(f'{self.path}', encoding="utf-8").read()
        self.unq   = None
        self.ntriv = []

    #  Here we collect all non-trivial words, i.e, all words not in our list of stop-words.
    @property
    def non_triv(self):
        non_trivial = []
        split_text = self.txt.split()
        for word in split_text: 
            if word not in stop_words:
                print(word)
                non_trivial.append(word)
        self.ntriv = non_trivial

    # Convert our list of non-trivial words to a set, in order to remove duplicates, giving us a list of unique vocabulary words for that text file.
    @property
    def unique(self):
        self.unq = set(self.txt.split())
        print(self.unq)
        return self.unq

    @property
    def freq(self):
        # Initializing an empty set where we will store words as we encounter them in our list. 
        logged = set()
        # Initializing an empty dictionary where we will store a word as a key, and its frequency as a value. {word:frequency}
        frequency = {}

        for word in self.txt.split():
            if word in logged:
                continue
            else:                
                logged.add(word)
                frequency[word] = self.txt.split().count(word)
                self.frq = frequency
                
        return frequency

   

