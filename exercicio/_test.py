import pytest

def calcula_pagamento(horas,vHora):
	return horas * vHora

def test_calcula_pagamento():
	assert calcula_pagamento(10,2) == 20
	assert calcula_pagamento(5,7) == 35
	assert calcula_pagamento(3,3) == 9
	assert calcula_pagamento(1.5,2) == 3.0
	assert calcula_pagamento(3.3,2) == 6.6


calcula_pagamento(5,5)	
