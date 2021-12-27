from stock_market_predictions.main import EncapsulacionEnClase


parametro1 = []
parametro2 = 'prueba'
def test_tonto():
    objeto = EncapsulacionEnClase(parametro1,parametro2)
    assert objeto.parametro1 == []
    assert objeto.parametro2 == 'prueba'
