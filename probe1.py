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



def refine_p(p):
    return p.replace(' ','')

def refine_z(n):

    list = ["Шкаф газовый ШГР ",'Шкаф газовый ШГР']

    split_line = n.split()
    for word in split_line:
        if word in list:
            n=None
    return n

    #         split_line.remove(word)
    # output = ' '.join(split_line)
    # return output

def write_csv(data):
    with open('cmcprobe1.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    lis = soup.find_all('div', class_='item_info')

    for li in lis:
        try:
            n = li.find('div', class_='item-title').find('a').text.strip()
            name = refine_z(n)
        except:
            name = ''

        try:
            p = li.find('div', class_='price_value_block').find('span', class_='price_value').text.strip()
            price = refine_p(p)
        except:
            price = ''
        data = {'name': name,
                'price': price}

        write_csv(data)



def main():



    pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/metallicheskie-shkafy/?PAGEN_1={}'

    for i in range(1, 3):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()
