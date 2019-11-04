

import os
import random
import time
import logging
import sys

from classes.InstagramLinkEndpoints import *

class Instagram:


	def __init__(self, login, password, browser):
		self.login = login
		self.password = password
		self.browser = browser


	def doLogin(self):

		self.browser.openPageWaitForElem(InstagramLinkEndpoints.loginPage, "//input[@name='username']")

		inputLogin  = self.browser.sendTextForm(self.login, "//input[@name='username']")
		inputPassword = self.browser.sendTextForm(self.password, "//input[@name='password']")

		showPassword = self.browser.locateElemXpath("//div/button[@class='sqdOP yWX7d     _8A5w5    ']")
		showPassword.click()

		logging.info("YOU NOW NEED TO CLICK ON 'LOGIN' BUTTON FOR YOURSELF AND THEN SKIP NOTIFICATION! YOU HAVE 15 SECONDS!")

		time.sleep(15)


	def viewStory(self, username):
		try:
			self.browser.openPageWaitForElem(InstagramLinkEndpoints.buildStoriesPage(username), "//div[@class='_7UhW9   xLCgt      MMzan         h_zdq uL8Hv         ']")
			self.browser.locateElemXpath("//div[@class='_7UhW9   xLCgt      MMzan         h_zdq uL8Hv         ']").click()
		except:
			return "Seems like user doesn't have a story!"
		#time.sleep(2)

	

