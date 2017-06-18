import psycopg2 as db
#ну а тут вообще пиздец
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
		self.cursor = self.database.cursor

	#def close(self):
		# self.cursor.close
		# self.database.close

	def create_table(self, cursor):
		cursor.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL UNIQUE);")

	#def add_title(self, title):
		#cursor.execute("INSERT INTO articles (title) values (%s)", title)

	#def print_all(self, table):
		#cursor.execute("")


	# def database(self):
	# 	return self.database
	# def cursor(self):
	# 	return self.cursor

