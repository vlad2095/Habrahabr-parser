#coding: utf-8
import urllib
import re
from db_handler import Postgresdb
from settings import TABLE_NAME
from string import replace

class Parser:
        
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_page(self):
        return urllib.urlopen(self.base_url).read()

    def get_links(self, page):
        result = []
        temp = re.findall(r'class="posts shortcuts_items"(.*?)class="page__footer"*', page, re.DOTALL)
        temp = re.findall(r'(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?', page, re.DOTALL)
        for x in temp:            
            if x.startswith('https://habrahabr.ru/') and re.match('(.*?)(\d+)\/', x) is not None:
                if not x in result and 'top' not in x:
                    result.append(x)
        return result

    def fix_quotes(self, string):
        temp = replace(string, "'", "\"")
        fixed = replace(temp, '"','\"')
        return fixed

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

        return parser.fix_quotes(parser.list_to_str(result))

    def get_data(self, page):
        article = parser.clean(parser.get_article(page))
        title = parser.get_title(page)
        return title, article        

    def run(self, links):
        for link in links:
            parser = Parser(link)
            page = parser.get_page()
            title, article = parser.get_data(page)
            db.inserti(parser.fix_quotes(title), article)

if __name__ == "__main__":
        db = Postgresdb()
        db.connect()
        db.create_table(TABLE_NAME)
        for i in range(1,3):
            parser = Parser("https://habrahabr.ru/all/page{0}/".format(i))
            page = parser.get_page()
            links = parser.get_links(page)
            parser.run(links)
        db.close()