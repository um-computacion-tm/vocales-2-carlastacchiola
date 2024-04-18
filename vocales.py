import unittest

def contar_vocales(mi_string):
    resultado = {}
    for letra in mi_string:
        if letra in 'aeiou' :
             if letra not in resultado:
                  resultado [letra] = 0
             resultado[letra]  += 1
        if letra in 'AEIOU' :
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] +=1
        if letra in 'áéíóú' :
            if letra not in resultado :
                resultado[letra] = 0
            resultado[letra] +=1
        if letra in 'ÁÉÍÓÚ' :
            if letra not in resultado :
                resultado[letra] = 0
            resultado[letra] +=1
    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

def test_contar_a(self):
    resultado = contar_vocales('cas')
    self.assertEqual(resultado, {'a': 1})

def test_contar_aa(self):
    resultado = contar_vocales('casa')
    self.assertEqual(resultado, {'a': 2})

def test_contar_aa(self):
    resultado = contar_vocales('bese')
    self.assertEqual(resultado, {'e': 2})

def test_contar_aa(self):
    resultado = contar_vocales('besa')
    self.assertEqual(resultado, {'a': 1, 'e' : 1})

def test_contar_aa(self):
    resultado = contar_vocales('casanova')
    self.assertEqual(resultado, {'a' : 3, 'o' : 1})

def test_contar_aa(self): 
    resultado = contar_vocales('Árbol')
    self.assertEqual(resultado, {'Á' : 1, 'O' : 1})

def test_contar_aa(self): 
    resultado = contar_vocales('Música')
    self.assertEqual(resultado, {'M' : 1,'ú' : 1, 'i' : 1})

def test_contar_aa(self): 
    resultado = contar_vocales('Televisión')
    self.assertEqual(resultado, {'T' : 1, 'e' : 2, 'i' : 2, 'ó' : 1})

def test_contar_aa(self): 
    resultado = contar_vocales('luciérnaga')
    self.assertEqual(resultado, {'a' : 2, 'é' : 1, 'i' : 1, 'u' : 1})



#unittest.main()
while(True):
    palabra = input('Ingrese una palabra: ')
    print(contar_vocales(palabra))

