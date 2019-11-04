

class InstagramLinkEndpoints:


	loginPage = "https://www.instagram.com/accounts/login"
	mainPage = "https://www.instagram.com/"


	def buildProfilePage(username):
		return "https://www.instagram.com/" + username + "/"

	def buildStoriesPage(username):
		return "https://www.instagram.com/stories/" + username + "/"



