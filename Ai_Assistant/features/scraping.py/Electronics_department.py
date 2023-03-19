import requests
from bs4 import BeautifulSoup

URL = "https://vesit.ves.ac.in/announcements/114"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
announcement=soup.find_all(class_='text-justify')

file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/electronics_dept.txt','w') 
   
for announ in announcement:
    announce = announ.text
    file.write(announce)