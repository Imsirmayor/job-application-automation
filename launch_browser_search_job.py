import yaml
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Function to load credentials from the YAML file
def load_credentials(file_path='config.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load username and password from the YAML file
credentials = load_credentials()
username = credentials['linkedin']['username']
password = credentials['linkedin']['password']

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Firefox()
driver.maximize_window()

# Navigate to LinkedIn login page
driver.get("https://linkedin.com/login")

# Wait until the username field is present and then input the username
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)

# Input the password
driver.find_element(By.ID, "password").send_keys(password)

# Click the login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Explicitly wait for the 'Jobs' link to be clickable, then click it
jobs_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Jobs')))
jobs_link.click()

# Search based on keywords and location and hit enter
search_keywords = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-search-box__text-input[aria-label='Search jobs']")))
search_keywords.clear()
search_keywords.send_keys("Software Engineer")  # Replace with actual keywords

search_location = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input[aria-label='Search location']")
search_location.clear()
search_location.send_keys("New York")  # Replace with actual location
search_location.send_keys(Keys.RETURN)

# Pause to keep the browser open for review
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
