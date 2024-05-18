from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


driver.get('https://www.google.com')



