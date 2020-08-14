"""Module for contacts table management for each user."""

# For scrub
from . import user
import sqlite3
import csv
import os


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
	print('\nShowing all contact...')

	# execute returns a sqlite object, fetchone fetches the tuple, and index 0 returns the first entry,
	# is the count
	contact_count = c.execute(f'SELECT COUNT(*) FROM {_tablename}').fetchone()[0]
	print(f'Total Contact Count: {contact_count}')
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


def delete_contact():
	"""Deletes contact based on the user input from the contacts table"""
	delete_contact_name = ''

	while delete_contact_name == '' or delete_contact_name == ' ':
		delete_contact_name = input('Enter name of contact to delete: ')

	# If there's at least one entry in table with given key name, then delete it
	if c.execute(f'''SELECT * FROM {_tablename} WHERE name = ?''', (delete_contact_name, )).fetchone() is not None:
		query = c.execute(f'''DELETE FROM {_tablename}
							WHERE name = ?''', (delete_contact_name, ))
		conn.commit()
		return True
	else:
		return False


def search_contact():
	"""Searches a contact in the current table and prints all relevant matches."""
	print('Enter Name to search the contact...')
	name_key = input('Name: ')

	while name_key == '' or name_key == ' ':
		print('No input..\ntry again: ')
		name_key = input('Name: ')

	# flag
	flag = False
	for contact_name, number, email in c.execute(f'SELECT * FROM {_tablename}'):
		if name_key in contact_name:
			print(f'Name: {contact_name} | Number: {number} | Email: {email}')
			flag = True

	return flag


def import_csv():
	"""Imports a CSV from the current directory and stores the data into table."""
	contact_row = list()
	file_name = input("Enter file name : ")
	if not os.path.exists(file_name):
		return False
	path = os.path.join(os.getcwd(), file_name)
	with open(path, 'r') as file:
		csv_reader = csv.DictReader(file)
		for key in csv_reader:
			for value in key.values():
				contact_row.append(value)

			contact_tuple = tuple(contact_row)
			contact_row.clear()
			# insert the value in user name table
			c.execute(f'''INSERT INTO {_tablename} 
							VALUES (?, ?, ?);''', contact_tuple)
			conn.commit()
	return True
			


def export_csv():
	"""Exports contents of table to a csv file in the current directory. Input name from user."""
	filename = ''

	# Read the CSV filename while handling incorrect inputs
	while filename.isalnum() is False and '.' not in filename:
		filename = input('CSV filename: ')
		if filename.isalnum() is False and '.' not in filename:
			print('Error: Invalid filename. Try again!\n')

	try:
		with open(filename, 'w') as file:
			csv_writer = csv.writer(file)
			for row in c.execute(f'SELECT * FROM {_tablename}'):
				csv_writer.writerow(row)
			else:
				return True
	except:
		return False