import psycopg2 as db

class Postgresdb:

	def __init__(self):
		self.database = None
		self.cursor = None
		

	def connect(self):
		self.database = db.connect(host="localhost", user="postgres", password="pomidor69", dbname="parser1") 
		self.cursor = self.database.cursor()

	def create_table(self, name):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS {0} (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, content TEXT NOT NULL);".format(name))
		self.database.commit()

	def close(self):
		self.database.close()


	def inserti(self, title, content):
		self.cursor.execute("INSERT INTO dtb (title, content) VALUES ('{0}', '{1}')".format(title, content))
		self.database.commit()


