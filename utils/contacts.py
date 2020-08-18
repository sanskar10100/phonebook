"""Module for contacts table management for each user."""

# For scrub
from . import user
from . import helper
import sqlite3
import csv
import os
import re


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
	_tablename = user.helper.scrub(_tablename)


def show_all_contacts():
	"""Shows all contacts in a user's contact table along with the total contact count."""
	print('\nShowing all contacts')

	# execute returns a sqlite object, fetchone fetches the tuple, and index 0 returns the first entry,
	# is the count
	contact_count = c.execute(f'SELECT COUNT(*) FROM {_tablename}').fetchone()[0]
	print(f'Total Contact Count: {contact_count}')
	# showing all contact
	for name, num, email in c.execute(f'SELECT name, phno, email FROM {_tablename}'):
		print(f'Name: {name} | Number: {num} | Email: {email}')


def add_contact():
	"""Adds a contact to the contacts table"""
	print('\nAdd contact')
	contact_list = list()

	# contact name
	contact_name = input('Name: ')
	# check whether the name is valid or not
	check_name = re.findall("[a-z,A-Z, ]", contact_name)
	check_name = "".join(check_name)
	if (check_name == contact_name):
		while contact_name == '' or contact_name == ' ':
			print('Error: Contact name can not be null!')
			contact_name = input('Name: ')
		else:		
			contact_list.append(contact_name)

	else:
		print("Invalid contact name")

	#contact number
	contact_num = input('Number: ')
	# check whether the number is valid or not
	check_number = re.findall("[0-9,+, ,-]", contact_num)
	check_number = "".join(check_number)
	if(check_number == contact_num):
		while contact_num == '' or contact_num == ' ':
			print('Error: Contact number can not be null!')
			contact_num = input('Number: ')
		else:
			contact_list.append(contact_num)

	else:
		print("Invalid Contact Number")
	 

	# contact email
	contact_email = input('Email: ')
	# check whether the email is valid or not
	check_email = re.findall("[@,.]", contact_email)
	if(check_email):
		if contact_email == '' or contact_email == ' ':
			contact_email = 'NULL'

		contact_list.append(contact_email)

	else:
		print("Invalid Email")

	contact_tuple = tuple(contact_list)
	try:
		# insert the value in user name table
		c.execute(f'''INSERT INTO {_tablename} 
						VALUES (?, ?, ?);''', contact_tuple)
		conn.commit()
		return True
	except:
		return False


def modify_contact():
	"""Modify contact based on the user's choice"""
	print('\nModifying contact')
	contact_name = ''

	while contact_name == '' or contact_name == ' ':
		contact_name = input('Enter name of contact to modify: ')

	if c.execute(f'''SELECT * FROM {_tablename} WHERE LOWER(name) = ?''', (contact_name.lower(), )).fetchone() is None:
		return False

	modify_attribute = helper.select_attributes()

	if modify_attribute == 1:
		try:
			modified_name = ''
			while modified_name == '' or modified_name == ' ':
				modified_name = input('Enter new name of contact: ')

			c.execute(f'''UPDATE {_tablename} 
							SET name = ?
							WHERE LOWER(name) = ?;''', (modified_name, contact_name.lower(), ))
			conn.commit()
			return True
		except:
			return False

	elif modify_attribute == 2:
		try:
			modified_num = input('Number: ')
			while modified_num == '' or modified_num == ' ':
				print('Error: Contact number can not be null!')
				modified_num = input('Number: ')

			c.execute(f'''UPDATE {_tablename} 
							SET phno = ?
							WHERE LOWER(name) = ?;''', (modified_num, contact_name.lower(), ))
			conn.commit()
			return True
		except:
			return False

	elif modify_attribute == 3:
		try:
			modified_mail = input('Email: ')
			while modified_mail == '' or modified_mail  == ' ':
				modified_mail = 'NULL'

			c.execute(f'''UPDATE {_tablename} 
							SET email = ?
							WHERE LOWER(name) = ?;''', (modified_mail, contact_name.lower(), ))
			conn.commit()
			return True
		except:
			return False


def delete_contact():
	"""Deletes contact based on the user input from the contacts table"""
	print('\nDelete contact')
	delete_contact_name = ''

	while delete_contact_name == '' or delete_contact_name == ' ':
		delete_contact_name = input('Enter name of contact to delete: ')

	# If there's at least one entry in table with given key name, then delete it
	if c.execute(f'''SELECT * FROM {_tablename} WHERE LOWER(name) = ?''', (delete_contact_name.lower(), )).fetchone() is not None:
		query = c.execute(f'''DELETE FROM {_tablename}
							WHERE LOWER(name) = ?''', (delete_contact_name.lower(), ))
		conn.commit()
		return True
	else:
		return False


def search_contact():
	"""Searches a contact in the current table and prints all relevant matches."""
	print('\nSearch contact')
	print('Enter Name to search the contact...')
	name_key = input('Name: ')

	while name_key == '' or name_key == ' ':
		print('No input..\ntry again: ')
		name_key = input('Name: ')

	# flag
	flag = False
	for contact_name, number, email in c.execute(f'SELECT * FROM {_tablename}'):
		if name_key.lower() == contact_name.lower():
			print(f'Name: {contact_name} | Number: {number} | Email: {email}')
			flag = True

	return flag


def import_csv():
	"""Imports a CSV from the current directory and stores the data into table.

	Assuming the CSV will be in the following format: name,number,email
	"""
	print('\nImport CSV')
	filename = ''
	while filename == '' or filename == ' ':
		filename = input('Enter filename (must be in current directory, phonebook/): ')			

	try:
		with open(filename, 'r') as file:
			csv_reader = csv.reader(file)
			for row in csv_reader:
				print(row)
				# If either name or number is empty, fail the operation
				if row[0] == '' or row[1] == '':
					print('Here')
					return False
				# if email doesn't exist
				if len(row) == 2:
					row.append('NULL')
				c.execute(f'''INSERT INTO {_tablename} 
								VALUES (?, ?, ?)''', tuple(row))
			else:
				conn.commit()
				return True
	except:
		return False


def export_csv():
	"""Exports contents of table to a csv file in the current directory. Input name from user."""
	print('\nExport CSV')
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