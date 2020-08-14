"""phonebook is a simple contact management tool written in python.

It hosts seperate phonebooks or contact lists for each user (that's right, we support multiple users)
Offers user management options like addition, removal and selection.
Also offers contact management option for each user, like addition, deletetion, searching etc
It also supports import and export of most CSV files for contacts
"""


from utils import user
from utils import contacts
import sys
import time

def _trigger_exit():
	"""Initiates the exit sequence."""
	print('\nExiting phonebook!')
	time.sleep(0.3)
	sys.exit(1)


def _input_user_menu_choice():
	"""Displays user management options and returns user's input choice"""
	print('\n')
	print('1. Add user')
	print('2. Delete user')
	print('3. Select user')
	print('4. Exit')
	choice = int(input('Input choice: '))

	if choice < 1 or choice > 4:
		raise Exception('Invalid choice')
	else:
		return choice


def _input_contact_menu_choice():
	"""Displays contact management options and returns user's input choice"""
	print('\n')
	print('1. Show all contacts')
	print('2. Add contact')
	print('3. Delete contact')
	print('4. Search contact')
	print('5. Import CSV')
	print('6. Export CSV')
	print('7. Switch to user management mode')
	print('8. Exit')

	choice = int(input('Input choice: '))

	if choice < 1 or choice > 8:
		raise Exception('Invalid choice')
	else:
		return choice


def _user_management():
	"""Processes user management menu input"""
	# Redraw user management menu until a user is successfully selected
	while True:
		user_choice = _input_user_menu_choice()
		if user_choice == 1:
			if user.add_user() is True:
				print('User successfully added')
			else:
				print('Error: Could not add user')
		elif user_choice == 2:
			if user.remove_user() is True:
				print('User successfully removed')
			else:
				print('Error: Could not remove user')
		elif user_choice == 3:
			if user.select_user() is True:
				print('User successfully selected')
				break
			else:
				print('Could not select user')
		else:
			_trigger_exit()


def _contacts_management():
	"""Processes contact management menu input."""
	# Redraw contact management menu until user exits.
	while True:
		contacts_choice = _input_contact_menu_choice()
		if contacts_choice == 1:
			contacts.show_all_contacts()
		elif contacts_choice == 2:
			if contacts.add_contact() is True:
				print('Contact added successfully')
			else:
				print('Could not add contact')
		elif contacts_choice == 3:
			if contacts.delete_contact() is True:
				print('Contact deleted successfully')
			else:
				print('Contact not found')
		elif contacts_choice == 4:
			contacts.search_contact()
		elif contacts_choice == 5:
			contacts.import_csv()
		elif contacts_choice == 6:
			contacts.export_csv()
		elif contacts_choice == 7:
			_user_management()
		elif contacts_choice == 8:
			_trigger_exit()



if __name__ == "__main__":
	try:
		_user_management()
	except KeyboardInterrupt:
		_trigger_exit()
	
	try:
		_contacts_management()
	except KeyboardInterrupt:
		_trigger_exit()
