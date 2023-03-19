import requests
from bs4 import BeautifulSoup

URL = "https://vesit.ves.ac.in/placements/procedure"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
announcements=soup.find_all(class_='row m-0')

file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/placement_procedure.txt','w') 
   
for announ in announcements:
    announcement = announ.text
    file.write(announcement)


