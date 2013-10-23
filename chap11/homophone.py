import pronounce

def mkwrddct(inputfile):
    """
    Makes a list of all words from text file

    inputfile: plain text file

    output: dictionary
    """
    fin = open(inputfile)
    words = dict()
    for line in fin:
        w = line.strip()
        words[w] = w
    return words

def homophones():
    """
    Finds all words, which without either the first or second letter
    is a homophone of the orignal word

    output: none
    """
    pron = pronounce.read_dictionary('c06d')
    words = mkwrddct('words.txt')

    for word in words:
        phone1 = word[1:]
        phone2 = word[0] + word[2:]
        if phone1 in pron and phone2 in pron and word in pron:
            if pron[word] == pron[phone1] and pron[word] == pron[phone2]:
                print word, phone1, phone2

if __name__ == '__main__':
    homophones()





