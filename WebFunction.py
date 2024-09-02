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
    print('//table[@class="results-item-header"]//h3/a[contains(@href,"' + protein + '")]')
    element_xpath = '//table[@class="results-item-header"]//h3/a[contains(@href,"' + protein + '")]'

    wait_for_element_exists(driver, element_xpath, 20)
    time.sleep(1)
    #searchResult = driver.find_element(By.XPATH,'//table[@class="results-item-header"]//*[contains(@href,"'+protein+'")]')
    #searchResult = driver.find_element(By.XPATH,'//table[@class="results-item-header"]//h3/a[contains(@href,"4ZTO")]')
    searchResult = driver.find_element(By.XPATH, element_xpath)
    searchResult.click()
    time.sleep(1)
    driver.find_element(By.ID, 'dropdownMenuDownloadFiles').click()
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//*[@href='/fasta/entry/1T60']")
    text = element.text
    print("Extracted Text line 43 : ", text)
    wait_for_element_exists(driver,'//*[@class="dropdown-menu pull-right"]//a[contains(@href,"download") and contains(text(),"PDB Format")]',5)
    driver.find_element(By.XPATH,'//*[@class="dropdown-menu pull-right"]//a[contains(@href,"download") and contains(text(),"PDB Format")]').click()
    time.sleep(5)


def wait_for_element_exists(driver, xpath, waitSec):
    """Check if an element exists by XPath."""
    i = 0
    while (len(driver.find_elements(By.XPATH, xpath)) < 1) and waitSec > i:
        time.sleep(1)  # Wait for 1 second before checking again
        i += 1
        print(f"Waiting... {i} seconds passed")
    return waitSec > i
