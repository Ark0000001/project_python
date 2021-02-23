import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv



def get_html(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name']))


def refine_p(p):
    return p.replace(' ','')

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('div', class_='item_info')

    for li in lis:

        name = li.find('div', class_='item-title').find('a').text.strip()



        data = {'name': name}

        write_csv(data)



def main():
    url = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/'
    print(get_data(get_html(url)))



if __name__ == '__main__':
    main()
