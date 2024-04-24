#!/usr/bin/env python3
"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""

def isUnique( listOfTestStrings ):
    store = dict()
    for string in listOfTestStrings:
        unique = True
        for ch in string:
            if (store.get(ch)):
                unique = False
                break
            else:
                store[ch] = 1
        if (unique == False):
            print(f"String: {string} is not unique!")
        else:
            print(f"String: {string} is unique!")
        
    print(store)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    
    testString1 = "aabbb"
    testString2 = "abcdefg"

    listOfStrings = [testString1, testString2]    
    isUnique(listOfStrings)