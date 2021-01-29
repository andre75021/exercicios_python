from funcoes import convert, soma


def test_convert():
    assert 10 == convert('1010')
    assert 15 == convert('1111')

def test_soma():
    assert 2 == soma(1,1)
    assert 4 == soma(2,2)
    
