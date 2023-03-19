import requests
from bs4 import BeautifulSoup

URL = "https://vesitaigyan.ves.ac.in/about/"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
about=soup.find_all(class_='has-text-align-center')

file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/ai_gyan_about.txt','w') 
for index,abt in enumerate(about):
    about_info = abt.text
    file.write(about_info+"\n")
       
