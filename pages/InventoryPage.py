from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from pages.BasePage import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        #Selectores
        self.item_list = (By.CLASS_NAME, "inventory_list") 
        self.item_details = (By.CLASS_NAME, "inventory_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.item_img = (By.CLASS_NAME, "inventory_item_img")
        self.add_to_cart = (By.CLASS_NAME, "btn_inventory")
        self.sort = (By.CLASS_NAME, "product_sort_container")  #Boton de ordenamiento es un <select> de HTML

    # Métodos ícono ordenar (sort)

    def obtener_ordenar(self):
        return self.driver.find_element(*self.sort)

    def ordenar(self, criterio):
        # Valores disponibles: "az" (A-Z), "za" (Z-A), "lohi" (precio menor a mayor), "hilo" (precio mayor a menor)
        botonOrdenar = self.driver.find_element(*self.sort)
        Select(botonOrdenar).select_by_value(criterio)

    # Métodos para productos

    def obtener_productos(self):
        return self.driver.find_elements(*self.item_details)
        
    def obtener_nombre_producto(self, numProd):
        productos = self.driver.find_elements(*self.item_details)
        producto = productos[numProd]
        return producto.find_element(*self.item_name).text

    def obtener_descripcion_producto(self, numProd):
        productos = self.driver.find_elements(*self.item_details)
        producto = productos[numProd]
        return producto.find_element(*self.item_desc).text

    def obtener_precio_producto(self, numProd):
        productos = self.driver.find_elements(*self.item_details)
        producto = productos[numProd]
        return producto.find_element(*self.item_price).text

    def agregar_al_carrito(self, numProd): #Función para agregar un producto al carrito, numProd recibe el numero del indice para elegir cual producto agregar.
        productos = self.driver.find_elements(*self.item_details)
        producto = productos [numProd] #de la lista de productos guarda el producto segun el indice recibido
        producto.find_element(*self.add_to_cart).click()

    def agregar_producto_por_nombre(self, nombre_producto_json):
        productos = self.driver.find_elements(*self.item_details)
        for producto in productos:
            nombre = producto.find_element(*self.item_name).text
            if nombre == nombre_producto_json:
                producto.find_element(*self.add_to_cart).click()
                break

    # Métodos para carrito

    def obtener_badge_carrito(self):
        return self.driver.find_element(*self.cart_badge)

