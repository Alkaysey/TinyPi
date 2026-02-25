#CS 351 Lexler and Parser
#part 1 due on 2/25/2026

import re
from enum import Enum

class TokenType(Enum):
    KEYWORD = str("^(?:int|float|if|for)")
    IDENTIFIER = str("^[A-Za-z]+[A-Za-z0-9]*")
    #LITERAL = str("^([0-9]{1,}\\.[0-9]{1,}|[0-9]+|[\"]{1}.*[\"]{1})")
    FLOAT = str("^[0-9]{1,}\\.[0-9]{1,}")
    INTEGER = str("^[0-9]+")
    STRING = str("^[\"]{1}.*[\"]{1}")
    SEPERATOR = str("^[()\":]")
    OPERATOR = str("^[=>+*]")


class Token:
    def __init__(self, type, value):
        self.type = TokenType(type)
        self.value = value
    def displayToken(self):
        print("<" + self.type.name + "," + self.value + ">")

class Lexer:
    def __init__(self):
        self.arr = []
    def addToken(self, type, value):
        self.arr.append(Token(type, value))
    def printLine(self):
        for token in self.arr:
            token.displayToken()

def CutOneLineTokens(string):
    tokenList = Lexer()
    while string != "":
        for pattern1 in TokenType:
            if string[0] == " ":
                string = re.sub("^\\s*", "", string)
            if re.match(pattern1.value, string):
                ranges = re.search(pattern1.value, string)
                value1 = string[ranges.start():ranges.end()]
                tokenList.addToken(pattern1, value1)
                newString = re.sub(pattern1.value, "", string)
                string = newString
                break
    return tokenList

if __name__ == '__main__':
    line = CutOneLineTokens("int A2 int float A2     =    \"string\"")
    line.printLine()
