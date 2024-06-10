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


@pytest.mark.run
def test_1():
    print("Primer test")
    assert True

@pytest.mark.run
def test_2():
    a=10
    b=10
    assert a==b, "No son iguales"

@pytest.mark.run
def test_3():
     a=5
     b=10
     assert a==b, "No son iguales"

@pytest.mark.run
def test_4():
     a=15
     b=10
     assert a>b, "A no es mayor que B"