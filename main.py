# coding=euc-kr
import os

import requests
import telegram
from bs4 import BeautifulSoup
import schedule


def crawler(url, key):
    news_link = []
    reponse = requests.get(url)
    html = reponse.text
    soup = BeautifulSoup(html, 'html.parser')  # news_area
    url = '/media/view.asp'
    idx = 'idx='
    kind = 'kind'

    for link in soup.find_all('a', href=True):
        notices_link = link['href']

        if notices_link.find(url) != -1 and notices_link.find(idx) != -1 and notices_link.find(kind) != -1:
            split_notices_link = notices_link.split('&')[0]

            if split_notices_link not in news_link and 'idx' in split_notices_link:
                news_link.append(split_notices_link)
    newlink = compareLink(news_link, key)
    chatBot(newlink)


def compareLink(newslink, key):
    newlink = []
    if os.path.exists('compare' + '_' + str(key) + '.txt'):
        with open('compare' + '_' + str(key) + '.txt') as f:
            link_list = f.readlines()
            for printer in newslink:
                if printer + '\n' in link_list:
                    newlink.append(printer)
    else:
        for printer in newslink:
            newlink.append(printer)

    with open('compare' + '_' + str(key) + '.txt', 'a') as f:
        for tempwrite in newlink:
            print(tempwrite)
            f.write(tempwrite + '\n')
    return newlink


def executeCrawler(urls):
    for key in urls:
        crawler(urls.get(key), key)


def chatBot(newlink):
    if newlink.__len__() != 0:
        bot = telegram.Bot(token='915048180:AAFQXGGq_8ZIrksva2RA2M3v9dOeQZmSPgQ')
        chat_id = bot.getUpdates()[-1].message.chat.id
        bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요!')


if __name__ == "__main__":
    # https://www.boannews.com/media/s_list.asp?skind=5     취약점 경고 및 보안 업데이트
    # https://www.boannews.com/media/s_list.asp?skind=6     정책
    # https://www.boannews.com/media/list.asp?mkind=1     security
    # https://www.boannews.com/media/list.asp?mkind=3    defense

    urls = {1: 'https://www.boannews.com/media/s_list.asp?skind=5',
            2: 'https://www.boannews.com/media/s_list.asp?skind=6',
            3: 'https://www.boannews.com/media/list.asp?mkind=1',
            4: 'https://www.boannews.com/media/list.asp?mkind=3'}
    executeCrawler(urls)
    # schedule.every(15).minutes.do(executeCrawler(urls))
