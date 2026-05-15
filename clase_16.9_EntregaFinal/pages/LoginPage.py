from selenium.webdriver.common.by import By 


class LoginPage:     #define la clase que representa la pagina del login
    def __init__(self, driver):     #Constructor: Funcion/metodo que ejectura todo su código automaticamente cuando se crea un objeto de esta clase.
                                    #Self refiere al objeto mismo que se crea con esta clase
        self.driver = driver #Se va a guardar el navegador dentro de la clase.
        
        # Selectores
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        
    def abrir_pagina(self): #funcion que abre el navegador
        self.driver.get("https://www.saucedemo.com/") # .get de selenium para abrir la pagina web

    def ingresar_usuario(self, usuario): #función que ingresa el usuario
        self.driver.find_element(*self.username_input).send_keys(usuario) # En vez de hardcodear el selector, ya lo llama desde la clase LoginPage
                                                       # el puntero o asterisco * es una variable que guarda la dirección de memoria de otra variable, en vez de guardar el valor, guarda la ruta para llegar a ese valor

    













from selenium.webdriver.common.keys import Keys #Keys se usa para oprimir las teclas especiales del teclado. (Enter, Tab, Escape, etc.)



def login(driver):  #esta función recibe el driver desde conftest y realiza el proceso de login en saucedemo
    driver.get("https://www.saucedemo.com/") #abre la pagina web a operar

    #Usuario
    usuario = driver.find_element(By.ID, "user-name")   #find_element busca un elemento de la pagina interactuando con el driver. "By" indica el como (por ID), y entre "" el qué buscar.
    usuario.send_keys("standard_user")    #send_keys envía las "teclas" que apretaria el usuario, en este caso para completar el campo "usuario"

    #Pass
    contrasena = driver.find_element(By.ID, "password") 
    contrasena.send_keys("secret_sauce")

    #Submit
    contrasena.send_keys(Keys.RETURN)     #Keys.RETURN indica que se oprima la tecla (Keys.) ENTER (RETURN)