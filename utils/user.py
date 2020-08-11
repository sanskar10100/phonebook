"""Module for user table management."""

import contacts

# TODO: Write __user_exists function
def _user_exists():
	pass


def _input_credentials():
	"""Inputs and returns username and password."""
	username = input('Username: ')
	password = input('Password: ')

	return (username, password)


def add_user():
	"""Adds user to database if doesn't exist and create a contacts table for him.
	Returns a string indicating the status
	"""
	username, password = _input_credentials()

	if _user_exists(username, password):
		return "The user already exists"
	else:
		# TODO: Add user to users table
		# TODO: Create contacts table for user. Name: contacts_username
		return "User successfully added"


def remove_user():
	"""Removes a user and associated contact table from the database.
	Returns a string indicating the status
	"""
	username, password = _input_credentials()

	if _user_exists(username, password):
		# TODO: Remove user from users table
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
