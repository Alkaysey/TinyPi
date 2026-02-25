#CS 351 Lexler and Parser
#part 1 due on 2/25/2026

import re
from enum import Enum

class TokenType(Enum):
    KEYWORD = str("^(?:int|float|if|for)")
    IDENTIFIER = str("^[A-Za-z]+[A-Za-z0-9]*")
    FLOAT = str("^[0-9]{1,}\\.[0-9]{1,}")
    INTEGER = str("^[0-9]+")
    STRING = str("^[\"]{1}.*[\"]{1}")
    SEPERATOR = str("^[()\":]")
    OPERATOR = str("^[=>+*]")


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def displayToken(self):
        print("<", self.type, "," + self.value + ">")

class Lexer:
    def __init__(self):
        self.arr = []
    def addToken(self, type, value):
        self.arr.append(Token(type, value))
    def printLine(self):
        for token in self.arr:
            token.displayToken()

#patternFind is wip
def CutOneLineTokens(string):
    patterns = ["^(?:int|float|if|for)","^[A-Za-z]+[A-Za-z0-9]*","^[0-9]{1,}\\.[0-9]{1,}","^[0-9]+","^[\"]{1}.*[\"]{1}","^[()\":]","^[=>+*]"]
    tokenList = Lexer()
    #print(string)
    while string != "":
        for pattern1 in TokenType:
            #print(string)

            if string[0] == " ":
                string = re.sub("^\\s*", "", string)
                #print("space")
            if re.match(pattern1.value, string):
                #print(pattern1)
                ranges = re.search(pattern1.value, string)
                value1 = string[ranges.start():ranges.end()]
                #print(value1)
                tokenList.addToken(pattern1, value1)
                newString = re.sub(pattern1.value, "", string)
                string = newString
                #print(string+" new string")
                break
    return tokenList


if __name__ == '__main__':
    #print(CutOneLineTokens("int A1=5"))
    line = CutOneLineTokens("float A2     =    5.2")
    line.printLine()
    print(TokenType.KEYWORD.name)
