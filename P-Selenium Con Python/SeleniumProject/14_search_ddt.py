import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
import time




def get_data(file_name):
    rows = []
    data_file= open(file_name, 'r')
    reader= csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows


@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver= self.driver
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    @data(*get_data('testdata.csv'))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver= self.driver

        search_field= driver.find_element(By.NAME,'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(By.XPATH,'//h2[@class= "product-name"]/a')
        expected_count= int(expected_count)
        if expected_count>0:
            self.assertEqual(expected_count, len(products))
        else:
            message= driver.find_elements(By.CLASS_NAME,'note-msg')
            self.assertEqual('Your search returns no results.', message)
        print(f'Found {len(products)} products')
        
    def tearDown(self): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        # Agregamos una espera de 15 segundos antes de hacer clic en el botón de registro
        time.sleep(3) 
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(
        verbosity=2, # Imprimir detalles de los resltados de los tests
        # testRunner=HTMLTestRunner( # Para generar los reportes
        #     output='reports', 
        #     report_name='DDT Report')
        )