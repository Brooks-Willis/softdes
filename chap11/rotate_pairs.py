def mkwrddct():
    """
    Makes a list of all words from text file
    """
    fin = open('words.txt')
    words = dict()
    for line in fin:
        w = line.strip()
        words[w] = w
    return words

def rot_letter(s,n):
    """Rotates a single letter by n spaces (ROT-n)

    s: string with one element
    n: integer
    """
    if s.islower():
        ind = ord('a')
    elif s.isupper():
        ind = ord('A')
    else:
        print s + " isn't a letter."

    c = (ord(s) - ind + n) % 26 +ind #I must admit, I needed to look at allen's code to get the % part of this

    return chr(c)

def rotate_word(s,n):
    """ROT encodes a given word by offset n
    
    s: alphabetical string
    n: integer
    """
    new_word = ''
    for c in s:
        new_word += rot_letter(c,n)

    return new_word

def rotate_pairs():
    """
    Finds all groups of words which are rotations of eachother

    output: none
    """
    words = mkwrddct()
    for word in words:
        for i in range(1, 14):
            new_word = rotate_word(word,i)
            if new_word in words:
                print word,'rotated by', i,'is', new_word

if __name__ == '__main__':
    rotate_pairs()









