"""
Written as a solution to excercise 14.3 in Allen Downey's "ThinkPython"

Authors: Brooks Willis 
Worked with Josh Jangowitz
"""

import anagram_sets
import shelve
def main(word = 'anagram'):
    store_anagrams()
    print read_anagrams(word)

def store_anagrams(filename = 'words.txt'):
    """
    Finds the anagrams of the words in the given file and stores 
    them to 'anagram_shelf'

    """
    fout = shelve.open('anagram_shelf')
    fout.update(anagram_sets.all_anagrams(filename))
    fout.close()

def read_anagrams(word):
    """
    Finds all anagrams of given word using "anagram_shelf" file

    word = string

    output: list of strings (anagrams of word)
    """
    fin = shelve.open('anagram_shelf')
    sig = anagram_sets.signature(word)
    return fin[sig]

if __name__ == '__main__':
    main()