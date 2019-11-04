from instaStoiner import*



def readFile(filename):
	f = open(filename, "r")
	ret = []
	for x in f:
		ret.append(x)
	return ret

if __name__ == "__main__":
	users = readFile("users_cruslah.txt")

	insta = InstaStoiner("YOUR_LOGIN", "YOUR_PASSWORD", users_list=users)
	insta.start()

	


