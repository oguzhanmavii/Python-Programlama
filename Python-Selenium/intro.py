
import sys
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
url='https://github.com/oguzhanmavii'
driver.get(url)