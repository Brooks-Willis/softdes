def mkwrddctlen(inputfile,n):
    """
    Makes a list of all words from text file that are length n

    inputfile: file containing words
    n: length of desired word

    output: dict of words
    """
    fin = open(inputfile)
    words = []
    for line in fin:
        w = line.strip()
        if len(w) == n:
            words.append(w)
    return words

def children(word):
    """
    Finds all the children (original word with one letter removed)
    of a given word

    word: string

    output:list of strings
    """

    kids = []
    for i in range(len(word)):
        newword = word[:i] + word[i+1:]
        kids.append(newword)

    return kids

def reduction():
    """
    Finds the longest reducible word in the english language

    output: string
    """
    memo = dict()
    memo[''] = ''
    memo['a'] = 'a'
    memo['i'] = 'i'
    n = 2
    i = 0
    words = mkwrddctlen('words.txt', 2)
    #print len(words), n
    while len(words) != 0:
        for word in words:
            kids = children(word)
            for element in kids:
                if element in memo:
                    memo[word] = word
                    
                    break
        n += 1 
        words = mkwrddctlen('words.txt', n)
        #print len(words), n
    temp = sorted(memo.values(), key = len, reverse = True)
    return temp[0]

if __name__ == '__main__':
    print reduction()    