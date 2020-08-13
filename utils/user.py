"""Module for user table management."""

import contacts
import hashlib
import sqlite3


# opening database and setting connection
conn = sqlite3.connect('material.db')
c = conn.cursor()


# TODO: Write __user_exists function
def _user_exists():
	pass


def _input_credentials():
	"""Inputs and returns username and password."""
	username = input('Username: ')
	password = input('Password: ')

	return (username, password)


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
		c.execute('''CREATE TABLE IF NOT EXISTS users
					( username VARCHAR(256) NOT NULL,
					  password VARCHAR(256) NOT NULL
					);''')

		login = [username, password]
		encrypted_credentials = [_encryption(login)]

		c.executemany("INSERT INTO users (?, ?)", encrypted_credentials)

		conn.commit()

		#Create contacts table for user. Name: contacts_username

		tablename = 'contacts_' + username
		c.execute(f'''CREATE TABLE {tablename}
		(name VARCHAR(255) NOT NULL,
		 number VARCHAR(15) NOT NULL,
		 email VARCHAR(255))''')
		
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
