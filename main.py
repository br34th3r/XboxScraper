from sys import platform
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("/Users/joshboddy/Downloads/chromedriver", options=chrome_options)
driver.get("https://www.xbox.com/en-GB/consoles/xbox-series-x")
outOfStock = True

while(outOfStock):
    try:
        driver.refresh()
        html = driver.page_source
        soup = BeautifulSoup(html, features='lxml')
        stocks = soup.find_all('span', class_="retline retstockbuy")
        for retailer in stocks:
            if(retailer.span.text != "OUT OF STOCK"):
                print("Back in Stock")
                outOfStock = False
    except ValueError:
        print("Page Structure has changed, please restructure code, but could mean that they've come back in stock, go and take a look")

driver.quit()

if(platform == "darwin"):
    os.system("open https://www.xbox.com/en-GB/consoles/xbox-series-x")
elif(platform == "win32"):
    os.system("explorer https://www.xbox.com/en-GB/consoles/xbox-series-x")