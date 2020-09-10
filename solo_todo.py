import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#SOLOTODO AUTOMATIZACION

def spawn():
    path_to_chromedriver = '/Users/joako/Documents/UDP/Cripto/tarea1/CL/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options, executable_path = path_to_chromedriver)
    return driver
    
def create_c(mail, passw):#creacion de cuenta
    driver = spawn()
    driver.get("https://www.solotodo.cl/account/signup")
    input_email = driver.find_element_by_id("inputEmail")
    input_pass = driver.find_element_by_id("inputPassword1")
    input_confpass = driver.find_element_by_id("inputPassword2")

    input_email.send_keys(mail)
    input_pass.send_keys(passw)
    input_confpass.send_keys(passw)

    reg_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='¡Registrarse!']")[0]
    reg_button.click()

def login(mail, passw):#inicio sesion
    driver = spawn()
    driver.get("https://www.solotodo.cl/account/login")
    input_email = driver.find_element_by_id("exampleInputEmail1")
    input_pass = driver.find_element_by_id("password")

    input_email.send_keys(mail)
    input_pass.send_keys(passw)
    login_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Ingresar']")[0]
    login_button.click()
    return driver

def res_pas(mail):#restablecer password
    driver = spawn()
    driver.get("https://www.solotodo.cl/account/password_reset")

    input_email = driver.find_element_by_id("exampleInputEmail1")

    input_email.send_keys(mail)

    login_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Enviar Correo']")[0]
    login_button.click()

def mod_pas(mail,passw,new_pass):#modificar password
    driver = login(mail, passw)

    time.sleep(5)
    driver.get("https://www.solotodo.cl/account/password_change")

    input_pass = driver.find_element_by_id("inputOldPassword")
    input_new_pass = driver.find_element_by_id("inputPassword1")
    input_confnew_pass = driver.find_element_by_id("inputPassword2")

    input_pass.send_keys(passw)
    input_new_pass.send_keys(new_pass)
    input_confnew_pass.send_keys(new_pass)

    mod_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Enviar']")[0]
    mod_button.click()


