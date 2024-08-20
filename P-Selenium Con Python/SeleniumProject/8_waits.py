import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitTests(unittest.TestCase):

    @classmethod# Para que las pruebas corran en una sola ventana sin cerrar tras cada test y reemplazamos self pro cls
    def setUpClass(cls): # Ejecuta todo lo necesario antes de hacer una prueba
        """ Test fixture to prepare everything. """
        # Use the ChromeDriverManager to automatically handle the path to chromedriver
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15) # Pausa de 15 segundos

    @classmethod #El decorador @classmethod indica que el método que sigue es un método de clase y no un método de instancia.
    def tearDownClass(cls): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        # Agregamos una espera de 15 segundos antes de hacer clic en el botón de registro
        time.sleep(10) 
        cls.driver.quit()

    def test_account_link(self):
        # Esperamos 10 segundos hasta que la función Lambda de True
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element('id', 'select-language').get_attribute('length') == '3')       
        
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()
        account.click()



    def test_create_new_customer(self):
        self.driver.find_element(By.LINK_TEXT,'ACCOUNT').click()
        
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))


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
