"""
Written as a solution to an exercise in thinkpython by Allen Downey

Author: Brooks Willis
Finds pairs of words which are palindromes
"""
def palindrome(word):
    """
    Reverses input word

    word: string
    """
    return word[::-1]

def find_pairs():
    """
    Finds all pairs of words which are palindromes of each other and prints 
    prints both words

    no inputs
    """
    fin = open('words.txt')
    words = []
    reverses = []
    for line in fin:
        w = line.strip()
        words.append(w)

    for word in words:
        pal = palindrome(word)
        if pal in words:
            del words[words.index(pal)]
            reverses.append([word, pal])
    print reverses        

find_pairs()

