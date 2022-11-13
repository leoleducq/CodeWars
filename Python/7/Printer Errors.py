def printer_error(s):
    return str(len([i for i in s if i not in 'abcdefghijklm'])) + "/" + str(len(s))