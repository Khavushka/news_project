'''
LinkedIn Posts Scrapping 
LINK: https://medium.com/@hugo.torche/linkedin-posts-scraping-with-python-1d8eeeb5bea4
'''

# Rediscover driver settings
# used 'detach' to keep the chrome window open after running, and window size to extend the window.

from options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json

options = Options()
options.add_experimantal_option("detach", True)
driver = webdriver.Chrome("chromedriver", options=options)
driver.set_window_size(1400, 1400)

# Improving code readability
# WebDriverWait component from the Selenium library, to make code cleaner

wait = WebDriverWait(driver, 20)

# define some functions
def click(path):
    wait.until(EC.element_to_be_clickable((By.XPATH, path))).click()
    
def send_keys(path, *args):
    for arg in args:
        wait.until(EC.presence_of_element_located((By.XPATH, path))).send_keys(arg)
        

# Dealing with credentials
linkedin_credentials = json.load(open("LinkedIn/linkedin_credentials.json"))
username = linkedin_credentials['username']
password = linkedin_credentials['password']

# Object oriented programming
# search word
search_bar_path = "/html/body/div[6]/header/div/div/div/div[1]/input"
send_keys(search_bar_path, word, Keys.RETURN)


# LinkedIn structure
# will include 10 posts
# scroll down to bottom 
x = 0
while x < ((number_of_posts/10)):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    x = x + 1
    
    # Date conversion
    
    import js2py

    # copyright: https://github.com/Ollie-Boyd/Linkedin-post-timestamp-extractor
    js_function = js2py.eval_js( """function extractUnixTimestamp(postId) {
    const asBinary = postId.toString(2);
    const first41Chars = asBinary.slice(0, 41);
    const timestamp = parseInt(first41Chars, 2);
    const dateObject = new Date(timestamp);
    const humanDateFormat = dateObject.toUTCString();
    return humanDateFormat;
    }""" )