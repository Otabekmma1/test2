def blue(text):
    return "\033[34m{}\033[0m".format(text)

def red(text):
    return "\033[31m{}\033[0m".format(text)

def yellow(text):
    return "\033[33m{}\033[0m".format(text)

def white_out(text):
    return "\033[47m{}\033[0m".format(text)

def black(text, shrift: bool=False):
    if shrift:
        return "\033[1m\033[30m{}\033[0m".format(text)
    return "\033[30m{}\033[0m".format(text)






