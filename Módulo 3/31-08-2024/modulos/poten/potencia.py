def potencia(x, y):
    i = 0
    while i != y:
        x *= x
        i += 1
        if i == y:
            break
    return x