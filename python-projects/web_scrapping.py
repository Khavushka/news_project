'''
Web scrapping involves extracting data from websites, and it is a valiable skill in various domains. In this project, you will use Python and the BeautifulSoup library to scrape data from a website of your chice. you will learn how to navigate HTML structures, extract specific information, and save it to a file or a database.
'''

import requests
from bs4 import BeautifulSoup

url = "http://dkexit.eu/sduwebudv23/site/ch09s03.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.text
paragraphs = soup.find_all("p")

print("Title: ", title)
print("Paragraphs: ")
for p in paragraphs:
    print(p.text)