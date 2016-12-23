from semana_05.lista_exercicios.fn_vogal import vogal


def test_eh_vogal_lower():
    assert vogal("a") == True

def test_not_eh_vogal_lower():
        assert vogal("b") == False

def test_eh_vogal_upper():
    assert vogal("E") == True