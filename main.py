users={}
status=""

def displayMenu():
	status=input("are you a registered user? y/n press q to quit")
	if status=="y":
		oldUser()
	elif status=="n":
		newUser()


def newUser():
	createLogin=input("Create UserName:")

	if createLogin in users:
		print("\nuser already exists\n")
	else:
		createPassw = input("create Password")
		users[createLogin]=createPassw
		print("\nUser created\n")

def oldUser():
	login =input("\nEnter UserName:")
	passw =input("\nEnter Password:")

	if login in users and users[login]==passw:
		print("\nlogin success")
	else:
		print("\nWrong Password")

	while status!="g":

		displayMenu()
