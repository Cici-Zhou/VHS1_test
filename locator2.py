#-*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://192.168.0.58:1337/login.html")

locator_username = (By.ID, 'txtUserName')
locator_password = (By.ID, 'txtPassword')
#locator_language = (By.ID, 'dropLanguage')
locator_loginButton = (By.ID, 'btnLogin')

driver.find_element(*locator_username).clear()
driver.find_element(*locator_username).send_keys("13275820900")
driver.find_element(*locator_password).clear()
driver.find_element(*locator_password).send_keys("20900")
driver.find_element(*locator_loginButton).click()

AddUser = driver.find_element(By.XPATH,"//li[@class='mainli'][0]/span").text
print (AddUser)

driver.quit()
