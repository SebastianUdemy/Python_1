import time
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
driver=""
f=""

# IMPORTANTE... ef setup_function(function): SIEMPRE LAS DOS PALABRAS DEBEN SER =
#Todos los tests que tengamos van a hacer esto al principio de c/u de ellos.
def setup_function(function):
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    f=Funciones_Globales(driver)
    #esta parte del login la metimos aca porque se repetirian en todos nuestros tests de abajo (hice 1 solo)
    f.Texto_Mixto("xpath", "(//input[contains(@data-val,'true')])[1]", "admin@yourstore.com", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Iniciando nuestros Test")

#Al final de c/u de ellos haran esto.
def teardown_function(function):
    print("Fin de los Tests")
    driver.close()


def test_uno():
    f.Click_Mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'SearchProductName')]","computer", t)
    f.Click_Mixto("xpath", "//button[contains(@id,'search-products')]", t)

def test_dos():
    #NO se encuentran elementos. 
    f.Click_Mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Click_Mixto("xpath", "//a[@href='/Admin/Product/Create']", t)
    f.Texto_Mixto("xpath", "//input[@id='Name']","Nombre del Producto", t)
    f.Texto_Mixto("xpath", "//textarea[contains(@id,'ShortDescription')]","Descripcion CORTA", t)
    f.Texto_Mixto("xpath", "//textarea[contains(@id,'ShortDescription')]","Descripcion CORTA", t)