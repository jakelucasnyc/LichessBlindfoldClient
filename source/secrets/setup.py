import time

def main():
	with open('secrets.py', 'w') as f:

		username = input('Please enter your lichess username (Case-Sensitive): ')

		f.write(f'USERNAME = "{str(username).strip()}"')

	apiToken = input('Please create a lichess API token and paste it here: ')

	with open('lichess.token', 'w') as f:

		f.write(str(apiToken).strip())


	print('Setup Complete. Happy Blindfold!')
	time.sleep(4)



if __name__ == '__main__':
	main()
