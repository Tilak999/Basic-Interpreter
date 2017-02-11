keywords = {
    "print": "PRINT",
    ".": "PRINT",
    "if": "IF",
    "endif": "ENDIF",
    "else": "ELSE",
    "elseif": "ELSEIF",
    ":": "COND END"
}

maths_operators = {
    "+": "ADD",
    "-": "SUB",
    "/": "DIV",
    "^": "POW"
}

logical_operators = {
    ">": "GTHEN",
    "<": "LTHEN",
    "~": "NOT EQU",
    "=": "EQU"
}

termination_list = list()
termination_list.append(" ")
termination_list.append("\n")
termination_list.append("\t")
termination_list.append("(")
termination_list.append(")")

termination_list.extend(logical_operators)
termination_list.extend(maths_operators)

