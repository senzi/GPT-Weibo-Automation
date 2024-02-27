#weibo_post_generator.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Ensure API key is available
if api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY in the .env file.")

# Instantiate the OpenAI client with the base URL and default headers
base_url = "https://api.link-ai.chat/v1/"
default_headers = {"x-foo": "true"}
client = OpenAI(api_key=api_key, base_url=base_url, default_headers=default_headers)

# Prompt template for Weibo post generation
weibo_bot_prompt = {
    "role": "system",
    "content": "你是一个微博机器人，需要帮助用户生成微博，有以下要求：生成的微博内容需要包含主题，且内容满300个字汉字。微博内容的语气要风趣幽默，不要使用emoji。不要使用markdown语法。"
}

# Function to generate Weibo post
def generate_weibo_post(theme, model="gpt-4"):
    messages = [
        weibo_bot_prompt,
        {
            "role": "user",
            "content": f'帮我生成一篇300字关于"{theme}"的微博。最后需要有 #fox-gpt# 的标签。'
        }
    ]
    response = client.chat.completions.create(model=model,
    messages=messages)
    post_content = response.choices[0].message.content
    return post_content

# Main script logic
if __name__ == "__main__":
    theme = input("请输入需要生成的微博主题: ")
    try:
        weibo_post = generate_weibo_post(theme)
        print("生成的微博博文:")
        print(weibo_post)
    except Exception as e:
        print(f"An error occurred: {e}")