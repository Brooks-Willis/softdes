"""Created as a solution to excersice 16-7 in ThinkPython by
Allen Downey

Author: Brooks Willis
"""

from datetime import *

def double_day(day1, day2):
    """Computes the double day of the give input days
    
    day1: date object from datetime module
    day2: date object from datetime module

    return: double, date object
    """
    if day1 > day2:
        delta = day1-day2
        double = day1 + delta

    if day2 > day1:
        delta = day2-day1
        double = day2 + delta

    return double

def main():
    day1 = date(1993,3,19)
    day2 = date(1963,2,1)
    print 'Year-'+'Month-'+'Day'
    print double_day(day1,day2)

if __name__ == '__main__':
    main()