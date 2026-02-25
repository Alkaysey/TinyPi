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
def CutOneLineTokens(string):
    patterns = ["^(?:int|float|if|for)","^[A-Za-z]+[A-Za-z0-9]*","^[0-9]{1,}\\.[0-9]{1,}","^[0-9]*","^[\"]{1}.*[\"]{1}","^[()\":]","^[=>+*]"]
    tokenList = Lexer()

    while string != "":
        for pattern1 in patterns:
            #print(pattern1)
            print(string)
            #if re.match("^\s*", string):
                #string = re.sub(pattern, "", string)
                #print(string+"2")
            if re.match(pattern1, string):
                print(pattern1)
                ranges = re.search(pattern1, string)
                value1 = string[ranges.start():ranges.end()]
                print(value1)
                tokenList.addToken(pattern1, value1)
                newString = re.sub(pattern1, "", string)
                string = newString
                print(string+"3")
                break
    return tokenList


if __name__ == '__main__':
    #print(CutOneLineTokens("int A1=5"))
    CutOneLineTokens("int A2=5")