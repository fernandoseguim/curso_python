def temp_min(temperaturas):
    min = temperaturas[0]

    for i in range(len(temperaturas)):
        if temperaturas[i] < min:
            min = temperaturas[i]

    return min

def temp_max(temperaturas):
    max = temperaturas[0]

    for i in range(len(temperaturas)):
        if temperaturas[i] > max:
            max = temperaturas[i]

    return max

def main():

    temperaturas = [21.5,32,35,28,19,35,19,22.5,23.4]

    print("A menor temperatura do mês foi %.1f C " % (temp_min(temperaturas)))
    print("A maior temperatura do mês foi %.2f C " % (temp_max(temperaturas)))

main()