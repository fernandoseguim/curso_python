def maximo(x,y,z):
    if x > y > z:
        return x
    elif z > y > x:
        return z
    else:
        return y