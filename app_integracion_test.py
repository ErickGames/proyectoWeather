import unittest
from openpyxl.reader.excel import load_workbook
from requests.api import get
from weather import *
import openpyxl

#Prueba de funcion que llama a otra funcion
#En este caso la funcion Convertir Graados llama a la funcion principal
#de obtener clima, traemos la variable de temperatura para convertirla a grados farenheit.

class TestApp(unittest.TestCase):

    def test_integracion_1(self):
        ciudad = 'saltillo'
        get_weather(ciudad)
        resultado = convertirGrados()
        self.assertEqual(resultado, 'Exito')

    def test_integracion_2(self):
        ciudad = 'londres'
        get_weather(ciudad)
        resultado = convertirGrados()
        self.assertEqual(resultado, 'Exito')

    def test_integracion_ENGLISH(self):
        ciudad = 'london'
        get_weather(ciudad)
        resultado = convertirGrados()
        self.assertEqual(resultado, 'Exito')


if __name__ == '__main__':
    unittest.main()