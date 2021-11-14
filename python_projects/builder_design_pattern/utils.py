
def to_group(variable):
    if type(variable) != tuple or type(variable) != list:
        return tuple(variable)
    return variable
