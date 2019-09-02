# coding=euc-kr


# https://m.boannews.com/html/Sub_Menu.html?mtype=2&tab_type=5     취약점 경고 및 보안 업데이트
# https://m.boannews.com/html/Sub_Menu.html?mtype=3&tab_type=6    정책

# https://m.boannews.com/html/Main_Menu.html?mkind=1     security
# https://m.boannews.com/html/Main_Menu.html?mkind=3     defense

# 915048180:AAFQXGGq_8ZIrksva2RA2M3v9dOeQZmSPgQ         토큰값
from collections import OrderedDict

import requests
from bs4 import BeautifulSoup


def crawler(url):
    news_link = []
    reponse = requests.get(url)
    html = reponse.text
    soup = BeautifulSoup(html, 'html.parser')  # news_area
    url = '/media/view.asp'
    idx = 'idx='
    kind = 'kind'
    page = 'page'

    print(soup.contents.__len__())
    for link in soup.find_all('a', href=True):
        notices_link = link['href']
        # print(notices_link)

        # for ahref in notices_link:
        # print(ahref.contains('idx'))
        if notices_link.find(url) != -1 and notices_link.find(idx) != -1 and notices_link.find(kind) != -1:
            # news_link = notices_link

            notices_link.split()
            if notices_link not in news_link:
                news_link.append(notices_link)
    #
    # # if link.__contains__('a href'):
    for printer in news_link:

        print(printer)
    # print(type(news_link))


# link = soup.select_one('#news_area')
# print(link)


# for link in soup.find_all('a'):
#     # print(link)
#     notices_link = link['href']
#     if 'detail.html' in notices_link:
#         news_link.append(notices_link)
# news_link = list(OrderedDict.fromkeys(news_link))
# print(news_link)


def match_class(target):
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)

    return do_match


if __name__ == "__main__":
    print("test")
    crawler('https://www.boannews.com/media/list.asp?mkind=1')
