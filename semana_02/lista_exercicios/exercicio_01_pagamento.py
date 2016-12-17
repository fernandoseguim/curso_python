def main():
    cliente = input("Digite o nome do cliente: ")
    diaVencimento = input("Digite o dia de vencimento: ")
    mesVencimento = input("Digite o mês de vencimento: ")
    valor = input("Digite o valor da fatura: ")

    msg = "Olá, " + cliente + "\n"
    msg += "A sua fatura com vencimento em " + diaVencimento + " de " + mesVencimento + " no valor de R$ " + valor + " está fechada."

    print(msg)


main()
