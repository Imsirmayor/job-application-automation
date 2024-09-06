from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

username = "replace_with_actual_email"
password = "replace_with_actual_password"

# driver = webdriver.Firefox()  uncommemt this line, comment chrome webriver to use fireforx
driver = webdriver.Chrome("chromedriver")  # Change this to the appropriate WebDriver for your browser
driver.get("https://linkedin.com/login")  # Replace with the desired URL
driver.find_element("id", "login_field").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element("name", "commit").click()


# Examples of browser actions
driver.refresh()  # Refresh the current page


driver.back()  # Navigate back to the previous page
driver.forward()  # Navigate forward to the next page




# input("Press Enter to close the browser...")
# driver.quit()
