import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales
from selenium.webdriver import ActionChains

t=1


@pytest.fixture(scope='module')
def setup_login():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f=Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "//input[contains(@class,'oxd-input oxd-input--focus')]", "Admin", t)
    f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("Entrando al Sistema")

def tearndown_function():
    print("Fin de todos los tests")
    driver.close()


@pytest.mark.login #Comienza con la version login. LO IDENTIFICA (CREO)
@pytest.mark.usefixtures("setup_login") #Agarra el setup_login de arriba
def test_uno():
    etiqueta=f.SEX("//header/div[1]/div[1]/span[1]/h6[1]").text
    print(etiqueta) #imprime lo que validamos arriba. 
    if(etiqueta=="Dashboard"):
        print("##############\n")
        print("Estas en la pagina de inicio")
        print("##############\n")
        assert etiqueta=="Dashboard"
    else:
        #Esto asi va a pasar siempre porque el assert es valido.... por lo que ESTA MAL.    
        assert etiqueta=="Dashboard", "No pudiste entrar al sistema"
