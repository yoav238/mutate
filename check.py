from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Download and get the path of ChromeDriver
chrome_driver_path = ChromeDriverManager().install()
print(f"ChromeDriver is located at: {chrome_driver_path}")

# Check if the path is valid
import os
print(f"Path exists: {os.path.exists(chrome_driver_path)}")