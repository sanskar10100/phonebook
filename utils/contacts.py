"""Module for contacts table management for each user."""

# For scrub
from . import user
import sqlite3


# Global sqlite3 connection and cursor
conn = sqlite3.connect('material.db')
c = conn.cursor()


# Name of current table
_tablename = ''


def _set_tablename(username):
	# Allows changing the value of global var tablename
	global _tablename
	"""Sets tablename based on the username obtained from user module."""
	_tablename = 'contacts_' + username
	# Tablename sanitized to avoid SQL injection attacks
	_tablename = user._scrub(_tablename)


def show_all_contacts():
	"""Shows all contacts in a user's contact table along with the total contact count."""
	printf('Showing all contact...')

	# showing all contact
	for name, num, email in c.execute(f'SELECT name, phno, email FROM {_tablename}'):
		print(f'Name: {name} | Number: {num} | Email: {email}')


def add_contact():
	"""Adds a contact to the contacts table"""
	contact_list = list()

	# contact name
	contact_name = input('Name: ')
	while contact_name == '' or contact_name == ' ':
		print('Error: Contact name can not be null!')
		contact_name = input('Name: ')
	else:		
		contact_list.append(contact_name)

	#contact number
	contact_num = input('Number: ')
	while contact_num == '' or contact_num == ' ':
		print('Error: Contact number can not be null!')
		contact_num = input('Number: ')
	else:
		contact_list.append(contact_num)

	# contact email
	contact_email = input('Email: ')
	if contact_email == '' or contact_email == ' ':
		contact_email = 'NULL'

	contact_list.append(contact_email)

	contact_tuple = tuple(contact_list)
	try:
		# insert the value in user name table
		c.execute(f'''INSERT INTO {_tablename} 
						VALUES (?, ?, ?);''', contact_tuple)
		conn.commit()
		return True
	except:
		return False


def delete_contact(choice):
	"""Deletes contact based on the user input from the contacts table"""
	pass


def search_contact():
	"""Searches a contact in the current table and prints all relevant matches."""
	pass


def import_csv():
	"""Imports a CSV and stores the data into table."""
	pass


def export_csv():
	"""Exports contents of table to a csv file. Input name from user."""
	pass
