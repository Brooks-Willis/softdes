"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks Willis

Determines if a word is a palindrome
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]



def is_palindrome(word):
    """Returns True if the input is a palindrome, and False if it is not

    word: String 
    """
    if not isinstance(word, str):
        print 'Input must be a string'
        return None
    elif len(word) < 2:
        return True 
    elif first(word) != last(word):
        return False
    else:
        newword = middle(word)
        return is_palindrome(newword)

print is_palindrome('cat')
print is_palindrome('tattarrattat') #Its a word! 
print is_palindrome('popcorn')
print is_palindrome('civic')
print is_palindrome('billygoat')