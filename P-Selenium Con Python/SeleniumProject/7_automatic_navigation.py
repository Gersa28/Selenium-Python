import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService



class NavigationTest(unittest.TestCase):

    def setUp(cls): # Ejecuta todo lo necesario antes de hacer una prueba
        """ Test fixture to prepare everything. """
        # Use the ChromeDriverManager to automatically handle the path to chromedriver
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.get('http://google.com/')
        driver.maximize_window()

    @classmethod #El decorador @classmethod indica que el método que sigue es un método de clase y no un método de instancia.
    def tearDownClass(self): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        # Agregamos una espera de 10 segundos antes de hacer clic en el botón de registro
        sleep(10) 
        self.driver.quit()

    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element('name', 'q')
        search_field.clear()

        search_field.send_keys('Germán Salina')
        search_field.submit()

        sleep(5)
        driver.back() # Retroceder
        sleep(5)
        driver.forward() # Avanzar
        sleep(5)
        driver.refresh()  # Refrescar

    

if __name__ == '__main__':
    unittest.main(
        verbosity=2, # Imprimir detalles de los resltados de los tests
        testRunner=HTMLTestRunner( # Para generar los reportes
            output='reports', 
            report_name='hello-world-report')
        )
    
'''
@classmethod Decorador:
El decorador @classmethod indica que el método que sigue es un método de clase y 
no un método de instancia.
Los métodos de clase reciben la clase en sí como el primer argumento, en lugar de 
una instancia de la clase. Este primer argumento es convencionalmente llamado cls, 
en lugar de self, que es lo que se usa en los métodos de instancia.
'''
