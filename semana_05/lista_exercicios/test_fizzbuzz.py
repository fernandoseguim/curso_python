from semana_05.lista_exercicios.fn_fizzbuzz import fizzbuzz


def test_fizz():
    assert fizzbuzz(3) == "Fizz"

def test_buzz():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"

def test_not_fizznuzz():
    assert fizzbuzz(4) == 4
