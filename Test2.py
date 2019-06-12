import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_load(text_to_wait, by=By.LINK_TEXT):
    delay = 3  # seconds
    try:
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((by, text_to_wait)))

    except TimeoutException:
        print("Loading took toomuch time!")
        raise


browser = webdriver.Chrome(executable_path=r"C:\Users\pf932\Homework\chromedriver.exe")
browser.get('https://www.alza.cz/')
wait_load('Elektromobilita')

filt6 = browser.find_element_by_link_text('Elektromobilita').click()
time.sleep(3)
filt5 = browser.find_element_by_link_text('Elektromobily').click()
time.sleep(3)
#filtr for set up from highest price to low
filtr = browser.find_element_by_link_text('Od nejdražšího').click()
time.sleep(3)
#filter for choose only items only in stock
filtr2 = browser.find_element_by_xpath(".//*[contains(text(), 'Pouze skladem')]").click()
time.sleep(3)
buyMostExpensive = browser.find_element_by_link_text("Koupit").click()
time.sleep(3)
back = browser.find_element_by_link_text('Zpět ke zboží').click()
time.sleep(3)
filt3 = browser.find_element_by_link_text('Od nejlevnějšího').click()
time.sleep(3)
buyLastExpensive = browser.find_element_by_link_text("Koupit").click()
time.sleep(3)
filt4 = browser.find_element_by_id('basket').click()
time.sleep(5)
browser.save_screenshot('basket.png')


browser.quit()