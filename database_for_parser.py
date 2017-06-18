import psycopg2 as db

class Postgresdb:

	def __init__(self):
		self.database = None
		self.cursor = None

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

	def add_article(self):
		add_title()
		add_text()
		add_link()

	def add_title(self):
		pass

	def add_text(self):
		pass
	def add_link(self):
		pass

