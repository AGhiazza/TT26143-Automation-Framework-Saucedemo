from selenium.webdriver.common.by import By 

def agregar_al_carrito(driver, numProd): #Función para agregar un producto al carrito, numProd recibe el numero del indice para elegir cual producto agregar.
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item") #guarda todos los productos como lista usando find_elements en la variable "productos"
    producto = productos [numProd] #de la lista de productos guarda el producto segun el indice recibido
    anadirCarrito = producto.find_element(By.CLASS_NAME, "btn_inventory") #busca el elemento del boton de añadir al carrito
    anadirCarrito.click()   #clickea el boton

def ir_al_carrito(driver): #función para clickear en el botón de ir al carrito
    botonCarrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link") #busca el botón para ir al carrito
    botonCarrito.click()