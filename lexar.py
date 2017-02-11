import dict


class Lexar:

    TOKENS = {}

    @staticmethod
    def is_num(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def error(line_num, msg, arg):
        print("PARSING ERROR : on Line "+str(line_num)+", "+msg+" '"+arg+"'")

    def addtoken(self,tokens):
        self.TOKENS.update(tokens)

    def tokenizer(self, data):

        line_number = 0
        found_tokens = []
        token = ""
        string = False
        variable = False

        for line in data:
            line_number += 1
            line += " "
            for char in line:
                if char in dict.termination_list:
                    if string:
                        token += char
                    elif variable:
                        variable = False
                        found_tokens.append("VARIABLE:"+token)
                        token = ""
                    elif self.is_num(token):
                        found_tokens.append("NUMBER:" + token)
                        token = ""
                    elif token != "":
                        self.error(line_number,"Undefined Token",token)
                        return []

                    if char in self.TOKENS:
                        found_tokens.append(self.TOKENS[char])
                else:
                    token += char
                    if token in self.TOKENS:
                        found_tokens.append(self.TOKENS[token])
                        token = ""
                    elif char == "\"" and not string:
                        string = True
                    elif char == "\"" and string:
                        string = False
                        found_tokens.append("STRING:" + token)
                        token = ""
                    elif char == "$":
                        if variable:
                            self.error(line_number, "Variable name can not contain $", token)
                            return []
                        else:
                            variable = True
        return found_tokens
