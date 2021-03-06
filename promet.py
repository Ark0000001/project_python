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



def refine_p(p):
    return p.replace(' руб.','')

def write_csv(data):
    with open('prom.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['price']))

# def get_page_data(html):
    # soup = BeautifulSoup(html, 'lxml')
    #
    # lis = soup.find_all('div', class_='item_info')
    #
    # for li in lis:
    #     try:
    #         name = li.find('div', class_='item-title').find('a').text.strip()
    #     except:
    #         name = ''
    #
    #     try:
    #         p = li.find('div', class_='price_value_block').find('span', class_='price_value').text.strip()
    #         price = refine_p(p)
    #     except:
    #         price = ''
    #     data = {'name': name,
    #             'price': price}
    #
    #     write_csv(data)

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    tab = soup.find_all('table', class_="complect-table")
    for t in tab:

        try:
            trs = t.tbody.find_all('tr')

            for tr in trs:
                tds = tr.find_all('td')
                name = tds[2].find('b').text
                # symbol = tds[1].find('a').text
                # url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
                price = refine_p(tds[7].text)

                data = {'name': name,

                        'price': price}

                write_csv(data)
        except:
            break

# def konec(url):
#
#     soup = BeautifulSoup(get_html(url), 'lxml')
#     url1 = soup.find('div', class_='nums').find_all('a', class_="dark_link")
#     for elem in url1:
#         e = []
#         e.append(elem)
#
#     k = str(e[-1])
#     c = re.compile('\d+')
#
#     return int(c.findall(k)[-1])+1


def main():
    url = 'https://www.safe.ru/catalog/metallicheskie-stellazhi/ms-pro-3000-kg-na-sektsiyu/'
    get_page_data(get_html(url))



    # pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/metallicheskie-shkafy/?PAGEN_1={}'
    #
    # for i in range(1, konec(pattern)):
    #     url = pattern.format(str(i))
    #     get_page_data(get_html(url))
    #
    # pattern = 'https://xn--c1azcgcc.xn----7sbenacbbl2bhik1tlb.xn--p1ai/catalog/seyfy/?PAGEN_1={}'
    #
    # for i in range(0, konec(pattern)):
    #     url = pattern.format(str(i))
    #     get_page_data(get_html(url))


if __name__ == '__main__':
    main()
