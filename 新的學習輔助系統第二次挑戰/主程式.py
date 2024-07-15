import transformers
import requests
from bs4 import BeautifulSoup
new_information = []
import requests
from bs4 import BeautifulSoup

url = 'https://docs.google.com/document/d/1V-GWJAFcYbdv7hlB43XSslmH5iyEK4WFZ1tYaKSosio/edit'

# 使用 requests 库获取网页内容
response = requests.get(url)

# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取文档内容
document_content = ""
for paragraph in soup.find_all('div', {'class': 'kix-paragraphrenderer-unstylized'}):
    text = paragraph.get_text()
    document_content += text + "\n"

# 打印文档内容
print(document_content)


