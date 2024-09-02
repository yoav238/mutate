from datetime import time
import time
from selenium.webdriver.common.by import By

from WebFunction import search_and_download
from FileFunctions import read_csv_to_string_array, move_latest_pdb_file
from FileFunctions import move_latest_file
from FileFunctions import list_files_in_folder
import rotkit
from pymol import cmd
from ryr_h_beniS import mutate
from FileFunctions import read_csv_to_double_array
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

cmd.reinitialize()

print(os.getenv('CHROME_DRIVER_PATH'))

print((os.getenv('CHROME_DRIVER_PATH')) is None)

filesInInput = list_files_in_folder(r'C:/Users/User/OneDrive/Documents/Mutaion/InputFiles')


# Set up Chrome options (ensure the browser is not headless)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# Set preferences for downloading files
prefs = {
    "download.default_directory": "C:\\Users\\User\\OneDrive\\Documents\\Mutaion\\OutputFiles",  # Specify your Jenkins download path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}

chrome_options.add_experimental_option("prefs", prefs)

# Use ChromeDriverManager to download and setup ChromeDriver
chromedriver_dir = os.path.dirname(ChromeDriverManager().install())
if os.getenv('CHROME_DRIVER_PATH') is None:

    chromedriver_path = os.path.join(chromedriver_dir, "chromedriver.exe")
else:
    chromedriver_path = os.getenv('CHROME_DRIVER_PATH')

print(f"Using ChromeDriver at: {chromedriver_path}")  # Added for debugging

# Check if the correct chromedriver.exe exists
if not os.path.exists(chromedriver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {chromedriver_path}")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

print(driver.capabilities['browserVersion'])

driver.get("https://www.rcsb.org/")
outputFolder = "C:/Users/User/OneDrive/Documents/Mutaion/OutputFiles"
element = driver.find_element(By.CLASS_NAME, "mainnav_title.hidden-xs")
text = element.text
print("Extracted Text:", text)
print(len(filesInInput))

for protienName in filesInInput:
    protienName = protienName.replace(".csv", "")
    print(protienName)
    search_and_download(driver, protienName)
    #move_latest_pdb_file("C:/Users/User/Downloads", outputFolder)

    # Mutate
    protienName = protienName.replace("T", "t")
    filesInOutput = list_files_in_folder(r'C:/Users/User/OneDrive/Documents/Mutaion/OutputFiles')
    for value in filesInOutput:
        print(value)
    cmd.load(outputFolder + "/" + protienName + ".pdb")

    csv_file_path = r'C:/Users/User/OneDrive/Documents/Mutaion/InputFiles/' + protienName + '.csv'
    time.sleep(2)
    patho = read_csv_to_double_array(csv_file_path)
    mutate(cmd, patho)
    print(protienName + " is done")
    cmd.reinitialize()

driver.quit()
