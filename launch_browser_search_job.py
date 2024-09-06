# import yaml
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Function to load credentials from the YAML file
# def load_credentials(file_path='config.yaml'):
#     with open(file_path, 'r') as file:
#         return yaml.safe_load(file)

# # Load username and password from the YAML file
# credentials = load_credentials()
# username = credentials['linkedin']['username']
# password = credentials['linkedin']['password']

# # Initialize the WebDriver (Chrome in this case)
# driver = webdriver.Chrome()

# # Navigate to LinkedIn login page
# driver.get("https://linkedin.com/login")

# # Wait until the username field is present and then input the username
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)

# # Input the password
# driver.find_element(By.ID, "password").send_keys(password)

# # Click the login button
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# # Pause to keep the browser open for review
# input("Press Enter to close the browser...")

# # Close the browser
# driver.quit()


import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Function to load credentials and search parameters from the YAML file
def load_config(file_path='config.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to login to LinkedIn
def linkedin_login(driver, username, password):
    driver.get("https://linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Function to search for and apply to jobs based on the config
def search_and_apply_jobs(driver, config):
    for position in config['positions']:
        for location in config['locations']:
            # Navigate to LinkedIn Jobs search page
            driver.get("https://www.linkedin.com/jobs/")
            time.sleep(3)  # Wait for the page to load

            # Enter the job position
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Search jobs')]")))
            search_box.clear()
            search_box.send_keys(position)
            time.sleep(1)  # Small delay for typing simulation

            # Enter the location
            location_box = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search location')]")
            location_box.clear()
            location_box.send_keys(location)
            time.sleep(1)
            location_box.send_keys(Keys.RETURN)

            time.sleep(3)  # Wait for search results to load

            # Filter remote jobs if specified
            if config.get('remote'):
                remote_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Remote')]")))
                remote_filter.click()
                time.sleep(3)

            # Extract and click on job listings
            job_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
            for job in job_listings:
                try:
                    job.click()
                    time.sleep(2)  # Wait for the job details to load

                    # Check for company and title blacklist
                    company_name = driver.find_element(By.CSS_SELECTOR, ".jobs-unified-top-card__company-name").text
                    job_title = driver.find_element(By.CSS_SELECTOR, ".jobs-unified-top-card__job-title").text

                    if any(blacklisted in company_name for blacklisted in config['companyBlacklist']):
                        print(f"Skipping {job_title} at {company_name} (blacklisted company)")
                        continue

                    if any(blacklisted in job_title for blacklisted in config['titleBlacklist']):
                        print(f"Skipping {job_title} (blacklisted title)")
                        continue

                    # Apply for the job
                    apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button--top-card")))
                    apply_button.click()
                    time.sleep(2)  # Wait for the application form to load

                    # Fill out the application form (adjust as necessary for the form structure)
                    phone_field = driver.find_element(By.CSS_SELECTOR, "[id^='single-line-text-form-component']")
                    phone_field.send_keys("0000000000")  # Example placeholder value, adjust as needed

                    # Submit the application
                    submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
                    submit_button.click()

                    print(f"Applied for {job_title} at {company_name}")

                except Exception as e:
                    print(f"Error applying to job: {e}")
                    continue

            # Delay between job searches to avoid rate-limiting
            time.sleep(5)

# Main function
def main():
    # Load configuration
    config = load_config()

    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        # Log in to LinkedIn
        linkedin_login(driver, config['linkedin']['username'], config['linkedin']['password'])

        # Search for and apply to jobs
        search_and_apply_jobs(driver, config)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
