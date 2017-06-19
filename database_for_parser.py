import psycopg2 as db

class Postgresdb:

	def __init__(self):
		self.database = None
		self.cursor = None
		
	# def __enter__(self):
	# 	return self

	# def __exit__(self, type, value, tb):
	# 	self.close()

	# def execute(self, query, param=None):
	# 	if param:
	# 		return self.cursor.execute(query, param)
	# 	else:
	# 		return self.cursor.execute(query)

	def connect(self):
		self.database = db.connect(host="localhost", user="postgres", password="pomidor69", dbname="parser1")
		self.cursor = self.database.cursor()


	#def close(self):
		# self.cursor.close
		# self.database.close

	def create_table(self, name):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS {0} (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL UNIQUE);".format(name))
		self.database.commit()

	def close(self):
		self.database.close()


	def inserti(self, title):
		print(("INSERT INTO titles (title) VALUES ({0})".format(title)))
		self.cursor.execute("INSERT INTO titles (title) VALUES ({0})".format(title))
	
	#def print_all(self, table):
		#cursor.execute("")


