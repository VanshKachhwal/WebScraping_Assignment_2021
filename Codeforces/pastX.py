from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys 
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(PATH, options = options)
number = int(sys.argv[1])

driver.get("https://codeforces.com/contests")

indexElementDiv = driver.find_element_by_class_name("pagination")
indexElementUl = indexElementDiv.find_element_by_tag_name("ul")
indexElements = indexElementUl.find_elements_by_tag_name("li")
MAX_INDEX = int(indexElements[-2].text)

for index in range(1,MAX_INDEX+1):

	driver.get("https://codeforces.com/contests/page/" + str(index))

	tables = driver.find_elements_by_class_name("datatable")
	rows = tables[1].find_elements_by_tag_name("tr")
	contests = []

	for row in rows:

		if row == rows[0]:
			continue

		if number == 0:
			break

		contest = row.get_attribute("data-contestid")
		contests.append(contest)
		number-=1

	for contest in contests:

		os.system("python fetch_round.py " + contest )

	if number == 0:
		break

driver.quit()