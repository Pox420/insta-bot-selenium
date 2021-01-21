from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# import username and password
from username_password import username,paasword

# import other function
from follow_suggestion_people import follow_suggested_people
from follow_people_from_page import follow_people_from_page
from unfollow_users import unfollow_users

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.instagram.com/'
driver.get(url)

# sets five seconds of waiting time.
# if Selenium can’t find an element, then it waits for five seconds to allow everything to load and tries again.
driver.implicitly_wait(5)
driver.set_window_size(1024, 720)
driver.maximize_window()

user = username
passwrd = paasword

username = driver.find_element_by_name('username')
username.send_keys(user)
time.sleep(3)

password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
password.send_keys(passwrd)
time.sleep(4)

driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()
time.sleep(3)

try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
except:
    pass
time.sleep(4)

try:
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
except:
    pass
time.sleep(4)


# follow_suggested_people()
follow_people_from_page(driver=driver,time=time,random=random)
# unfollow_users()