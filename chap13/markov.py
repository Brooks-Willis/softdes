"""Created as a solution to an exercise in 
Think Python by Allen B. Downey

Author: Brooks Willis
"""

import string
import random
from operator import itemgetter
def mashup(file1 = 'emma.txt',file2 = 'theiliad.txt',prefix_len = 2,skip_header=True):
    """Makes a histogram that contains the words from both files.

    file1: string
    file2: string
    prefix_len: int, length of prefix 
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    markov_map = {}
    words = []

    fp0 = file(file1)
    
    if skip_header:
        skip_gutenberg_header(fp0)

    for line in fp0:
        process_line(line, words)

    fp1 = file(file2)
    if skip_header:
        skip_gutenberg_header(fp1)

    for line in fp1:
        process_line(line,words)

    for i in range(prefix_len-1,len(words)-1):
        prefix = tuple(words[i-prefix_len:i])

        if prefix in markov_map:
            markov_map[prefix] = markov_map[prefix] + [words[i]]
        else:
            markov_map[prefix] = [words[i]]
    #print markov_map
    return markov_map


def process_file(filename, prefix_len = 2,skip_header=True):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    markov_map = {}
    words = []
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, words)

    for i in range(prefix_len-1,len(words)-1):
        prefix = tuple(words[i-prefix_len:i])

        if prefix in markov_map:
            markov_map[prefix] = markov_map[prefix] + [words[i]]
        else:
            markov_map[prefix] = [words[i]]
    #print markov_map
    return markov_map


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, words):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    words: list of strings
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        words.append(word)

def random_suffix(pre, markov_map):
    """Chooses a random word from a given value in dict.

    The probability of each word is proportional to its frequency.
    """
    
    temp = markov_map[pre]
    #print temp, 'options'
    n = random.randint(0,len(temp)-1)

    return temp[n]

def markov(markov_map, prefix_len, text_len=100):
    """Runs a Markov analysis of given dictionary

    markov_map: dict with prefixes in tuples as keys, and possible suffixes as string values
    prefix_len: int, length of prefixes
    text_len = int, length of desired paragraph
    """
    pre = random.choice(markov_map.keys())
    for word in pre:
        print word,
    for i in range(text_len):
        x = random_suffix(pre, markov_map)
        print x,
        pre = pre[1:] + (x,)

if __name__ == '__main__':
    order = 2
    text_len = 200
    markov_map = process_file('emma.txt', order, skip_header=True)
    
    markov(markov_map, order, text_len)

    # Markov Mashup
    #mashup_map = mashup('emma.txt','theiliad.txt',order,skip_header=True)

    #markov(mashup_map, order, text_len)