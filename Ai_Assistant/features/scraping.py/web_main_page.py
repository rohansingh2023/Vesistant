import requests
from bs4 import BeautifulSoup

URL = "https://vesit.ves.ac.in/"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
main=soup.find_all(class_='card-header text-center')


file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/main_page.txt','w') 

   
for content in main:
    con = content.text.replace(' ','')
    file.write(con+"\n")