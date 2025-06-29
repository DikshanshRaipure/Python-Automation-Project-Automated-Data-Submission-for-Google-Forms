import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

filename = 'test.csv'
df = pd.read_csv(filename)
data = df.to_dict('records')

time.sleep(7)

XPATHS = {
    'Email' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Register Joining Code' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'ID No.' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Age in Company (Years)' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Age' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Weight in Kgs' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Father Name' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Date Joining' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Password' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Region' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'City' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'First Name' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input',
    "Mother's Name" : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Middle Initial' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input',
    "Mother's Maiden Name" : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Place Name' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Salary' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div/div[1]/input',
    '% Salary Hike' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Country' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Date of Birth' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'Last Name' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/div[1]/div/div[1]/input',
    'submit' : '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
}

# Start the Chrome browser
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
time.sleep(2)

form_url = "https://forms.gle/32zsHBCAF5fVcQ6v8"

for entry in data:
    driver.get(form_url)  # Open the form
    time.sleep(5)  # Wait for the page to load

    # Fill each field using its XPATH
    driver.find_element(By.XPATH, XPATHS["Email"]).send_keys(entry["Email"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Register Joining Code"]).send_keys(entry["Register Joining Code"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["ID No."]).send_keys(entry["ID No."])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Age in Company (Years)"]).send_keys(entry["Age in Company (Years)"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Age"]).send_keys(entry["Age"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Weight in Kgs"]).send_keys(entry["Weight in Kgs"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Father Name"]).send_keys(entry["Father Name"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Date Joining"]).send_keys(entry["Date Joining"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Password"]).send_keys(entry["Password"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Region"]).send_keys(entry["Region"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["City"]).send_keys(entry["City"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["First Name"]).send_keys(entry["First Name"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Mother's Name"]).send_keys(entry["Mother's Name"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Middle Initial"]).send_keys(entry["Middle Initial"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Mother's Maiden Name"]).send_keys(entry["Mother's Maiden Name"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Place Name"]).send_keys(entry["Place Name"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Salary"]).send_keys(entry["Salary"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["% Salary Hike"]).send_keys(entry["% Salary Hike"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Country"]).send_keys(entry["Country"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Date of Birth"]).send_keys(entry["Date of Birth"])
    time.sleep(0.5)
    driver.find_element(By.XPATH, XPATHS["Last Name"]).send_keys(entry["Last Name"])
    time.sleep(0.5)

    # Click the submit button
    driver.find_element(By.XPATH, XPATHS["submit"]).click()
    time.sleep(2)  # Wait for submission to complete

    # Optionally, handle "Submit another response"
    # You can find its XPATH and click it if you want to submit more entries
    
input("Press Enter to exit and close the browser...")
driver.quit()
