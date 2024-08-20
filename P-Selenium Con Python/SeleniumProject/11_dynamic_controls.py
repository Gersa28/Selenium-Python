import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewClass(unittest.TestCase):

    @classmethod# Para que las pruebas corran en una sola ventana sin cerrar tras cada test y reemplazamos self pro cls
    def setUpClass(cls): # Ejecuta todo lo necesario antes de hacer una prueba
        """ Test fixture to prepare everything. """
        # Use the ChromeDriverManager to automatically handle the path to chromedriver
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()
        driver.maximize_window()

    @classmethod #El decorador @classmethod indica que el método que sigue es un método de clase y no un método de instancia.
    def tearDownClass(cls): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        # Agregamos una espera de 15 segundos antes de hacer clic en el botón de registro
        time.sleep(10) 
        cls.driver.quit()

    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]') # Usamos el Selector CSS
        checkbox.click()

        remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click()

        # Condición esperada
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')))
        remove_add_button.click()

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
        text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('Texto Insertado')

        enable_disable_button.click()



if __name__ == '__main__':
    unittest.main(
        verbosity=2, # Imprimir detalles de los resltados de los tests
        testRunner=HTMLTestRunner( # Para generar los reportes
            output='reports', 
            report_name='Test Results')
        )
    
'''
@classmethod Decorador:
El decorador @classmethod indica que el método que sigue es un método de clase y 
no un método de instancia.
Los métodos de clase reciben la clase en sí como el primer argumento, en lugar de 
una instancia de la clase. Este primer argumento es convencionalmente llamado cls, 
en lugar de self, que es lo que se usa en los métodos de instancia.
'''
