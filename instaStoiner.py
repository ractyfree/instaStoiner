from classes.ChromeDriver import *
from classes.Instagram import *
from classes.InstagramLinkEndpoints import *



	







class InstaStoiner:

	TIMEOFSTORY = 30

	def __init__(self, login, password, users_list=[], storviewcnt=100000, cookies=False, tabs=3):
		self.login = login
		self.password = password
		self.users_list = users_list
		self.storviewcnt = storviewcnt
		self.cookies = cookies
		self.tabs = tabs
		
		
	def __makeQueue(self):
		queue = []
		tab = 0
		for x in self.users_list:
			if tab > self.tabs:
				tab = 0
			queue.append([x,tab])
			tab+=1
		return queue

	def start(self):
		browser = ChromeDriverClass(self.cookies, self.tabs)
		insta = Instagram(self.login, self.password, browser)
		insta.doLogin()
		# We are logged in! Now we can iterate through all users and watch their stories multionausly
		browser.makeNewTabs()
		tabs = browser.getAllTabs()

		for x in self.__makeQueue():
			print(x)
			browser.switchTab(tabs[x[1]])
			insta.viewStory(x[0])
			if x[1] == self.tabs:
				time.sleep(10)
			time.sleep(1)



		




	


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)

	insta = InstaStoiner("cruslah", "SpreadingMethod117", users_list=["afshin_tur", "suciangelic", "sani._.one", "khabib_nurmagomedov", "chemodan_prk", "elizabeth__9980"], cookies=False)
	print(insta.start())

	#print(insta.makeQueue())