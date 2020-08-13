"""phonebook is a simple contact management tool written in python.
It hosts seperate phonebooks or contact lists for each user (that's right, we support multiple users)
Offers user management options like addition, removal and selection.
Also offers contact management option for each user, like addition, deletetion, searching etc
It also supports import and export of most CSV files for contacts
"""


from utils import user

def _input_user_menu_choice():
	"""Displays user management options and returns user's input choice"""
	print('\n')
	print('1. Add user')
	print('2. Delete user')
	print('3: Select user')
	choice = int(input('Input choice: '))

	if choice < 1 or choice > 3:
		raise Exception('Invalid choice')
	else:
		return choice


def _input_contact_menu_choice():
	"""Displays contact management options and returns user's input choice"""
	print('1. Show all contacts')
	print('2. Add contact')
	print('3. Delete contact')
	print('4. Search contact')
	print('5. Import CSV')
	print('6. Export CSV')
	print('7. Switch to user management mode')

	choice = int(input('Input choice: '))

	if choice < 1 or choice > 6:
		raise Exception('Invalid choice')
	else:
		return choice


if __name__ == "__main__":
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
		else:
			if user.select_user() is True:
				print('User successfully selected')
				break
			else:
				print('Could not select user')

