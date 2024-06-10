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

def get_Data():
    return[
        ("Sebastian", "123123"),
        ("Pedro", "321312"),
        ("Gerardo", "897897")
    ]


@pytest.mark.parametrize("user, clave", get_Data())
def test_login(user, clave):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f=Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "//input[contains(@class,'oxd-input oxd-input--focus')]", user, t)
    f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", clave, t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("Entrando al Sistema")

def teardown_function():
    print("Salida del test")
    driver.close()