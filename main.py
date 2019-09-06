# coding=euc-kr
import os

import requests
import telegram
from bs4 import BeautifulSoup


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
    newlink = compareLink(news_link)
    chatBot(newlink, key)


def compareLink(newslink):
    newlink = []
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '/compare.txt'):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/compare.txt') as f:
            link_list = f.readlines()
            for printer in newslink:
                if printer + '\n' not in link_list:
                    newlink.append(printer)
    else:
        for printer in newslink:
            newlink.append(printer)

    with open(os.path.dirname(os.path.abspath(__file__)) + '/compare.txt', 'a') as f:
        for tempwrite in newlink:
            print(tempwrite)
            f.write(tempwrite + '\n')
    return newlink


def executeCrawler(urls):
    for key in urls:
        crawler(urls.get(key), key)


def chatBot(newlink, key):
    if key == 1:
        category = '����� ��� �� ���� ������Ʈ'
    elif key == 2:
        category = '��å'
    elif key == 3:
        category = 'security'
    else:
        category = 'defense'

    if newlink.__len__() != 0:
        bot = telegram.Bot('TOKEN')
        chat_id = 'your chat_id'
        for newlisk_list in newlink:
            bot.sendMessage(
                chat_id=chat_id, text='�ں��ȴ���\nī�װ� : '
                                      '{category}\nURL : {URL}'.format(category=category,
                                                                       URL='\nhttps://www.boannews.com' + newlisk_list))


if __name__ == "__main__":
    # https://www.boannews.com/media/s_list.asp?skind=5     ����� ��� �� ���� ������Ʈ
    # https://www.boannews.com/media/s_list.asp?skind=6     ��å
    # https://www.boannews.com/media/list.asp?mkind=1     security
    # https://www.boannews.com/media/list.asp?mkind=3    defense

    urls = {1: 'https://www.boannews.com/media/s_list.asp?skind=5',
            2: 'https://www.boannews.com/media/s_list.asp?skind=6',
            3: 'https://www.boannews.com/media/list.asp?mkind=1',
            4: 'https://www.boannews.com/media/list.asp?mkind=3'}
    executeCrawler(urls)
