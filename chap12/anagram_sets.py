from collections import Counter

def mkwrdlst(inputfile):
    """
    Makes a list of all words from text file

    inputfile: plain text file

    output: list of strings
    """
    fin = open(inputfile)
    words = []
    for line in fin:
        w = line.strip()
        words.append(w)
    return words

def eightletterwords(inputfile):
    """
    Makes a list of all 8 letter words from text file

    inputfile: plain text file

    output: list of strings
    """
    fin = open(inputfile)
    words = []
    for line in fin:
        w = line.strip()
        if len(w) == 8:
            words.append(w)
    return words

def alphabetize(word):
    """
    Alphabetizes a given string

    word: string

    output: string
    """
    return ''.join(sorted(word))

def allanagrams():
    """
    Finds all groups of words which are anagrams of each other

    output: list of lists of strings
    """
    words = mkwrdlst('words.txt')
    anagrams = dict()
    for word in words:
        alph = alphabetize(word)
        if alph not in anagrams:
            anagrams[alph] = [word]
        else:
            anagrams[alph] = anagrams[alph] + [word]
    temp = sorted(anagrams.values(), key = len, reverse = True)
    return [i for i in temp if len(i) != 1]

def bingo():
    """
    Finds the largest group of 8 letters words which are anagrams
    of eachother

    output: list of strings
    """
    words = eightletterwords('words.txt')
    anagrams = dict()
    for word in words:
        alph = alphabetize(word)
        if alph not in anagrams:
            anagrams[alph] = [word]
        else:
            anagrams[alph] = anagrams[alph] + [word]
    temp = sorted(anagrams.values(), key = len, reverse = True)
    return temp[0]

if __name__ == '__main__':
    temp = allanagrams() 
    for i in range(len(temp)):
        print temp[i]

    print bingo()