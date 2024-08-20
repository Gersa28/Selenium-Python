import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatizar búsquedad para que se apliquen en forma secuencial

class SearchTests(unittest.TestCase):

    @classmethod# Para que las pruebas corran en una sola ventana sin cerrar tras cada test y reemplazamos self pro cls
    def setUpClass(self): # Ejecuta todo lo necesario antes de hacer una prueba
        """ Test fixture to prepare everything. """
        # Use the ChromeDriverManager to automatically handle the path to chromedriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15) # Pausa de 15 segundos  
    
    @classmethod
    def tearDownClass(self): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        self.driver.quit()


    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element('name', 'q')
        search_field.clear() # limpia el campo de búsqueda en caso de que haya algún texto

        search_field.send_keys('tee') # enviamos al campo de búsqueda la palabra 'tee' = Camisa
        search_field.submit() # Enter

    def test_search_salt_shaker(self): # Preguntamos por un "Salero"
        driver = self.driver
        search_field = driver.find_element('name', 'q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        #Assertion
        products = self.driver.find_elements('xpath','//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a')
        self.assertEqual(1, len(products)) # Verifica si solo hay 1 producto

if __name__ == '__main__':
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner( # Para generar los reportes
            output='reports', 
            report_name='hello-world-report')
        )