import time
import requests
import lxml.html
from database_for_parser import Postgresdb
from string import replace

def fix_quotes(string):
    temp = replace(string, "'", "\"")
    fixed = replace(temp, '"','\"')
    return fixed

class Parser:
        
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_page(self):
                
        try:
            res = requests.get(self.base_url)
        except requests.ConnectionError:
            return
                        
        if res.status_code < 400:
            return res.content

    def get_html_tree(self, html):
        return lxml.html.fromstring(html)

    def get_link(self, somedata):
        return somedata.get('href')

    def get_path(self, html_tree, link):
        return html_tree.xpath(link)

    def get_full_text(self, somelist):
        articles = []
        path = './/div[@class="content html_format js-mediator-article"]'
        for link in somelist:
            link = Parser(link)
            page = link.get_page()
            tree = link.get_html_tree(page)
            links = link.get_path(tree, path)
            for one in links:
                text = one.text_content().encode('utf-8')
                articles.append(text)
        return(articles)

    def get_info(self, html):
        try:    
            tree = parser.get_html_tree(html)
            titles_path = './/div[@class="posts_list"]//h2[@class="post__title"]//a[@class="post__title_link"]'
            titles = parser.get_path(tree, titles_path)
        except (IndexError, AttributeError):
            return
        titles_list = []
        link_list = []
        for one in titles:
            link = parser.get_link(one)
            link_list.append(link)
            title = one.text_content().encode('utf-8')
            titles_list.append(title)

        return titles_list, link_list





    # def run(self):
    #     while True:
    #         page = self.get_page()
    #         if page is None:
    #             time.sleep(0.5)
    #             continue
    #         self.get_info(page)
    #         time.sleep(0.5)

if __name__ == "__main__":
        db = Postgresdb()
        db.connect()
        db.create_table("dtb") 
        for i in range(1,10,1):
            print(i)
            parser = Parser("https://habrahabr.ru/all/page{0}/".format(i))
            page = parser.get_page()
            titles, links = parser.get_info(page)
            articles = parser.get_full_text(links)
            for i in range(10):
                print(i)
                title = fix_quotes(titles[i])
                article = fix_quotes(articles[i])
                db.inserti(title, article)
        db.close()