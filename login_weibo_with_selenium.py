#login_weibo_with_selenium.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

# 你的chromedriver的路径
chromedriver_path = './chromedriver'

# 创建WebDriver对象
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# 手动登录微博并保存cookies
driver.get('https://weibo.com')
time.sleep(60)  # 给足够时间手动登录

# 保存cookies
pickle.dump(driver.get_cookies(), open("weibo_cookies.pkl", "wb"))

driver.quit()