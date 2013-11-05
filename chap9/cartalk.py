def check_td(word):
    """
    Checks if the given word contains three consecutive double letters

    word: string
    """
    c = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            c += 1
            i += 2 
            if c == 3:
                return True
        else:
            c = 0
            i += 1 
    return False

def triple_double():
    """
    Finds all words containing three consecutive double letters
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if check_td(word):
            print word

def num_palindrome():
    """
    Finds the solution to the cartalk puzzler about odometers used as an exercise 
    in chapter 9 of think python    
    """
    nums = map(str, range(1000000))
    odo = []
    for i in range(len(nums)):
        if len(nums[i]) < 6:
            odo.append('0'*(6-len(nums[i])) + nums[i])
        elif len(nums[i]) == 6:
            odo.append(nums[i])
    
    for i in range(len(odo)-3):    
        first = odo[i][2:] == odo[i][:1:-1]
        second = odo[i+1][1:] == odo[i+1][:0:-1]
        third = odo[i+2][1:5] == odo[i+2][4:0:-1]
        fourth = odo[i+3][:] == odo[i+3][::-1]
        if first & second & third & fourth:
            print 'A possible odometer reading is '+odo[i]
        

num_palindrome()
print ''
triple_double()