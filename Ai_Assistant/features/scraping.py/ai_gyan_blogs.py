import requests
from bs4 import BeautifulSoup

URL = "https://vesitaigyan.ves.ac.in/blogs/"
response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,'lxml')
blogs=soup.find_all(class_='text-blog')

file= open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/ai_gyan_blogs.txt','w') 
for index,name in enumerate(blogs):
    blog = name.text 
    file.write(blog+"\n")
   