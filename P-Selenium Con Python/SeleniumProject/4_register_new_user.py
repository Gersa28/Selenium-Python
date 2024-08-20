import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class RegisterNewUser(unittest.TestCase):

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

    @classmethod #El decorador @classmethod indica que el método que sigue es un método de clase y no un método de instancia.
    def tearDownClass(self): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        self.driver.quit()

    def test_new_user(self):
        driver = self.driver
        # Encontrar elemento por xpath y hacer Click para desplegar, para seleccionar la opción Login        
        driver.find_element('xpath','/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click() 
        driver.find_element('link text','Log In').click()

        # Dentro del Menú Account Login
        create_account_button = driver.find_element('xpath','//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
            #Validamos que el botón esté habilitado con un assertion
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        # Verificamos si estamos dentro del sitio de Creación de cuentas, usamos el título de la pestaña
        self.assertEqual('Create New Customer Account', driver.title)

        # Fomulario
        first_name = driver.find_element(By.ID, 'firstname')
        middlename = driver.find_element(By.ID,'middlename')
        last_name = driver.find_element(By.ID,'lastname')
        email_address = driver.find_element(By.ID,'email_address')
        news_letter_subscription = driver.find_element(By.ID,'is_subscribed')
        password = driver.find_element(By.ID,'password')
        confirm_password = driver.find_element(By.ID,'confirmation')
        submit_button = driver.find_element('xpath','//*[@id="form-validate"]/div[2]/button/span/span')

        # Comprobamos si los elementos están habilitados
        self.assertTrue(
        first_name.is_enabled()
        and middlename.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled()
        )

        # Ingresamos los datos al formulario
        first_name.send_keys('Test')
        driver.implicitly_wait(5)
        middlename.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('arqcftlothxuknlxkt@awdrt.com') #sacado de 10-minute mail
        password.send_keys('Test')
        confirm_password.send_keys('Test')

        # Agregamos una espera de 15 segundos antes de hacer clic en el botón de registro
        time.sleep(10)  

        submit_button.click()



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
