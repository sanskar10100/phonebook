"""Module for user table management."""

import contacts
import hashlib
import sqlite3


# opening database and setting connection
conn = sqlite3.connect('material.db')
c = conn.cursor()

# TODO: Write __user_exists function
def _user_exists(username, password):
	"""Checking if the user already exists or not"""
	login = [username]
	encrypted_credentials = [_encryption(login)]

	sql = c.execute("SELECT username FROM users WHERE username = ?", encrypted_credentials)
	row = c.fetchone()
	if row is None:
		return False
	else:
		return True
	

def _input_credentials():
	"""Inputs and returns username and password."""
	username = input('Username: ')
	password = input('Password: ')

	return (username, password)

def _scrub(table_name):
    return ''.join( chr for chr in table_name if chr.isalnum() or chr == '_' )


def _encryption(login_details):
	"""Return the login credential in sha256 encrypted format."""
	encrypt_login_details = list()
	for credential in login_details:
		encrypt_login_details.append(hashlib.sha256(credential.encode()).hexdigest())
	return tuple(encrypt_login_details)


def add_user():
	"""Adds user to database if doesn't exist and create a contacts table for him.
	Returns a string indicating the status
	"""
	username, password = _input_credentials()

	if _user_exists(username, password):
		return "The user already exists"
	else:
		#Add user to users table
		c.execute("""CREATE TABLE IF NOT EXISTS users( 
			username VARCHAR(256) NOT NULL,
			password VARCHAR(256) NOT NULL);
		""")
		encrypted_credentials = _encryption([username, password])
		c.execute("INSERT INTO users VALUES (?,?);", encrypted_credentials)
		conn.commit()

		#Create contacts table for user. Name: contacts_username
		#Scrubing the username.
		tablename = scrub('contacts_' + username)
		c.execute("""CREATE TABLE %s (
			name VARCHAR(255) NOT NULL,
			phno VARCHAR(20) NOT NULL,
			email VARCHAR(255) NOT NULL);
			"""% tablename)
		
		conn.commit()
		
		return "User successfully added"


def remove_user():
	"""Removes a user and associated contact table from the database.
	Returns a string indicating the status
	"""
	username, password = _input_credentials()

	if _user_exists(username, password):
		#Remove user from users table
		login = [username]
		encrypt_username = _encryption(login)
		c.execute("DELETE FROM Phonebook WHERE username = ?", encrypt_username)
		conn.commit()

		# TODO: Remove users contacts table
		return "User successfully removed"
	else:
		return "User not found"


def select_user():
	"""Selects a user for current contact operations.
	Returns a string indicating the status
	"""
	username, password = _input_credentials()

	if _user_exists(username, password):
		contacts._username = username
		return "User successfully selected"
	else:
		return "User not found"