from selenium.webdriver.common.by import By 
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