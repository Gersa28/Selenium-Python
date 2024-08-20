import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class HomePageTests(unittest.TestCase):

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

    def test_search_text_field(self):
        search_fields = self.driver.find_element("id",'search')
    
    def test_search_text_field_by_name(self):
        self.driver.find_element("name", "q")
    
    def test_search_text_field_by_class_name(self):
        self.driver.find_element("class name", "input-text")
    
    def test_search_button_enabled(self):
        # Verificamos que un botón esté disponible
        button = self.driver.find_element("class name", "button")
    
    def test_count_of_promo_banner_images(self):
        # Encuentra el elemento de la lista de banners
        banner_list = self.driver.find_element("class name", 'promos')
        # Encuentra todos los elementos <img> dentro del banner_list
        banners = banner_list.find_elements("tag name", 'img')
        print(f"Number of banners found: {len(banners)}")
        for index, banner in enumerate(banners):
            print(f"Banner {index + 1}: {banner.get_attribute('src')}")
        # Verifica que el número de banners sea igual a 3
        self.assertEqual(3, len(banners))

    
    def test_vip_promo(self):
        """
        Verifica la presencia del elemento VIP promo en la página usando XPath.
        """
        # Encuentra el elemento VIP promo usando el localizador XPath
        vip_promo = self.driver.find_element("xpath", '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/ul/li[1]/a/img')
        # Aquí puedes agregar aserciones o verificaciones adicionales si es necesario
        print("VIP promo element found:", vip_promo)

    def test_shopping_cart(self):
        """
        Verifica la presencia del ícono del carrito de compras usando un selector CSS.
        """
        # Encuentra el ícono del carrito de compras usando el selector CSS
        shopping_cart_icon = self.driver.find_element("css selector", 'div.header-minicart span.icon')
        # Aquí puedes agregar aserciones o verificaciones adicionales si es necesario


    @classmethod #El decorador @classmethod indica que el método que sigue es un método de clase y no un método de instancia.
    def tearDownClass(cls): # Acciones para finalizar (Cerrar la ventana del navegador)
        """ Test fixture with the output. """
        cls.driver.quit()

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
