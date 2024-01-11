import pytest
from calculator import adunare, scadere, inmultire, impartire

# pytest fixtures
@pytest.fixture(params=[
    (2, 4, 6),
    (6, 12, 18),
    (5, 3, 8),
    (7, 12, 19),
    (3, 2, 5),
    (7, 7, 14)
])
def add_data(request):
    return request.param

@pytest.fixture
def add_data2(request):
    return request.param

@pytest.mark.parametrize('add_data2', [
    (2, 4, 6),
    (6, 12, 18),
    (5, 3, 8),
    (7, 12, 19),
    (3, 2, 5),
    (7, 7, 14)
])

def test_adunare_fixture_parametrize(add_data2):
    a, b, rezultat = add_data2
    assert adunare(a, b) == rezultat

def test_adunare():
    assert adunare(2,4) == 6
    assert adunare(6, 12) == 18
    assert adunare(5, 3) == 8
    assert adunare(7, 12) == 19
    assert adunare(3, 2) == 5

def test_adunare_rezultat_gresit():
    assert adunare(2, 5) != 6

def test_adunare_cu_string():
    with pytest.raises(TypeError):
        adunare('unu', 5)
    with pytest.raises(TypeError):
        adunare(1, 'cinci')

@pytest.mark.parametrize('add_data2', [
    (True, 5),
    (5, True),
    (False, 3),
    (3, False),
    (False, False),
    (True, True),
    (False, True),
    (True, False)
])

def test_adunare_cu_un_element_bool(add_data2):
    a, b = add_data2
    with pytest.raises(TypeError):
        adunare(a, b)

def test_adunare_cu_un_parametru_de_tip_dictionar():
    a = {
        'mere': 5,
        'pere': 3
    }
    b = 2
    with pytest.raises(TypeError):
        adunare(a, b)
    with pytest.raises(TypeError):
        adunare(b, a)

@pytest.mark.parametrize('add_data2', [
    (2, 3, 4),
    (2, 3, 4, 5),
    (2, 3, 4, 5, 6)
])

def test_adunare_parametri_multipli(add_data2: tuple):
    rezultat = sum(add_data2)
    assert adunare(*add_data2) == rezultat

def test_adunare_cu_0_si_1_fara_parametrizare():
    assert adunare(0, 1) == 1
    assert adunare(1, 0) == 1
    assert adunare(0, 0) == 0
    assert adunare(1, 1) == 2

@pytest.mark.parametrize('add_data2', [
    (0,1,1),
    (1,0,1),
    (0,0,0),
    (1,1,2)
])

def test_adunare_cu_0_si_1_cu_parametrizare(add_data2):
    pass


def test_adunare_cu_un_patrametru_lista():
    a = ['mere', 'pere']
    b = 2
    with pytest.raises(TypeError):
        adunare(a, b)
    with pytest.raises(TypeError):
        adunare(b, a)



def test_adunare_fixture(add_data):
    a, b, asteptat = add_data
    rezultat = adunare(a, b)
    assert asteptat, rezultat

def test_scadere():
    assert scadere(6, 3) == 3

@pytest.mark.parametrize('add_data3',[
    (4, 2, 2),
    (7, 5, 2),
    (20, 10, 10),
    (5.3, 3, 2.3)
])
def test_scadere_parametrii_multiplii(add_data3):
    a, b, rezultat = add_data3
    assert scadere(a, b) == rezultat

def test_scadere_cu_string():
    with pytest.raises(TypeError):
        scadere ('cinci', 3)
    with pytest.raises(TypeError):
        scadere(5, 'trei')

@pytest.mark.parametrize('add_data3', [
    (True, 7),
    (7, True),
    (False, 10),
    (10, False),
    (False, True),
    (True, False),
    (True, True),
    (False, False)
    ])
def test_scadere_cu_un_element_bool(add_data3):
    a, b = add_data3
    with pytest.raises(TypeError):
        scadere(a, b)

def test_scadere_cu_un_parametru_de_tip_dictionar():
    a = { "case": 10,
          "blocuri": 20}
    b = 7
    with pytest.raises(TypeError):
        scadere(a, b)
    with pytest.raises(TypeError):
        scadere(b, a)
#
def test_scadere_cu_un_parametru_lista():
    a = ['fructe', 'legume']
    b = 19
    with pytest.raises(TypeError):
        scadere(a, b)
    with pytest.raises(TypeError):
        scadere(b, a)

def test_scadere_fixture(add_data):
    a, b, asteptat = add_data
    rezultat = scadere(a, b)
    assert asteptat, rezultat

def test_inmultire():
    assert inmultire(10, 3) == 30

@pytest.mark.parametrize('add_data', [
    (2,3,6),
    (3,3,9),
])
def test_inmultire_parametrii_multiplii(add_data):
    a, b, rezultat = add_data
    assert inmultire(a, b) == rezultat

def test_inmultire_cu_un_string():
    with pytest.raises(TypeError):
        inmultire ('sapte', 3)
    with pytest.raises(TypeError):
        inmultire(7, 'trei')

@pytest.mark.parametrize('add_data3', [
    (True, 7),
    (7, True),
    (False, 10),
    (10, False),
    ])
def test_inmultire_cu_un_element_bool(add_data3):
    a, b = add_data3
    with pytest.raises(TypeError):
        inmultire(a, b)

def test_inmultire_cu_un_parametru_de_tip_dictionar():
    a = { "case": 10,
          "blocuri": 20}
    b = 7
    with pytest.raises(TypeError):
        inmultire(a, b)

def test_inmultire_cu_un_parametru_lista():
    a = ['fructe', 'legume']
    b = 19
    with pytest.raises(TypeError):
        inmultire(a, b)

# aici imi da eroare, dar merge daca pun in calculator
# if isinstance(a, (int)) or isinstance(b, int):
# return a*b
@pytest.mark.parametrize('add_data', [
    (3,3,9),
    (4,3,12)
])
def test_inmultire_fixture(add_data):
    a, b, asteptat = add_data
    rezultat = inmultire(a, b)
    assert asteptat, rezultat

def test_impartire():
    assert impartire(18, 9) == 2

def test_impartire_la_0():
    """asa prindem o eroare ridicata de o functie"""
    with pytest.raises(ZeroDivisionError):
        impartire(5, 0)







