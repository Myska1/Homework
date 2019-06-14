import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



browser = webdriver.Firefox(executable_path=r"C:\Users\pf932\Homework\geckodriver.exe")
browser.get('https://regrephub-sit.deutsche-boerse.de/transactions/')





