from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
#Launch the chrome browser
chrome_driver_path=r"E:\GUVI\chromedriver.exe"
chrome_service=ChromeService(chrome_driver_path)
driver=webdriver.Chrome(service=chrome_service)
# Open Saucedemo Url

driver.get("https://www.saucedemo.com/")
# print current url page
current_url = driver.current_url
print("Current URL:", current_url)

# print current page title
driver.title
page_title = driver.title
print("Page Title:", page_title)

# Extract the entire page content
page_source = driver.page_source

# Save the content in a text file
with open("webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)