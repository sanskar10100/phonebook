"""Module for contacts table management for each user."""

# For scrub
from . import user

# Name of current table
_tablename = ''

def _set_tablename(username):
	# Allows changing the value of global var tablename
	global _tablename
	"""Sets tablename based on the username obtained from user module."""
	_tablename = 'contacts_' + username
	_tablename = user._scrub(_tablename)


def show_all_contacts():
	"""Shows all contacts in a user's contact table along with the total contact count.
	Returns a tuple containing all the contacts. If there are no contacts, returns False"""
	pass


def add_contact():
	"""Adds a contact to the contacts table.
	Returns true if successful"""
	pass


def delete_contact(choice):
	"""Deletes contact based on the user input from the contacts table/
	Returns true if successful"""
	pass


def search_contact():
	"""Searches a contact in the current table and prints all relevant matches.
	Returns a tuple containing all the matches. If no matches are found, returns False"""
	pass


def import_csv():
	"""Imports a CSV and stores the data into table.
	Returns true if successful"""
	pass


def export_csv():
	"""Exports contents of table to a csv file. Input name from user
	Returns true if successful"""
	pass