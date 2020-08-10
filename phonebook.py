"""Integration and Front-End module"""


import utils.user
import utils.contacts


def input_user_menu_choice():
	"""Displays user management options and returns user's input choice"""
	print('1. Add user')
	print('2. Delete user')
	print('3: Select user')
	choice = int(input('Input choice: '))

	if choice < 1 or choice > 3:
		raise Exception('Invalid choice')
	else:
		return choice


def input_contact_menu_choice():
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
	user_menu_choice = input_user_menu_choice()
	contact_menu_choice = input_contact_menu_choice()
