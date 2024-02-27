import os
from dotenv import load_dotenv
from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pickle
import sys
import json

# 加载环境变量
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 确保API密钥已设置
if api_key is None:
    sys.exit("请在.env文件中设置OPENAI_API_KEY。")

# 初始化OpenAI客户端
base_url = "https://api.link-ai.chat/v1/"
default_headers = {"x-foo": "true"}
client = OpenAI(api_key=api_key, base_url=base_url, default_headers=default_headers)

# 微博内容生成函数
def generate_weibo_post(theme):
    prompt = {
        "role": "system",
        "content": "你是一个微博机器人，需要帮助用户生成微博，有以下要求：生成的微博内容需要包含主题，且内容满300个字汉字。微博内容的语气要风趣幽默，不要使用任何emoji。不要使用markdown语法。"
    }
    messages = [prompt, {"role": "user", "content": f'帮我生成一篇300字关于"{theme}"的微博。最后需要有 #fox-gpt# 的标签。'}]
    response = client.chat.completions.create(model="gpt-4", messages=messages)
    return response.choices[0].message.content

def post_weibo_with_selenium(content):
    chromedriver_path = './chromedriver'
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    
    # 打开微博
    driver.get('https://weibo.com') 
    time.sleep(3)
    
    # 加载cookies
    cookies = pickle.load(open("weibo_cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    
    # 刷新页面
    driver.refresh()
    time.sleep(3)
    
    # 显式等待页面加载和元素出现
    wait = WebDriverWait(driver, 10)
    weibo_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/main/div[1]/div/div/div[1]/div/div[1]/div/textarea')))
    
    # 使用 json.dumps 来转义 content 字符串中的所有特殊字符
    content_escaped = json.dumps(content)
    
    # 构建 JavaScript 执行脚本，确保双引号被正确转义
    input_script = f"arguments[0].value = {content_escaped};"
    # 替换转义的双引号为实际的双引号
    input_script = input_script.replace(r'\"', '"')
    driver.execute_script(input_script, weibo_input)

    # 触发输入框的 input 事件
    input_event_script = "arguments[0].dispatchEvent(new InputEvent('input', { bubbles: true }));"
    driver.execute_script(input_event_script, weibo_input)

    # 等待发送按钮变为可点击状态
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/main/div[1]/div/div/div[1]/div/div[4]/div/div[4]/button')))
    send_button.click()
    # 等待发送完成
    time.sleep(10)
    
    # 关闭浏览器
    driver.quit()

# 主脚本逻辑
def main():
    while True:
        theme = input("请输入需要生成的微博主题: ")
        weibo_post = generate_weibo_post(theme)
        print("生成的微博博文:")
        print(weibo_post)
        confirm = input("确认内容吗？(Y/N/R): ").strip().lower()
        if confirm == 'y':
            post_weibo_with_selenium(weibo_post)
            print("微博已发送。")
            break
        elif confirm == 'r':
            continue
        elif confirm == 'n':
            print("退出。")
            sys.exit()
        else:
            print("无效输入，请输入Y、N或R。")
            continue

if __name__ == "__main__":
    main()