from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "replace"
password = "replace"

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# Navigate to LinkedIn login page
driver.get("https://linkedin.com/login")

# Wait until the username field is present and then input the username
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)

# Input the password
driver.find_element(By.ID, "password").send_keys(password)

# Click the login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Pause to keep the browser open for review
input("Press Enter to close the browser...")

# Close the browser
driver.quit()