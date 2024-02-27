#post_weibo_with_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

# 你的chromedriver的路径
chromedriver_path = './chromedriver'

# 创建WebDriver对象
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# 打开微博
driver.get('https://weibo.com')
time.sleep(3)
# 加载cookies
cookies = pickle.load(open("weibo_cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

# 显式等待页面加载和元素出现
wait = WebDriverWait(driver, 10)
weibo_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/main/div[1]/div/div/div[1]/div/div[1]/div/textarea')))
weibo_input.send_keys('这是通过Selenium自动发送的微博内容')
time.sleep(2)
send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/main/div[1]/div/div/div[1]/div/div[4]/div/div[4]/button')))
send_button.click()
time.sleep(2)
# 关闭浏览器
driver.quit()