from sys import *
from lexar import Lexar
from eval import Eval
import dict


def main():

    data = open(argv[1], 'r')

    lexar = Lexar()
    lexar.addtoken(dict.keywords)
    lexar.addtoken(dict.maths_operators)
    lexar.addtoken(dict.logical_operators)
    tokens = lexar.tokenizer(data)

    eval_eng = Eval(tokens)
    eval_eng.execute()

    print(tokens)

main()
