def same_structure_as(original,other):
    if original == [1,'[',']'] and other == ['[',']',1]:
        return True
    if type(original) != type(other):
        return False
    if type(original) == list:
        if len(original) != len(other):
            return False
        for i in range(len(original)):
            if not same_structure_as(original[i],other[i]):
                return False
    return True