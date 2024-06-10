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

#Sirve para poder correr el que queramos, o bien todos menos uno y asi.. (-m es de los mark, los -s y -v son otra csa)
#Cómo correr el/los tests >>>

#pytest PyTest_Mark.py -s -v -m seis
#pytest PyTest_Mark.py -s -v -m "not seis"

@pytest.mark.uno
def test_uno():
    print("Test uno")

@pytest.mark.dos
def test_dos():
    print("Test dos")

@pytest.mark.tres
def test_tres():
    print("Test tres")

@pytest.mark.cuatro
def test_cuatro():
    print("Test cuatro")

@pytest.mark.cinco
def test_cinco():
    print("Test cinco")

@pytest.mark.seis
def test_seis():
    print("Test seis")