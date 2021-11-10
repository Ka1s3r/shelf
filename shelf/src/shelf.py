#┏━━━┓━━━━━━━━━━━┓━━━━━━━┓━━━┓━━━━━━━━━━━━━━━━
#┃┏━┓┃━━━━━━━━━━━┃━━━━┓┏┓┃━━━┃━━━━━━━━━━━━━━━━
#┃┃━┗┛━━┓━┓━┓━━━┓┃━━━━┃┃┃┃┓┏┓┗━┓━━┓━━┓━━━┓┓━┏┓
#┃┃━┏┓┏┓┃┏┛┏┓┓┏┓┃┃━━━━┃┃┃┃┃┃┃┏┓┃━┓┃━┏┓┓┏┓┃┃━┃┃
#┃┗━┛┃┗┛┃┃━┃┃┃┃━┫┗┓━━━┛┗┛┃┗┛┃┃┃┃┗┛┗┓┃┃┃┃━┫┗━┛┃
#┗━━━┛━━┛┛━┛┗┛━━┛━┛━━━━━━┛━━┛┛┗┛━━━┛┛┗┛━━┛━┓┏┛
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┃━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛━
    
from collections import Counter

class Shelf:
    def __init__(self, path, name = None):
        self.path = path
        self.name = name
        self.vols = []
        self.ct   = 0
        self.feel = None
                
# Reading text file
def mood(self):
    text = open(self.path, encoding="utf-8").read()

    # Converting to lowercase.
    lower_case = text.lower()

    # Creating a string of punctuation marks to check and replace within a given text, with nothing.
    punc = '''

        !()-[]{};:'"\,<>./?@#$%^&*_~

        '''
    # Removing punctuation in a given text by replacing punctuation characters with nothing.
    for char in lower_case:
        if char in punc:
            lower_case = lower_case.replace(char, " ") 

    # Splitting the lowered text into individual words.
    tokenized_words = lower_case.split()

    # Removing stop words from the tokenized list of words.
    # Stop words are words not important for sentiment analysis and are present in most sentences.
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our','ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its',
    'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these',
    'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
    'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out',
    'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
    'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y',
    'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
    'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    # Creating an empty list where we will store our non_trivial_words. Words like 'love', 'hate', 'happy', 'sad'.
    non_trivial_words = []

    # If our word is not a stop_word, then append it to our list of non_trivial_words.
    for word in tokenized_words:
        if word not in stop_words:
            non_trivial_words.append(word)
    print(non_trivial_words)

    # Initializing empty list where we will later store the emotions picked out by our algorithm.
    emotion_list = []
    
    with open('emotions.txt', 'r') as file:
        for line in file:
            bare_line = line.replace("\n", '').replace(",", '').replace("'", '').strip() 
            word, emotion = bare_line.split(':')
            if word in non_trivial_words:
                emotion_list.append(emotion)
        self.feel = emotion_list
        return self.feel

    #print(emotion_list)
    #emo = Counter(emotion_list)
    #print(emo)