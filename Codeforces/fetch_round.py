from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys 
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(PATH, options = options)
contest = sys.argv[1]
os.mkdir(str(contest))
a = os.getcwd()

driver.get("https://codeforces.com/contest/"+contest)

table = driver.find_element_by_class_name("problems")
rows = table.find_elements_by_tag_name("tr")
problems = []

for row in rows:
	if row == rows[0]:
		continue
	columns = row.find_elements_by_tag_name("td")
	# problems.append(columns[0].text)
	problems.append(columns[0].find_element_by_tag_name("a").get_attribute("href"))

for problem in problems:

	# driver.get("https://codeforces.com/problemset/problem/" + str(contest) + '/' + problem)
	driver.get(problem)
	title = driver.find_element_by_class_name("title")
	ls = problem.split("/")
	b = a + '/' + str(contest) + '/' + ls[-1]
	os.mkdir(b)
	S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
	driver.set_window_size(S('Width'),S('Height'))
	element = driver.find_element_by_class_name("problem-statement")
	element.screenshot(b+'/'+"problem.png")
	io = driver.find_elements_by_class_name("input-output-copier")
	flag = 0
	no = 1
	for i in io:
		target = i.get_attribute('data-clipboard-target')
		data = driver.find_element_by_css_selector(target)
		if flag == 0:
			f = open(b + '\input' + str(no) + '.txt','w')
			f.write(data.text)
			f.close
			flag = 1
		elif flag == 1:
			f = open(b + '\output' + str(no) + '.txt','w')
			f.write(data.text)
			f.close
			flag = 0
			no+=1

	
driver.quit()




