'''
LinkedIn Posts Scrapping 
'''

# Rediscover driver settings
# used 'detach' to keep the chrome window open after running, and window size to extend the window.

from options import Options
from selenium import webdriver

options = Options()
options.add_experimantal_option("detach", True)
driver = webdriver.Chrome("chromedriver", options=options)
driver.set_window_size(1400, 1400)

# Improving code readability
# WebDriverWait component from the Selenium library, to make code cleaner

wait = WebDriverWait(driver, 20)

# define some functions
def click(path):
    wait.until(EC.element_to_be_clickable((By.XPATH, psth))).click()


