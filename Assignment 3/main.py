# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(11)

# Step 2: Go to "All" at the top left corner and select "Bestsellers"
all_dropdown = driver.find_element("xpath", "(//span[@class='hm-icon-label'])[1]")
all_dropdown.click()

time.sleep(2)

# go to bestseller in all category
bestsellers_link = driver.find_element("xpath", "(//a[@class='hmenu-item'][normalize-space()='Best Sellers'])[1]")
bestsellers_link.click()

time.sleep(2)

# Going through arrow key present in the website to browse more products
next_arrow = driver.find_element("xpath", "(//i[@class='a-icon a-icon-next'])[1]")
next_arrow.click()

time.sleep(2)

# selecting an element
click_item = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/ol/li/div/div[2]/div/a[1]/div/img")
click_item.click()

time.sleep(2)

# clicking ratings
ratings = driver.find_element("xpath", "(//span[@id='acrCustomerReviewText'])[1]")
ratings.click()

time.sleep(2)

# clicking one star element
one_star = driver.find_element("xpath", "(//div[@role='progressbar'])[5]")
one_star.click()

time.sleep(2)

# in ask question bar asking question without question mark to generate error message
question_bar = driver.find_element("xpath", "(//textarea[@id='askQuestionFormId'])[1]")
question_bar.send_keys("aaaa")

time.sleep(2)

ask_key = driver.find_element("xpath", "(//input[@value='Ask'])[1]")
ask_key.click()

time.sleep(2)

# clearing the question textbox
question_bar.clear()

# asking question with question mark
question_bar = driver.find_element("xpath", "(//textarea[@id='askQuestionFormId'])[1]")
question_bar.send_keys("aaaa?")

time.sleep(2)

ask_key = driver.find_element("xpath", "(//input[@value='Ask'])[1]")
ask_key.click()





time.sleep(3)





driver.quit()


