import time
import pytest
import allure

from allure_commons.types import AttachmentType

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

#Para imagenes de error // NO SACA LA CAPTURA DE ERROR NOSE PORQUE. 

#Esto va para que funcione el scrypt de captura de error.
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.maximize_window()
    f=Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "(//input[contains(@data-val,'true')])[1]", "admin@yourstore.com", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Entrando al Sistema")
    yield #cumple la funcion del teardown_function
    print("Salida del login 1")
    driver.close()

@pytest.fixture(scope='module')
def setup_login_dos():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    f=Funciones_Globales(driver)
    #esta parte del login la metimos aca porque se repetirian en todos nuestros tests de abajo (hice 1 solo)
    f.Texto_Mixto("xpath", "//input[contains(@class,'oxd-input oxd-input--focus')]", "Admin", t)
    f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", t)
    print("Entrando al Sistema")
    yield #cumple la funcion del teardown_function
    print("Salida del login 2")

########################################################################################

@pytest.mark.usefixtures("log_on_failure") #se le pone a cada test
@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando al sistema 1")
    f.Click_Mixto("xpath", "//a[@href='#'][contains(.,'Customers')]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Customers')])[2]", t)
    f.Texto_Mixto("xpath", "//input[contains(@id,'SearchFirstName')]", "victoria", t)
    allure.attach(driver.get_screenshot_as_png(), name="buscando_nombre", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//button[contains(@id,'search-customers')]", 5)
    #Aca saca SCREN >> en NAME se pone el que quieras. 
    allure.attach(driver.get_screenshot_as_png(), name="customers", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//a[@href='/Admin/Customer/Create']", t)
    email=driver.find_element(By.XPATH, "//input[contains(@id,'Email')]")
    email.send_keys("Email@123.com" + Keys.TAB + "contraseña" + Keys.TAB + "Sebas" + Keys.TAB + "Regini")
    allure.attach(driver.get_screenshot_as_png(), name="datos", attachment_type=AttachmentType.PNG)
    time.sleep(2)
    f.Click_Mixto("id", "Gender_Female", t)
    assert 1==2 #lo hacemos fallar a proposito
    
    
@pytest.mark.usefixtures("log_on_failure") #se le pone a cada test
@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando al sistema 2")
    f.Click_Mixto("xpath", "//a[@href='/web/index.php/admin/viewAdminModule']", t)
    f.Click_Mixto("xpath", "//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'User Management')]", t)
    allure.attach(driver.get_screenshot_as_png(), name="items", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "(//li[contains(.,'Users')])[2]", t)
    assert 1==2 #lo hacemos fallar a proposito