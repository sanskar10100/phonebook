"""phonebook is a simple contact management tool written in python.

It hosts seperate phonebooks or contact lists for each user (that's right, we support multiple users)
Offers user management options like addition, removal and selection.
Also offers contact management option for each user, like addition, deletetion, searching etc
It also supports import and export of most CSV files for contacts
"""


from utils import user
from utils import contacts
from utils import helper

def _input_user_menu_choice():
	"""Displays user management options and returns user's input choice"""
	print()
	print('--------------------')
	print('User Management Menu')
	print('--------------------')
	print()
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
	print()
	print('-----------------------')
	print('Contact Management Menu')
	print('-----------------------')
	print()
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
	try:
		while True:
			user_choice = _input_user_menu_choice()
			if user_choice == 1:
				if user.add_user() is True:
					print('User successfully added')
				else:
					print('Error: user already exists')
			elif user_choice == 2:
				if user.remove_user() is True:
					print('User successfully removed')
				else:
					print('Error: user does not exist')
			elif user_choice == 3:
				if user.select_user() is True:
					print('User successfully selected')
					break
				else:
					print('Error: user does not exist')
			else:
				helper.trigger_exit()
	except EOFError:
		_user_management()


def _contacts_management():
	"""Processes contact management menu input."""
	# Redraw contact management menu until user exits.
	try:
		while True:
			print('Contact Management Menu')
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
				if contacts.search_contact() is False:
					print('Contact lookup failed')
			elif contacts_choice == 5:
				if contacts.import_csv() is True:
					print('CSV import successful')
				else:
					print('CSV import failed')
			elif contacts_choice == 6:
				if contacts.export_csv() is True:
					print('CSV export successful')
				else:
					print('CSV export failed')
			elif contacts_choice == 7:
				helper.clear_screen()
				_user_management()
			else:
				helper.trigger_exit()
	except EOFError:
		_contacts_management()

if __name__ == "__main__":
	try:
		_user_management()
		helper.clear_screen()
	except KeyboardInterrupt:
		helper.trigger_exit()
	
	try:
		_contacts_management()
		helper.clear_screen()
	except KeyboardInterrupt:
		helper.trigger_exit()