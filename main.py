from WebFunction import search_and_download
from FileFunctions import read_csv_to_string_array
from FileFunctions import move_latest_file
from FileFunctions import list_files_in_folder
import rotkit
import cmd
from pymol import cmd
from ryr_h_beniS import mutate
from FileFunctions import read_csv_to_double_array
cmd.reinitialize()
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


filesInInput = list_files_in_folder(r'C:/Users/User/OneDrive/Documents/Mutaion/InputFiles')
print(filesInInput)

# Set up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()

# Initialize the WebDriver with ChromeDriverManager
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.rcsb.org/")
outputFolder = "C:/Users/User/OneDrive/Documents/Mutaion/OutputFiles"

print(len(filesInInput))

for protienName in filesInInput:
    protienName = protienName.replace(".csv","")
    # Perform an action with each value, e.g., printing it

    print(protienName)
    search_and_download(driver,protienName)
    move_latest_file("C:/Users/User/Downloads", outputFolder)

    # Mutate
    cmd.load(outputFolder+"/"+protienName+".pdb")
    csv_file_path = r'C:/Users/User/OneDrive/Documents/Mutaion/InputFiles/'+protienName+'.csv'
    patho = read_csv_to_double_array(csv_file_path)
    mutate(cmd, patho)
    print(protienName+" is done")
    cmd.reinitialize()

driver.quit()







