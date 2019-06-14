import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"/Users/myska/Documents/Python/Homework/chromedriver")
browser.get('http://www.impuls.cz/souteze/hti-milionovy-zavod/')

email = browser.find_element_by_id("email")
email.send_keys("lucinka.cepakova@gmail.com")

name = browser.find_element_by_id("name1")
name.send_keys("Lucie")

surname = browser.find_element_by_id("name2")
surname.send_keys("Cepáková")

age = browser.find_element_by_id("age")
age.send_keys("33")

zipcode = browser.find_element_by_id("zipcode")
zipcode.send_keys("19000")

browser.find_element_by_xpath("//select[@name='pohlavi']/option[text()='Žena']").click()

phone = browser.find_element_by_id("phone")
phone.send_keys("773641618")

filtr5 = browser.find_element_by_id('submit').click()

time.sleep(15)
browser.quit()


