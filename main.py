def isOdd(param):
    if param is True:
        return True
    return isinstance(param, int) and param % 2 != 0
