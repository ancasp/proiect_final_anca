# def adunare(a,b):
#     if isinstance(a, str) or isinstance(b, str):
#         raise TypeError
#     elif isinstance(a, bool) or isinstance(b, bool):
# #  SAU   elif type(a) == bool or type(b) == bool:
#         raise TypeError
#     return a+b

def adunare(*args):
    for arg in args:
        if isinstance(arg, bool):
            raise TypeError
    return(sum(args))
def scadere(*args):
#    return a-b
    for arg in args:
        if isinstance(arg, bool):
            raise TypeError
    rezultat = args[0]
    for numar in args[1:]:
        rezultat -= numar
    return rezultat

def inmultire(a, b):
    # return a*b
    if not type(a) == int:
        raise TypeError
    elif not type(b) == int:
        raise TypeError
    elif not type(a) == float:
        raise TypeError
    elif not type(b) == float:
        raise TypeError
    return a*b
    # if isinstance(a, (int)) or isinstance(b, int):
    #     return a*b

def impartire(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def ridicare_la_putere(a, b):
    pass

