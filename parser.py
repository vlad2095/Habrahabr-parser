#coding: utf-8
import urllib
import re
from db_handler import Postgresdb
from settings import TABLE_NAME

class Parser:
        
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_page(self):
        return urllib.urlopen(self.base_url).read()

    def get_links(self, page):
        result = []
        temp = re.findall(r'<h2> class="post__title"(.*?)</h2', page, re.DOTALL)
        #temp = re.findall(r'<a href="(.*?)"', page, re.DOTALL)
        print temp

    def list_to_str(self, ls):
        result = ''
        for one in ls:
            result += one
        return result

    def get_title(self, page):
        result = re.findall(r'<title>(.*?)</title>*', page, re.DOTALL)
        return parser.list_to_str(result)

    def get_article(self, page):
        result = re.findall(r'<div class="content html_format js-mediator-article">(.*?)<script*', page, re.DOTALL)
        return parser.list_to_str(result)

    def clean(self, text):
        result = re.findall(r'>(.*?)</*', text, re.DOTALL)
        return parser.list_to_str(result)

    def get_data(self, page):
        article = parser.clean(parser.get_article(page))
        title = parser.get_title(page)
        return title, article        

    # def get_data(self, page):
    #     page = page = parser.get_page()
    #     article = parser.clean(parser.get_article(page))


if __name__ == "__main__":
        db = Postgresdb()
        db.connect()
        db.create_table(TABLE_NAME)
        #for i in range(1,3,1):
            #print(i)
        parser = Parser("https://habrahabr.ru/all/page{0}/".format(1))
        page = parser.get_page()
        #print parser
        test = parser.get_links(page)
        #print(test)
        #title, article = parser.get_data(page)
        #print title, article
        # titles, links = parser.get_info(page)
        # articles = parser.get_full_text(links)
        # for i in range(2):
        #     print(i)
        #     title = fix_quotes(titles[i])
        #     article = fix_quotes(articles[i])
            #db.inserti(title, article)
        #db.close()

#<a href=(.*?) class="post__title_link">Запускаем GSM-сеть у себя дома</a>