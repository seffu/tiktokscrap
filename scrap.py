# import os
# # PATH = os.environ['PATH2']
# from selenium import webdriver

# PATH = "/home/skn/Desktop/Projects/python/regular/worldleading/wlselenium/"
# driver = webdriver.Firefox(PATH)

# driver.get('https://www.google.com')

# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.utils import os_architecture

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get('https://app.popularpays.com/search/off-platform?brandId=bf0f61a7-c6d1-46ad-9926-40ba0356bd3a&follower_count_gteq=50000')
# username = driver.find_element_by_id("identification")
# password = driver.find_element_by_id("password")
# login = driver.find_element_by_class_name("button")
# username.sendKeys("seffu.kioi@zalda.net");
# password.sendKeys("Rawadh2020&");
# login.click();

# username = "seffu.kioi@zalda.net"
# password = "Rawadh2020&"
# driver.find_element_by_id("identification").send_keys(username)
# # find password input field and insert password as well
# driver.find_element_by_id("password").send_keys(password)
# # click login button
# driver.find_element_by_class_name("button").click()


# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.utils import os_architecture
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get('http://www.facebook.com')
# username = driver.find_element_by_id("email")
# password = driver.find_element_by_id("pass")
# submit   = driver.find_element_by_name("login")
# username.send_keys("you@email.com")
# password.send_keys("yourpassword")
# submit.click()


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import os_architecture
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://app.popularpays.com/search/off-platform?brandId=bf0f61a7-c6d1-46ad-9926-40ba0356bd3a&follower_count_gteq=50000')

element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("identification"))
username = driver.find_element_by_id("identification")
password = driver.find_element_by_id("password")
submit   = driver.find_element_by_class_name("button--full-width")
username.send_keys("your-email")
password.send_keys("your-password")
submit.click()



# def scroll(driver):


    # scroll_pause_time = timeout
    # # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     # Wait to load page
    #     time.sleep(scroll_pause_time)
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         # If heights are the same it will exit the function
    #         break
    #     last_height = new_height

element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("ember66"))

# time.sleep(2)  # Allow 2 seconds for the web page to open
# scroll_pause_time = 5 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
# screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
# i = 1
# while True:
#     # scroll one screen height each time
#     print('in the while')
#     driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
#     i += 1
#     time.sleep(scroll_pause_time)
#     # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
#     scroll_height = driver.execute_script("return document.body.scrollHeight;")  
#     # Break the loop when the height we need to scroll to is larger than the total scroll height
#     if (screen_height) * i > scroll_height:
#         break 


SCROLL_PAUSE_TIME = 30
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

data = driver.find_elements_by_class_name("off-platform-profile")
full_list = []
for items in data:
    details = []
    handle = items.find_element_by_class_name("off-platform-profile__handle")
    details.append(handle.text)
    name = items.find_element_by_class_name("off-platform-profile__name")
    details.append(name.text)
    followers = items.find_element_by_class_name("off-platform-profile__stat-value")
    details.append(followers.text)
    # if items.find_element_by_class_name("off-platform-profile__email-text"):
    #     email = items.find_element_by_class_name("off-platform-profile__email-text")
    full_list.append(details)
print(full_list)
print(len(full_list))