import psycopg2 as db

class Postgresdb:

	def __init__(self):
		self.database = None
		self.cursor = None
		
	def __enter__(self):
		return self

	def __exit__(self, type, value, tb):
		self.close()

	def connect(self, parameters):
		self.database = db.connect(**parameters)
		self.cursor = self.database.cursor

	def close(self):
		self.cursor.close
		self.database.close

	def execute(self, query, param=None):
		if param:
			return self.cursor.execute(query, param)
		else:
			return self.cursor.execute(query)
	def create_table(self):
		pass

	def add_article(self,title, link, article):
		cursor.execute("INSERT INTO articles (title, link, article) values(%s, %s,%s)", title, link, article)

	def print_all(self, table):
		cursor.execute("SELECT * FROM %s;", table)

	def database(self):
		return self.database
	def cursor(self):
		return self.cursor

