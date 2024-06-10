import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains

class Funciones_Globales():

    #Inicializa la clase 
    def __init__(self,driver):
        self.driver = driver

    #Funcion que se usa en >>> Introduccion.py
    def saludos(self):
        print("Bienvenidos a Page Object Model")

    #Funcion que se usa en >>> Funcion Time.py
    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t
    
    #Funcion que se usa en >>> Funcion Navegar.py
    def Navegar(self,Url, tg):
        self.driver.get(Url)
        self.driver.maximize_window() 

    #Funcion que se usa en >>> Funcion Texto con Xpath.py
    def Texto_Xpath(self, xpath, texto, Tiempo):
        val=self.driver.find_element(By.XPATH, xpath)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(Tiempo)
        return
    
    #Funcion que se usa en >>> Funcion Texto con Xpath.py
    def Texto_Xpath_Valida(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
            val.clear()
            val.send_keys(texto)
            #Buena practica de respuesta
            print("Escribiendo en el campo {} el texto {} >>".format(xpath, texto))
            t = time.sleep(tiempo)
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)

    #Funcion que se usa en >>> Funcion Clic.py
    def Clic_Xpath_Valida(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)
            return t
        
    #Funcion que se usa en >>> NO LA USAMOS PORQUE ES IGUAL QUE LA DE ARRIBBA PERO CON ID 
    def Clic_ID_Valida(self, id, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, id)))
            #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + id)
            return t

    def Salida(self):
        print("Se termina la prueba exitosamente")


    def Select_Xpath_Text(self, xpath, text, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
            val=self.driver.find_element(By.XPATH, xpath)
            t = time.sleep(tiempo)
            val=Select(val)
            val.select_by_visible_text(text)
            print("El campo seleccionado es {} ".format(text))
            t=time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)
            return t

    #Es la funcion mejorada de arriba.
    def Select_Xpath_Type(self, xpath, tipo, dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
            val=self.driver.find_element(By.XPATH, xpath)
            t = time.sleep(tiempo)
            val=Select(val)
            if (tipo=="text"):
                val.select_by_visible_text(dato)
            elif(tipo=="index"):
                val.select_by_index(dato)
            elif(tipo=="value"):
                val.select_by_value(dato)
            print("El campo seleccionado es {} ".format(dato))
            t=time.sleep(tiempo)
            return t   
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento " + xpath)
            return t

    #Funcion que se usa en >>> Funcion Upload_file.py
    def Upload_Xpath(self, xpath, ruta, tiempo):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val=self.driver.find_element(By.XPATH, xpath)
                val.send_keys(ruta)
                print("Se carga la imagen: {}" .format(ruta))
                t = time.sleep(tiempo)
                return t   
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + xpath)
                return t
            
    #NO se usa pero es igual a la de arriba
    def Upload_ID(self, id, ruta, tiempo):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, id)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val=self.driver.find_element(By.XPATH, id)
                val.send_keys(ruta)
                print("Se carga la imagen: {}" .format(ruta))
                t = time.sleep(tiempo)
                return t   
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + id)
                return t

   #Funcion que se usa en >>> Funcion Check.py
    def Check_Xpath(self, xpath, tiempo):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val=self.driver.find_element(By.XPATH, xpath)
                val.click()
                print("Clic en el campo {}" .format(xpath))
                t = time.sleep(tiempo)
                return t   
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + xpath)
                return t

    #Funcion que se usa en >>> Funcion Check Multiples.py
    def Check_Xpath_Multiples(self, tiempo, *args):
            try:
                 for num in args:
                    val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                    #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                    val=self.driver.find_element(By.XPATH, num)
                    val.click()
                    print("Clic en el campo {}" .format(num))
                    t = time.sleep(tiempo)
                    return t   
            except TimeoutException as ex:
                for num in args:
                    print(ex.msg)
                    print("No se encontró el elemento " + num)
                    







