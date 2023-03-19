import requests
from bs4 import BeautifulSoup

URL = "https://vesit.ves.ac.in/announcements/107"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
announcements=soup.find_all(class_='text-justify')
file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/national_startup_day.txt','w') 
   
for announ in announcements:
    announcement = announ.text
    file.write(announcement)