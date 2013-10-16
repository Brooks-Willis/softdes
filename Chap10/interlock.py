"""
Written as a solution to an exercise in thinkpython by Allen Downey

Author: Brooks Willis

Either finds all interlocked or all triple interlocked english words 
"""

from bisect import *
def isinlist(word, wordlist):
    """
    Checks if a string is in a given list

    word: string
    wordlist: list of strings
    """
    index = bisect_left(wordlist,word)
    return index<len(wordlist) and word == wordlist[index]

def separate_word(word):
    """
    Unweaves word into two parts 

    word: string
    """
    word1 = word[::2]
    word2 = word[1::2]
    return [word1, word2]

def separate_word3(word):
    """
    Unweaves word into three parts 

    word: string
    """
    word1 = word[::3]
    word2 = word[1::3]
    word3 = word[2::3]
    return [word1, word2, word3]

def mkwrdlst():
    """
    Makes a list of all words from text file
    """
    fin = open('words.txt')
    words = []
    for line in fin:
        w = line.strip()
        words.append(w)
    return words


def interleave():
    """
    Finds all words which can be created by interweaving two other words.
    Returns a list of lists containing the interwoven word and the words 
    that build it.
    """
    words = mkwrdlst()
    interlocked = []
    
    for word in words:
        new_words = separate_word(word)

        if isinlist(new_words[0], words):
            if isinlist(new_words[1], words):
                interlocked.append([word, new_words[0], new_words[1]])
    return interlocked  

def triple_interleave():
    """
    Finds all words which can be created by interweaving three other words.
    Returns a list of lists containing the interwoven word and the words 
    that build it.
    """
    words = mkwrdlst()
    interlocked = []

    for word in words:
        new_words = separate_word3(word)

        if isinlist(new_words[0], words):
            if isinlist(new_words[1], words):
                if isinlist(new_words[2], words):
                    interlocked.append([word, new_words[0], new_words[1], new_words[2]])

    return interlocked

def printnicely(lockedwords):
    for sets in lockedwords:
        print sets[1], 'and', sets[2], 'interlock to form', sets[0]

def printnicely3(lockedwords):
    for sets in lockedwords:
        print sets[1]+', ' + sets[2], 'and', sets[3], 'interlock to form', sets[0]

lockedwords = interleave()
#lockedwords3 = triple_interleave()

printnicely3(lockedwords3)