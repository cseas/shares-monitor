print("URL Lib output:\n\n")

import urllib.request

# test URLs
#url = 'https://www.moneyam.com/share-list_T.html'
url = 'https://udacity.github.io/cs101x/index.html'
#url = 'https://xkcd.com/353/'

print(urllib.request.urlopen(url).read().decode("utf8"))



print("\n\nSelenium output:\n\n")
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://udacity.github.io/cs101x/index.html')
html_source = browser.page_source

print(html_source)

browser.quit()