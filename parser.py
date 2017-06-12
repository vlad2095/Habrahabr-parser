import time
import requests
import lxml.html

class HabrParser:
        
    def __init__(self, base_url):
        self.base_url = base_url
        self.whatever = ""
        
    def get_page(self):
                
        try:
            res = requests.get(self.base_url)
        except requests.ConnectionError:
            return
                        
        if res.status_code < 400:
            return res.content
                
    def parse(self, html):
        html_tree = lxml.html.fromstring(html)
        titles_path = './/div[@class="posts_list"]//h2[@class="post__title"]//a[@class="post__title_link"]'
        titles = html_tree.xpath(titles_path)
        mains_path = './/div[@class="posts_list"]//div[@class="content html_format"]'
        maintext = html_tree.xpath(mains_path)
        for i in range(2):
            print("Title: " + titles[i].text_content()+'\n')
            print("Text: " + maintext[i].text_content()+'\n')

                
    def run(self):
        pass
                
if __name__ == "__main__":

        parser = HabrParser("https://habrahabr.ru/")
        page = parser.get_page()
        parser.parse(page)