#ESTA FUNCION REEMPLAZADA LAS FUNCIONES Texto_Xpath_Valida Y Texto_ID_Valida  >>> Funcion Texto Mixto.py
    def Texto_Mixto(self, tipo, selector, texto, tiempo):
        if (tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val.clear()
                val.send_keys(texto)
                #Buena practica de respuesta
                print("Escribiendo en el campo {} el texto >> {}".format(selector, texto))
                t = time.sleep(tiempo)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
        elif (tipo=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val.clear()
                val.send_keys(texto)
                #Buena practica de respuesta
                print("Escribiendo en el campo {} el texto >> {}".format(selector, texto))
                t = time.sleep(tiempo)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)

#ESTA FUNCION REEMPLAZADA LAS FUNCIONES Click_ID Y Clic_Xpath >>> Funcion Clic Mixto.py
    def Click_Mixto(self, tipo, selector, tiempo):
        if (tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val.click()
                #Buena practica de respuesta
                print("Dando clic en: {}".format(selector))
                t = time.sleep(tiempo)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
        elif (tipo=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val.click()
                print("Dando clic en: {}".format(selector))
                t = time.sleep(tiempo)
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)


    
    def Existe(self, tipo, selector, tiempo):
        if (tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val.click()
                #Buena practica de respuesta
                print("Dando clic en: {}".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return "No Existe"
        elif (tipo=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                #ir=self.driver.execute_script("arguments[0].scrollIntoView();",ir) 
                val.click()
                print("Dando clic en: {}".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return "No Existe"

    #Selecciona Xpath
    def SEX(self, elemento):
        val=WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val=self.driver.execute_script("arguments[0].scrollIntoView();",val) 
        val=self.driver.find_element(By.XPATH, elemento)
        return val
    
    #Selecciona ID
    def SEI(self, elemento):
        val=WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val=self.driver.execute_script("arguments[0].scrollIntoView();",val) 
        val=self.driver.find_element(By.ID, elemento)
        return val
    
    #Se usa en ClickDerecho.py
    def Mouse_Derecho(self, tipo, selector, tiempo=.2):
        if (tipo=="xpath"):
            try:
                val=self.SEX(selector)
                act=ActionChains(self.driver) 
                act.context_click(val).perform()
                print("Click derecho en: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return t
        elif (tipo=="id"):
            try:
                val=self.SEI(selector)
                act=ActionChains(self.driver) 
                act.context_click(val).perform()
                print("Click derecho en: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return "No Existe"
            
    #Se usa en Drag and Drop.py 
    def Drag_And_Drop(self, tipo, selector, destino, tiempo=.2):
        if (tipo=="xpath"):
            try:
                val=self.SEX(selector)
                val2=self.SEX(destino)
                act=ActionChains(self.driver) 
                act.drag_and_drop(val, val2).perform()
                print("Se solto el elemento: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return t
        elif (tipo=="id"):
            try:
                val=self.SEI(selector)
                val2=self.SEI(destino)
                act=ActionChains(self.driver) 
                act.drag_and_drop(val, val2).perform()
                print("Se soltó el elemento: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return "No Existe"
            

    #Se usa en Drag_and_DropXY.py 
    def Mouse_DragDropXY(self, tipo, selector, x, y, tiempo=.2):
        if (tipo=="xpath"):
            try:
                self.driver.switch_to.frame(0) #Agarra el primer Iframe de la pagina, se puede hace muchas veces
                val=self.SEX(selector)
                act=ActionChains(self.driver) 
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se solto el elemento: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return t
        elif (tipo=="id"):
            try:
                self.driver.switch_to.frame(0)  #Agarra el primer Iframe de la pagina, se puede hace muchas veces
                val=self.SEI(selector)
                act=ActionChains(self.driver) 
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se soltó el elemento: {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return "No Existe"


    #Se usa en Drag_and_DropXY.py 
    def ClickXY(self, tipo, selector, x, y, tiempo=.2):
        if (tipo=="xpath"):
            try:
                #self.driver.switch_to.frame(0) #Agarra el primer Iframe de la pagina, se puede hace muchas veces
                val=self.SEX(selector)
                act=ActionChains(self.driver) 
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento {} coornedada {}, {}".format(selector,x , y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return t
        elif (tipo=="id"):
            try:
                #self.driver.switch_to.frame(0)  #Agarra el primer Iframe de la pagina, se puede hace muchas veces
                val=self.SEI(selector)
                act=ActionChains(self.driver) 
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click al elemento {} coornedada {}, {}".format(selector,x , y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento " + selector)
                return "No Existe"
    



