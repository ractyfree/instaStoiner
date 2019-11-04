from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pickle
import os
import random
import time






class ChromeDriverClass:



	CHROMEDRIVERRPATH = "bin/chromedriver.exe"
	COOKIESFILE = "cookies.pkl"
	DEFAULTTIMEOUT = 3

	def __init__(self, cookies = False, tabs=3):
		self.driver = self.getBrowser()
		self.tabs = tabs
		if self.__isThereCookies() and cookies == True:
			self.__loadCookies

	def getBrowser(self):
		return webdriver.Chrome(executable_path=self.CHROMEDRIVERRPATH)

	def makeNewTabs(self):
		for _ in range(0, self.tabs):
			self.driver.execute_script("window.open('');")

	def switchTab(self, tab):
		return self.driver.switch_to_window(tab)

	def getAllTabs(self):
		return self.driver.window_handles
		

	def openPage(self, page):
		return self.driver.get(page)

	def locateElemXpath(self, xpath):
		return self.driver.find_element_by_xpath(xpath)

	def openPageWaitForElem(self, page, xpath):
		self.openPage(page)
		WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))

	def saveCookies(self):
		pickle.dump(self.driver.get_cookies(), open(self.COOKIESFILE, "wb"))

	def __loadCookies(self):
		cookies = pickle.load(open(self.COOKIESFILE, "rb"))
		for x in cookies:
			self.driver.add_cookie(cookie)

	def __isThereCookies(self):
		return os.path.exists(self.COOKIESFILE)

	def sendTextForm(self, text, xpath):
		inputForm = self.locateElemXpath(xpath)
		for x in text:
			inputForm.send_keys(x)
			time.sleep(0.05)