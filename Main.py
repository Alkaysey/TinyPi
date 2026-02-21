#CS 351 Lexler and Parser
#part 1 due on 2/25/2026

import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def displayToken(self):
        print("<",self.type,",",self.value,">")

class Lexer:
    def __init__(self):
        self.arr = []
    def addToken(self, type, value):
        self.arr.append(Token(type, value))

#patternFind is wip
def patternFind(string):
    patterns = ["\b(?:int|float|if|for)\b",]
    print(string + ' is: ' + "\n")
    nothing = 0 #if string meets no criteria
    if re.match("^[0-9]*$", string):
        print('a. An integer \n')


    nothing = nothing + 1
    if re.match("^\b(?:int|float|if|for)\b", string):
    print('b. A float consists of 1 or more digits before and after decimal
    point \n')
    nothing = nothing + 1
    if re.match("^[0-9]*\\.[0-9]{2}$", string):
    print('c. A float with exactly 2 digits after the decimal point \n')
    nothing = nothing + 1
    if re.match("^[0-9]*\\.[0-9]*[A-z]", string):
    nothing = nothing + 1
    print('d. A float end with letter f (4.321f) \n')
    if re.match("[A-Z]{1,}[a-z]{1,}\\d{1,}$", string):
    nothing = nothing + 1
    print('e. Capital letters, followed by small case letters, followed by
    digits \n')
    if re.match("^[0-9]{3}[A-z]{2,}", string):
    nothing = nothing + 1
    print('f. Exactly 3 digits, followed by at least 2 letters \n')
    if nothing == 0:
    print('Not recognized in any pattern \n')


def CutOneLineTokens(string):
    tokenList = Lexer

    while(string != ""):

        string = string[1:]
    ranges = re.search(pattern, string)
    removed = string[ranges.start():ranges.end()]
    newstring = re.sub(pattern, "", removed)
    return tokenList


def main():
    print("hey-there")
CutOneLineTokens ("int A1=5")