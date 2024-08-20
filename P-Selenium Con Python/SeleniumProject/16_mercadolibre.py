import unittest
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException

class NewClass(unittest.TestCase):

    def setUp(self):
        """ Test fixture to prepare everything. """
        # Use the ChromeDriverManager to automatically handle the path to chromedriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('https://www.mercadolibre.com/')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        # 1 Identificar el país
        country = driver.find_element(By.ID,'CO')        
        country.click()
        time.sleep(2)

        # 2 Nos ubicamos en la Barra de Búsqueda y buscamos 'playstation 4'
        search_field = driver.find_element(By.NAME,'as_word')
        search_field.click() # Nos ubicanmos en la barra de búsqueda
        time.sleep(2)
        search_field.clear() # Borramos texto presente, por las dudas
        search_field.send_keys('playstation 5')
        search_field.submit()
        time.sleep(2)

        # 3 Aplicamos filtro de ubicación
        location = driver.find_element("partial link text", "Bogotá D.C.")
        driver.execute_script("arguments[0].click();", location)
        time.sleep(2)

        # 4 Elegimos la condición de "Nuevo"
        condition = driver.find_element("partial link text", 'Nuevo')
        # condition.click() # Da error, no es necesario
        driver.execute_script("arguments[0].click();", condition)
        time.sleep(2)

        # 5 Ordenar lista de Resultados
        order_menu = driver.find_element('class name', 'andes-dropdown__trigger')
        order_menu.click()
        time.sleep(2)        
        # Localizar el elemento que contiene el texto "Mayor precio"
        higher_price = driver.find_element("xpath", "//span[text()='Mayor precio']")
        # Hacer clic en el elemento
        higher_price.click()
        # Esperar 2 segundos
        time.sleep(2)        


        # 6 Obtén los nombres y precios de los productos        
        products = []        
        try:            
            for i in range(5): # PRECAUCION: i arranca en cero y la lista del XPATH en 1      
                # Espera explícita para asegurarse de que el elemento esté presente y visible
                wait = WebDriverWait(driver, 10)

                element = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/main/div/div[3]/section/ol/li[{i+1}]/div/div/div[2]/a')))
                article_name = element.text  # Una vez que el elemento es encontrado, se puede acceder a su texto o hacer click en él      

                element_precio = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="root-app"]/div/div[3]/section/ol/li[{i+1}]/div/div/div[2]/div[2]')))  
                article_price = element_precio.text      

                products.append((article_name, article_price))   

        except NoSuchElementException as e:
            print(f"Elemento no encontrado: {e}")
        except TimeoutException as e:
            print(f"Tiempo de espera agotado: {e}")        
        except Exception as e:                
            print(f"Error to found the article {i}: {e}")                        
        
        # Imprime los resultados   
        i = 0     
        for name, price in products:    
            i = i + 1        
            print(f"Product {i}: {name} - Price: {price}")

    def tearDown(self):
        time.sleep(10)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
    