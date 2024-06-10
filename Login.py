from selenium import webdriver

from Funciones.Funciones import Funciones_Globales

tg=2

#Todo esto como el test de abajo pueden ir en funciones... y unicamente los llamas y listo. 
def test_login1():
    global driver
    driver = webdriver.Chrome()

    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", tg)
    driver.maximize_window()
    f.Texto_Mixto("xpath", "(//input[contains(@data-val,'true')])[1]", "asd@gmail.com", tg)
    f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", "contraseña", tg)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", tg)
    e1=f.SEX("//div[contains(@class,'message-error validation-summary-errors')]")
    e1=e1.text

    if(e1=="Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect"):
         print("Prueba de Email Exitosa")
    else: 
        print("La prueba de Email NO es Exitosa")
    driver.close()



def test_login2():
    global driver
    driver = webdriver.Chrome()

    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", tg)
    driver.maximize_window()
    f.Texto_Mixto("xpath", "(//input[contains(@data-val,'true')])[1]", "", tg)
    f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", "contraseña", tg)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", tg)
    e1=f.SEX("//span[contains(@id,'Email-error')]")
    e1=e1.text

    if(e1=="Please enter your email"):
        print("Prueba de Validacion Exitosa")
    else: 
        print("La prueba de Validacion NO es Exitosa")
    driver.close()