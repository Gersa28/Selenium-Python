import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.common.by import By 



class AddRemoveElements(unittest.TestCase):

    @classmethod# Para que las pruebas corran en una sola ventana sin cerrar tras cada test y reemplazamos self pro cls
    def setUpClass(cls): # Ejecuta todo lo necesario antes de hacer una prueba
        """ Test fixture to prepare everything. """
        # Use the ChromeDriverManager to automatically handle the path to chromedriver
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        driver = cls.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    @classmethod #El decorador @classmethod indica que el método que sigue es un método de clase y no un método de instancia.
    def tearDownClass(cls): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        # Agregamos una espera de 15 segundos antes de hacer clic en el botón de registro
        time.sleep(10) 
        cls.driver.quit()

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many elements will you add?: ')) # Pregunta por consola
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element('xpath', '//*[@id="content"]/div/button')

        time.sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element('xpath', '//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements than existent")
                break
        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are 0 elements on screen")

        time.sleep(3)

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
