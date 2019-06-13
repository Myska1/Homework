import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#browser = webdriver.Chrome(executable_path=r"C:\Users\pf932\Homework\chromedriver.exe")
browser = webdriver.Chrome(executable_path=r"/Users/myska/Documents/Python/Homework/chromedriver")
browser.get('https://www.alza.cz/')

#selecting a link for Electro mobile cathegory
filtr = browser.find_element_by_link_text('Elektromobilita').click()
time.sleep(3)
#selecting a link for Electro cars cathegory
filtr1 = browser.find_element_by_link_text('Elektromobily').click()
time.sleep(3)
#filtr for setting up items from the most expensive thing
filtr2 = browser.find_element_by_link_text('Od nejdražšího').click()
time.sleep(3)
#filter for choosing only items only in stock
filtr3 = browser.find_element_by_xpath(".//*[contains(text(), 'Pouze skladem')]").click()
time.sleep(3)
#add the most expensive item into the cart
buyMostExpensive = browser.find_element_by_link_text("Koupit").click()
time.sleep(3)
back = browser.find_element_by_link_text('Zpět ke zboží').click()
time.sleep(3)
#filtr for setting up items from the least expensive thing
filtr4 = browser.find_element_by_link_text('Od nejlevnějšího').click()
time.sleep(3)
#add the least expensive item into the cart
buyLastExpensive = browser.find_element_by_link_text("Koupit").click()
time.sleep(3)
#show me items in the basket
filtr5 = browser.find_element_by_id('basket').click()
time.sleep(5)
#printscreen
browser.save_screenshot('basket.png')


browser.quit()
