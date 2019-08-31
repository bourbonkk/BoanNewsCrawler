# coding=euc-kr


# https://www.boannews.com/media/s_list.asp?skind=5     취약점 경고 및 보안 업데이트
# https://www.boannews.com/media/s_list.asp?skind=6     정책

# https://www.boannews.com/media/list.asp?mkind=1       security
# https://www.boannews.com/media/list.asp?mkind=3       defense

# 915048180:AAFQXGGq_8ZIrksva2RA2M3v9dOeQZmSPgQ         토큰값
from collections import OrderedDict

import requests
from bs4 import BeautifulSoup


def crawler(url):
    news_link = []
    reponse = requests.get(url)
    html = reponse.text
    soup = BeautifulSoup(html,'html.parser')  # news_area

    for link in soup.find_all('a'):
        notices_link = link['href']
        if '/media/view.asp?idx=' in notices_link:
            news_link.append(notices_link)
    news_link = list(OrderedDict.fromkeys(news_link))
    print(news_link)



if __name__ == "__main__":
    print("test")
    crawler('https://www.boannews.com/media/list.asp?mkind=1')
