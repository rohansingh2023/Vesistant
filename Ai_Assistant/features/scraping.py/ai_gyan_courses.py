import requests
from bs4 import BeautifulSoup

URL = "https://vesitaigyan.ves.ac.in/courses/"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
courses=soup.find_all(class_='elementor-toggle-title')

file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/ai_gyan_courses.txt','w') 

for index,c in enumerate(courses):
   course = c.text
   file.write(course+"\n")