import dict


class Eval:

    def __init__(self,tokens):
        self.tokens = []
        self.value = []

        for token in tokens:
            parts = token.split(":")
            if len(parts) == 1:
                self.tokens.append(parts[0])
                self.value.append("")
            else:
                self.tokens.append(parts[0])
                self.value.append(parts[1])

    def process(self, tokens, values):

        i = 0

        while i < len(tokens):
            if tokens[i] == "PRINT" and tokens[i+1] == "STRING":
                print(values[i+1].strip("\""))
                i += 2
            elif tokens[i] == "IF":
                if tokens[i + 1] == "NUMBER" and tokens[i + 2] in dict.logical_operators.values() and tokens[
                            i + 3] == "NUMBER" and \
                                tokens[i + 4] == "COND END":
                    num1 = int(values[i + 1])
                    cond = tokens[i + 2]
                    num2 = int(values[i + 3])
                    i += 5

                    #print(num1, num2, cond)
                    valid = False

                    if cond == "EQU":
                        if num1 == num2:
                            valid = True;
                    elif cond == "GTHEN":
                        if num1 > num2:
                            valid = True;
                    elif cond == "LTHEN":
                        if num1 < num2:
                            valid = True;
                    elif cond == "NOT EQU":
                        if num1 != num2:
                            valid = True;
                    else:
                        valid = False

                    #print(valid)
                    while not valid and tokens[i] != "ENDIF":
                        #print(tokens[i])
                        i+=1

            else:
                #print(tokens[i])
                i += 1

    def execute(self):
        self.process(self.tokens, self.value)

