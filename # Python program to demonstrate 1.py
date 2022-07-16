# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome(r"C:\Users\welcome\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")

# get google.co.in
driver.get("https://google.co.in")
element = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")


