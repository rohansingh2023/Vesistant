import requests
from bs4 import BeautifulSoup

URL = "https://vesit.ves.ac.in/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'lxml')

whats_new = soup.find_all('div',class_="col-12 col-md-3 mx-0")

file=open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/whats_new.txt','w')
for new in whats_new:
    what_new = new.text
    file.write(what_new+"\n")
