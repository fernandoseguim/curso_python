def maximo(x,y):
    if x > y:
        return x
    else:
        return y


def maximo3(x,y,z):
    if x > y > z:
        return x
    elif z > y > x:
        return z
    else:
        return y