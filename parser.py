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
		
	def parse(self):
		pass
		
	def run(self):
		pass
		
if __name__ == "__main__":

	parser = HabrParser("https://www.olx.ua/list/")
	page = parser.get_page()
	print (page)
