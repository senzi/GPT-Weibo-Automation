# Automated Weibo Posting Script

## Introduction

This script automates the process of generating and posting content to Weibo using Python, Selenium, and the OpenAI GPT model. It helps users save time while maintaining the humor and originality of Weibo posts.

## Features

- **Automatic Login**: Uses the Selenium library to log in to Weibo accounts automatically.
- **Content Generation**: Utilizes the OpenAI GPT model to generate witty and humorous Weibo content.
- **Posting Tweets**: Automatically posts the generated content to Weibo.
- **Environment Variable Management**: Safely manages API keys and other sensitive information through a `.env` file.

## Quick Start

### Prerequisites

- Python 3.x
- Google Chrome Browser
- ChromeDriver

### Installation Steps

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/senzi/GPT-Weibo-Automation.git
   ```
2. Navigate to the project directory:
   ```
   cd GPT-Weibo-Automation
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create and edit the `.env` file, adding your OpenAI API key:
   ```
   OPENAI_API_KEY="your_api_key_here"
   ```
5. Locate the `baseurl` in the script (usually found in a configuration section or as a constant) and replace it with the correct URL provided by your API service.
6. Run the script:
   ```
   python GPTWeiboAutoPost.py
   ```

### Note on `baseurl`

Before running the script, ensure that you have updated the `baseurl` in the script to match the endpoint provided by your API service. This is typically found in a configuration file or within the script itself. If you are unsure where to find or modify the `baseurl`, refer to the documentation provided with the API or contact the API service provider for assistance.

请确保在您的脚本中有一个明确的注释或文档说明，指导用户如何找到并修改 `baseurl`。这样可以提高用户体验，确保他们能够顺利地配置和运行您的脚本。
## Usage

- After running the script, you will be prompted to enter a Weibo topic.
- Once the topic is entered, the script will generate the Weibo content and display it in the console.
- Confirm the content is correct by entering `y` to post the Weibo, or `n` to exit.

## Important Notes

- Ensure that your ChromeDriver version is compatible with your Google Chrome browser version.
- Before using, carefully read and understand the code in the script to ensure security.
- Comply with OpenAI's terms of use and do not abuse the API.

## Contributing

If you have any suggestions for improvement or find any issues, please feel free to submit an issue or pull request.