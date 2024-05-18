import requests
from bs4 import BeautifulSoup
import selenium


for i in (1,2,3,4):
    print("=========",i,"============")
    網站 = requests.get(f"https://www.vscinemas.com.tw/vsweb/film/index.aspx?p={i}")
    html = 網站.text
    soup = BeautifulSoup(html, "html.parser")
    sections = soup.find_all("section",class_="infoArea")
    for section in sections:
        print(section.find("h2").text)
   