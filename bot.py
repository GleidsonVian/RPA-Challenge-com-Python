from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pyautogui as ptg


driver = webdriver.Chrome()

driver.get("https://www.rpachallenge.com/")
driver.maximize_window()

time.sleep(5)

start = driver.find_element(By.XPATH, '//button[@class="waves-effect col s12 m12 l12 btn-large uiColorButton"]')
start.click()

excel = pd.read_excel(r'C:\pasta4\Python\rpa challenge\challenge.xlsx')
df = pd.DataFrame(excel)



for indice, linha in df.iterrows():
    first_name = df.iloc[indice, 0]
    last_name = df.iloc[indice, 1]
    company_name = df.iloc[indice, 2]
    role_in_company = df.iloc[indice, 3]
    adress = df.iloc[indice, 4]
    email = df.iloc[indice, 5]
    phone_number = df.iloc[indice, 6]
    
    time.sleep(0.5)
    
    try:
        campo_nome = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
        campo_nome.send_keys(first_name)
        time.sleep(0.2)
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    
    try:
        campo_sobrenome = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
        campo_sobrenome.send_keys(last_name)
        time.sleep(0.2)
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    
    try:
        campo_empresa = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
        campo_empresa.send_keys(company_name)
        time.sleep(0.2)
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    
    try:
        campo_cargo = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
        campo_cargo.send_keys(role_in_company)
        time.sleep(0.2)
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    
    try:
        campo_endereco = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
        campo_endereco.send_keys(adress)
        time.sleep(0.2)
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    
    try:
        campo_email = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
        campo_email.send_keys(email)
        time.sleep(0.2)
    except Exception as e:
        print(f'Ocorreu um erro {e}')
        
    try:
        campo_telefone = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
        campo_telefone.send_keys(int(phone_number))
        time.sleep(0.2)
    except Exception as e:
        print(f'Ocorreu um erro {e}')
    
    try:
        submit = driver.find_element(By.XPATH, "//input[@class='btn uiColorButton']")
        submit.click()
        time.sleep(1)
    except Exception as e:
        print(f'Ocorreu um erro {e}')

    
foto = ptg.screenshot()
foto.save(r'C:\pasta4\Python\rpa challenge\foto.png')


