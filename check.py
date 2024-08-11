from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("chrome://version/")
version = driver.find_element_by_css_selector("body > table > tbody > tr:nth-child(1) > td:nth-child(2)").text
print(f"Chrome version: {version}")
driver.quit()