from sys import *

TOKENS = ["PRINT", "IF"]


def openfile(filename):
    data = open(filename, 'r')
    return data


def tokenizer(filecontent):

    line = 0

    for char in filecontent:
        print(str(line)+" : "+char)
        line +=1




tokenizer(openfile(argv[1]))
