import yaml
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Function to load credentials from the YAML file
def load_credentials(file_path='config.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load username and password from the YAML file
credentials = load_credentials()
username = credentials['linkedin']['username']
password = credentials['linkedin']['password']

# Initialize the WebDriver (using Firefox in this case)
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to LinkedIn login page
driver.get("https://linkedin.com/login")
driver.implicitly_wait(15)

# Wait until the username field is present and then input the username
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)

# Input the password
driver.find_element(By.ID, "password").send_keys(password)

# Click the login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.implicitly_wait(15)

def scroll_down(driver, num):
    body_elem = driver.find_element(By.TAG_NAME, "body")
    for _ in range(num):
        body_elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)  # Add a small delay to ensure the page loads

SCROLL_PAUSE_TIME = 10
prev_height = driver.execute_script("return document.body.scrollHeight")

# Scroll down in a loop
for i in range(0, 500):
    scroll_down(driver, 1)
    time.sleep(SCROLL_PAUSE_TIME)  # Wait to allow new items to load
    
    # Get the new scroll height and compare with the previous one
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height and i > 0:
        break
    prev_height = new_height

# Pause to keep the browser open for review
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
