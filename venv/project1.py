from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/seleniumwebdriver/chromedriver.exe')  #execute selenium
driver.get("https://buyme.co.il/") #open Buyme site
driver.find_element_by_class_name("seperator-link").click()  #clicking on registration\login button
driver.find_element_by_class_name("text-btn").click()  #clicking registration button
driver.find_element_by_id("ember1019").send_keys("adir") #clicking first name field and enter firstname
driver.find_element_by_id("ember1021").send_keys("asss323@gmmm.com") #clicking email field and filling it
driver.find_element_by_id("valPass").send_keys("12345678As") #entering password
driver.find_element_by_id("ember1025").send_keys("12345678As")  #entering confirm password
driver.execute_script("arguments[0].click();",driver.find_element_by_class_name("fa-check"))  #checking radio button
driver.find_element_by_xpath("//button[@type='submit']").click()   #clicking on submit

time.sleep(5)  # 5 seconds delay
drop_down = driver.find_elements_by_class_name("chosen-single")    #assigning all availabe dropdowns into variable
drop_down[0].click()
price_points = driver.find_elements_by_class_name("active-result")  #selecting suitable price from drop down
price_points[1].click()

#continue
drop_down2 = driver.find_elements_by_class_name("chosen-single")  #assigning all availabe dropdowns into variable
drop_down2[1].click()
price_points = driver.find_elements_by_class_name("active-result")  #selecting area from drop down
price_points[3].click()

drop_down3 = driver.find_elements_by_class_name("chosen-single")  #assigning all availabe dropdowns into variable
drop_down3[2].click()
price_points = driver.find_elements_by_class_name("active-result")  #selecting category from drop down
price_points[3].click()


driver.find_element_by_id("ember723").click()   #clicking on search button


time.sleep(5)
driver.find_elements_by_class_name('card-item')[2].click()  #clicking of prefered buissnes

time.sleep(5)
driver.find_element_by_id("ember1162").send_keys("500")  #entering price

driver.find_element_by_xpath("//button[@type='submit']").click() #pressing on submit button

time.sleep(5)
driver.find_element_by_id("ember1278").send_keys("moshe")  #entering reciver name

driver.find_element_by_id("ember1280").send_keys("adir israeli")  #entering sender name


driver.find_element_by_xpath("//*[@id='ember1298']/textarea").send_keys("mazl tov monkey")  #writing some blessing

driver.find_element_by_id("ember1307").send_keys('C:/Users/adir.israeli/Pictures/1.jpg') #upload local picture



drop_down7 = driver.find_element_by_id("ember1282_chosen")    #pressing on event radio button
drop_down7.click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="ember1282_chosen"]/div/ul/li[2]').click()  #choosing an event

driver.find_element_by_class_name("btn-send-option-inner").click()  #selecting SMS

driver.find_element_by_id("ember1749").send_keys("0545454545")   #filling recipient phone
driver.find_element_by_id("resendReciver").send_keys("0546969696")  #filling sender phone



time.sleep(3)
driver.find_element_by_xpath("//button[@type='submit']").click()  #saving reciver+sender phones


driver.find_element_by_xpath("//button[@type='submit']").click()   #submit








