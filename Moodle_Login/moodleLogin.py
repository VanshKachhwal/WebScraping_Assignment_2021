from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys 

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")

loginId = driver.find_element_by_id("username")
username = sys.argv[1]
loginId.send_keys(username)

pwd = driver.find_element_by_id("password")
password = sys.argv[2]
pwd.send_keys(password)

captcha = driver.find_element_by_id("login")

st = captcha.text
ls = st.split(" ")

flag = 1
for i in range(len(ls)):
    if ls[i] == '+':
        res = int(ls[i-1]) + int(ls[i+1])
        break
    elif ls[i] == '-':
        res = int(ls[i-1]) - int(ls[i+1])
        break
    elif ls[i] == 'second':
        flag = 2
    elif ls[i] == ',':
        if flag == 1:
            res = int(ls[i-1])
        else:
            res = int(ls[i+1])
        break

captchaAnswer = driver.find_element_by_id("valuepkg3")
captchaAnswer.clear()

captchaAnswer.send_keys(str(res))    
submit_button = driver.find_element_by_id("loginbtn")
submit_button.click()

