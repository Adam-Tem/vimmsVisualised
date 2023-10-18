localVars = {}


def printKwargs(one, two):
    print(one)
    print(two)

localVars["one"] = 1
localVars["two"] = 2
localVars["three"] = 3

printKwargs(**localVars)

