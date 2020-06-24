# import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/username/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
driver.implicitly_wait(4)

# Send input
input_field = driver.find_element(By.ID, 'helpsearch')
input_field.clear()
input_field.send_keys('Cancel order')


# click enter
search_icon = driver.find_element(By.XPATH, "//input[@class='a-button-input']")
search_icon.click()

# verify that correct search result is present
text = driver.find_element(By.XPATH, "//h1[text() = 'Cancel Items or Orders']").text
assert text == 'Cancel Items or Orders'

# close the window
driver.quit()


