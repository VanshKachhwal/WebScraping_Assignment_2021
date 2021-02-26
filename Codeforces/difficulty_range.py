from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys 
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(PATH, options = options)
start = sys.argv[1]
end = sys.argv[2]
number = int(sys.argv[3])

driver.get("https://codeforces.com/problemset/?tags=" + start + "-" + end)

indexElementDiv = driver.find_element_by_class_name("pagination")
indexElementUl = indexElementDiv.find_element_by_tag_name("ul")
indexElements = indexElementUl.find_elements_by_tag_name("li")
MAX_INDEX = int(indexElements[-2].text)

problems = []

for index in range(1,MAX_INDEX+1):

	driver.get("https://codeforces.com/problemset/page/" + str(index) + "?tags=" + start + "-" + end)

	table = driver.find_element_by_class_name("datatable")
	rows = table.find_elements_by_tag_name("tr")
	

	for row in rows:

		if row == rows[0]:
			continue

		if number == 0:
			break

		columns = row.find_elements_by_tag_name("td")
		problems.append(columns[0].find_element_by_tag_name("a").get_attribute("href"))

		number-=1


	if number == 0:
		break

os.mkdir("Difficulty_Range_"+start+"-"+end)
a = os.getcwd()

for problem in problems:
	driver.get(problem)
	ls = problem.split("/")

	b = a + '/' + "Difficulty_Range_" + start + "-" +  end + '/' + ls[-2] + ls[-1]
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
