import sys
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
url='https://google.com'
driver.maximize_window()
driver.get(url)
time.sleep(2)
url2='https://youtube.com'
driver.get(url2)
time.sleep(2)
url3='https://www.youtube.com/channel/UC0sWMgurJhGw4g328xG9gUA'
driver.get(url3)
time.sleep(2)
driver.get(url)
time.sleep(1)
driver.close()
