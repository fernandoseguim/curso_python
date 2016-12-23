def vogal(letra):

    list_vogais = ["a","e", "i", "o", "u"]

    for i in list_vogais:
        if str.upper(letra) == str.upper(i):
            return True

    return False
