from semana_08.exercicios_aula.temperaturas import temp_min

def run_test_temp_min():
    print("Inicio dos testes...")
    temperaturas=[0]
    test_temp_min(temperaturas, 0)

    temperaturas = [0,0,0,0,0,0]
    test_temp_min(temperaturas, 0)

    temperaturas = [0,1,2,3,4,5,6,7,8,9,10]
    test_temp_min(temperaturas, 0)

    temperaturas = [30,27,25,26,29,31,32,33,30,29,24,26,30,27,24,25,26,24,22,23,25,25,28,28,32,32,31,29,28,31,33]
    test_temp_min(temperaturas, 22)

    temperaturas = [-15,-12,0,20,30]
    test_temp_min(temperaturas, -15)

    print("Fim dos testes...")

def test_temp_min(temperaturas, valor_esperado):
    valor_retornado = temp_min(temperaturas)
    if valor_retornado != valor_esperado:
        print("Falha no array %s! Era esperado o valor %.1f e foi retonado o valor %.1f " % (temperaturas,valor_esperado,valor_retornado))
    else:
        print("Sucesso!")

run_test_temp_min()