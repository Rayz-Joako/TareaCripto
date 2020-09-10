import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#MICHALEPAGE AUTOMATIZACION

def spawn():
    path_to_chromedriver = '/Users/joako/Documents/UDP/Cripto/tarea1/ES/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options, executable_path = path_to_chromedriver)
    return driver

def create_c(name, last_name, mail, passw):#creacion de cuenta
    driver = spawn()
    driver.get("https://www.michaelpage.es/user/register")

    input_name = driver.find_element_by_id("edit-field-first-name-und-0-value")
    input_last_name = driver.find_element_by_id("edit-field-last-name-und-0-value")
    input_mail = driver.find_element_by_id("edit-mail")
    input_conf_mail = driver.find_element_by_id("edit-conf-mail")
    input_pass = driver.find_element_by_id("edit-pass")

    input_name.send_keys(name)
    input_last_name.send_keys(last_name)
    input_mail.send_keys(mail)
    input_conf_mail.send_keys(mail)
    input_pass.send_keys(passw)

    button = driver.find_element_by_xpath("//input[@id='edit-privacy-data-1']")
    driver.execute_script("arguments[0].click();", button)

    login_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Inscríbete']")[0]
    driver.execute_script("arguments[0].click();", login_button)

def login(mail, passw):#inicio sesion
    driver = spawn()
    driver.get("https://www.michaelpage.es/mypage")
    input_email = driver.find_element_by_id("edit-name")
    input_pass = driver.find_element_by_id("edit-pass")

    input_email.send_keys(mail)
    input_pass.send_keys(passw)

    login_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Iniciar Sesión']")[0]
    driver.execute_script("arguments[0].click();", login_button)
    return driver

def res_pas(mail):#restablecer password
    driver = spawn()
    driver.get("https://www.michaelpage.es/user/password")

    input_email = driver.find_element_by_id("edit-name")

    input_email.send_keys(mail)

    send_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Enviar']")[0]
    driver.execute_script("arguments[0].click();", send_button)

def mod_pas(mail,passw,new_pass):#modificar password
    driver = login(mail, passw)

    time.sleep(5)
    driver.get("https://www.michaelpage.es/mypage/account-settings?source=saved-jobs")

    input_pass = driver.find_element_by_id("edit-current-pass")
    input_new_pass = driver.find_element_by_id("edit-pass")

    input_pass.send_keys(passw)
    input_new_pass.send_keys(new_pass)

    mod_button = driver.find_elements_by_xpath("//input[@type='submit' and @value='Confimar los cambios']")[0]
    driver.execute_script("arguments[0].click();", mod_button)

