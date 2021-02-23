import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv
import re

def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text


url = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/seyfy'
soup = BeautifulSoup(get_html(url), 'lxml')

url1 = soup.find('div', class_='nums').find_all('a',class_="dark_link")
for elem in url1:
    e=[]
    e.append(elem)

k=str(e[-1])
c=re.compile('\d+')

print(int(c.findall(k)[-1])-1)







