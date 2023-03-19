import requests
from bs4 import BeautifulSoup

URL = "https://vesitaigyan.ves.ac.in/events/"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
event=soup.find_all(class_='elementor-text-editor elementor-clearfix')

file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/ai_gyan_events.txt','w') 

for e in event:
   eve = e.text
   file.write(eve)
 
    