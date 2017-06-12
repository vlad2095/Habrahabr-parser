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
    
    def get_path(self, html_tree, link):
        return html_tree.xpath(link)

    def get_link(self, title):
        return title.get('href')

    def get_info(self, html):
        try:    
            html_tree = lxml.html.fromstring(html)
            titles_link = './/div[@class="posts_list"]//h2[@class="post__title"]//a[@class="post__title_link"]'
            synopsis_link = './/div[@class="posts_list"]//div[@class="content html_format"]'
            titles = parser.get_path(html_tree, titles_link)
            synopsises = parser.get_path(html_tree, synopsis_link)
        except (IndexError, AttributeError):
            return

        for i in range(len(titles)):
            print("Title: " + titles[i].text_content()+'\n')
            print("Link: " + parser.get_link(titles[i]) + '\n')
            print("Text: " + synopsises[i].text_content()+'\n')

                
    def run(self):
        while True:
            page = self.get_page()
            if page is None:
                time.sleep(0.5)
                continue
            self.get_info
            time.sleep(0.5)
                
if __name__ == "__main__":

        parser = HabrParser("https://habrahabr.ru/")
        page = parser.get_page()
        parser.get_info(page)
