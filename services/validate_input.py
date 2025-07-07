"""
Validate user input from form
"""

import mysql.connector
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from DBconnection import get_DBconnection


def check_email(email):
	""" 
	Checks if email exist in the datebase.

	Args:
		email (str): String representing email address to be checked.

	Returns:
		(bool): True if email exists, false if it does not.
	"""

	conn = get_DBconnection()
	cursor = conn.cursor()

	query = "SELECT * FROM Survey WHERE `email` = %s"

	try:
		cursor.execute(query, email)
		respose = cursor.fetchall()

		if (len(respose) > 0):
			return True
		return False
	
	except mysql.connector.Error as err:
		cursor.close()
		conn.close()
		return f"Error {err}"



# def check_age(date_str):
# 	"""
# 	Checks personal details.

# 	Args:
# 		date_str (str): a string representing a date of birth

# 	Returns:

# 		 age(int): an integer representing age 
# 	"""

# 	birth_date = datetime.strptime(date_str, "%Y-%m-%d")
# 	current = datetime.now()
# 	date_difference = current - birth_date
# 	age = date_difference.days // 365

# 	return age

	
