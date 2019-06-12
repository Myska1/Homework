import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path=r"C:\Users\pf932\Homework\chromedriver.exe")
browser.get('https://www.alza.cz/')

filtr = browser.find_element_by_link_text('Elektromobilita').click()
time.sleep(2)
filtr1 = browser.find_element_by_link_text('Elektromobily').click()
time.sleep(2)
#filtr for set up from highest price to low
filtr2 = browser.find_element_by_link_text('Od nejdražšího').click()
time.sleep(2)
#filter for choose only items only in stock
filtr3 = browser.find_element_by_xpath(".//*[contains(text(), 'Pouze skladem')]").click()
time.sleep(2)
buyMostExpensive = browser.find_element_by_link_text("Koupit").click()
time.sleep(2)
back = browser.find_element_by_link_text('Zpět ke zboží').click()
time.sleep(3)
filtr4 = browser.find_element_by_link_text('Od nejlevnějšího').click()
time.sleep(2)
buyLeastExpensive = browser.find_element_by_link_text("Koupit").click()
time.sleep(2)
filtr5 = browser.find_element_by_id('basket').click()
time.sleep(5)
browser.save_screenshot('basket.png')


browser.quit()
