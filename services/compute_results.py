"""
Survey results
"""
import mysql.connector
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))





def total_surveys():

	from DBconnection import get_DBconnection
	conn = get_DBconnection()

	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None

	"""
	returns number of surveys.

	Args:
		None

	Returns:
		total (int): integer representing number of rows
	"""


	query = "SELECT COUNT(*) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchall()

		total = data[0]

		return total[0]

	except mysql.connector.Error as err:
		cursor.close()
		conn.close()
		return f"Error: {err}"


def average_age():

	"""
	Returns the average of participants

	Args:
		None

	Returns:
		average_age (int): Integer representing an averange of age
	"""

	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None

	
	query = "SELECT AVG(age) AS Average_age FROM Survey"

	try:

		cursor.execute(query)

		data = cursor.fetchone()

		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False

	except mysql.connector.Error as err:
		return f"Error: {err}"

def oldest():

	"""
	Returns the oldest person
	"""

	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None


	query = "SELECT fullname, age FROM Survey WHERE age = (SELECT MAX(age) FROM Survey)"

	try:
		cursor.execute(query)

		data = cursor.fetchall()
		if (cursor.rowcount > 0):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def youngest():

	"""
	Returns youngest person
	"""

	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None


	query = "SELECT fullname, age FROM Survey WHERE age = (SELECT 	MIN(age) FROM Survey)"

	try:
		cursor.execute(query)

		data = cursor.fetchall()
		if (cursor.rowcount > 0):
			return data[0]
		return False
	except mysql.connector.Error as err:
		return f"Error: {err}"
	

def pizza():

	"""
	Returns percentage of people who like pizza 
	"""

	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None




	query = "SELECT (SUM(pizza = 1) / COUNT(*)) * 100 FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def pasta():
	"""
	Returns percentage of people who like pasta 
	"""
	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None
	

	query = "SELECT (SUM(pasta = 1) / COUNT(*)) * 100 FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def pap_wors():
	"""
	Returns percentage of people who like Pap and  Wors
	"""
	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None


	query = "SELECT (SUM(pap_and_wors = 1) / COUNT(*)) * 100 FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
	
def movie():
	"""
	Returns the average rating for people who like movies
	"""
	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None
	

	query = "SELECT AVG(6 - movies) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def radio():
	"""
	Returns the average rating for people who like radio
	"""
	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None
	

	query = "SELECT AVG(6 - radio) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def eating_out():
	"""
	Returns the average rating for people who like eating out
	"""
	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None
	

	query = "SELECT AVG(6 - eat_out) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0 and data[0] is not None):
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"
	
def tv():
	"""
	Returns the average rating for people who like tv
	"""

	from DBconnection import get_DBconnection
	conn = get_DBconnection()
	
	if conn:
		print("Database connected!")
		cursor = conn.cursor()
	else:
		print("No DB connection")
		cursor = None

	query = "SELECT AVG(6 - tv) FROM Survey"

	try:
		cursor.execute(query)

		data = cursor.fetchone()
		if (cursor.rowcount > 0) and data[0] is not None:
			return data[0]
		return False
	
	except mysql.connector.Error as err:
		return f"Error: {err}"