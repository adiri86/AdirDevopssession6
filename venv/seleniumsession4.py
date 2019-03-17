#selenium - webautomation

import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/seleniumwebdriver/chromedriver.exe')
# # driver.implicitly_wait(10) #will give a chance up to 10 secondes for the web page to load
# driver.get("https://translate.google.com/")
# driver.find_element_by_id("source").click()   #button which i want selenium to click on it
# driver.find_element_by_id("source").send_keys("hello")
# driver.find_element_by_id("source").clear()
# my_button = driver.find_element_by_id("source")  #configure some variable in order to perform verification in a row after
# print(my_button.is_displayed())



# print(driver.current_url)         #will show us our current url we are watching
# print(driver.title)       #will show us the tab's name
# print(driver.page_source)      # will show us the page source(you can send it to a specific file)
# driver.close();       #will close current tab


# #using locators

# my_button = driver.find_elements_by_name("abc")  #all names with abc
# my_list = driver.find_elements_by_id("abc")
# x = my_list[30]  #find the 30th element in the page-using index
#

#xpath locator (absolute path)
# my_button = driver.find_element_by_xpath(/html[@class='gr__translate_google_com']/body[@class='rtl-display-lang displaying-homepage']/div[@class='frame']/div[@class='page tlid-homepage homepage translate-text']/div[@class='homepage-content-wrap']/div[@class='tlid-source-target main-header']/div[@class='source-target-row']/div[@class='tlid-results-container results-container empty'])
#
#

#controlles
#
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/seleniumwebdriver/chromedriver.exe')
# driver.get("https://www.facebook.com/")
# driver.find_element_by_id("source").click()   #button that i want selenium to click on it



#keyboards

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/seleniumwebdriver/chromedriver.exe')
# driver.get("https://translate.google.com/")
# from selenium.webdriver.common.keys import Keys      #IMPORT OPTIONS TO USE KEYbord keys
# driver.find_element_by_id("source").send_keys(Keys.ENTER)
