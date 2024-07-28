from datetime import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def my_function():
    print("Hello from my_function!")


def search_and_download(driver, protein):
    input_field = driver.find_element(By.ID, 'search-bar-input-text')
    driver.maximize_window()

    input_field.send_keys(protein)

    # Optionally, you can submit the form if needed
    input_field.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds

    # Wait for the element to exist
    print('//table[@class="results-item-header"]//h3/a[contains(@href,"'+protein+'")]')

    searchResult = wait.until(EC.presence_of_element_located((By.XPATH,'//table[@class="results-item-header"]//h3/a[contains(@href,"'+protein+'")]')))

    #searchResult = driver.find_element(By.XPATH,'//table[@class="results-item-header"]//*[contains(@href,"'+protein+'")]')
    #searchResult = driver.find_element(By.XPATH,'//table[@class="results-item-header"]//h3/a[contains(@href,"4ZTO")]')
    searchResult.click()
    driver.find_element(By.ID, 'dropdownMenuDownloadFiles').click()

    driver.find_element(By.XPATH,'//*[@class="dropdown-menu pull-right"]//a[contains(@href,"download") and contains(text(),"PDB Format")]').click()

    time.sleep(5)