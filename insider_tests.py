from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())

try:
    # 1. Open the Insider homepage
    driver.get("https://useinsider.com")
    print("Opened Insider homepage")
    time.sleep(2)  # Wait for the page to load

    # 2. Navigate to the Careers page and verify blocks
    careers_link = driver.find_element(By.LINK_TEXT, "Careers")
    careers_link.click()
    print("Navigated to Careers page")
    time.sleep(2)

    # Verify blocks on the Careers page
    teams_block = driver.find_element(By.XPATH, "//h3[contains(text(), 'Teams')]")
    locations_block = driver.find_element(By.XPATH, "//h3[contains(text(), 'Locations')]")
    print("Verified Teams and Locations blocks")

    # 3. Filter jobs by Istanbul, Turkey and Quality Assurance
    driver.get("https://useinsider.com/careers/open-positions/")
    time.sleep(2)

    # Select location (Istanbul, Turkey)
    location_filter = driver.find_element(By.XPATH, "//select[@name='location']")
    location_filter.send_keys("Istanbul, Turkey")
    time.sleep(1)

    # Select department (Quality Assurance)
    department_filter = driver.find_element(By.XPATH, "//select[@name='department']")
    department_filter.send_keys("Quality Assurance")
    time.sleep(1)

    # 4. Verify that all jobs match the criteria
    job_listings = driver.find_elements(By.CLASS_NAME, "job-listing")
    for job in job_listings:
        title = job.find_element(By.CLASS_NAME, "job-title").text
        location = job.find_element(By.CLASS_NAME, "job-location").text
        department = job.find_element(By.CLASS_NAME, "job-department").text

        assert "Istanbul, Turkey" in location, f"Job {title} is not in Istanbul, Turkey"
        assert "Quality Assurance" in department, f"Job {title} is not in Quality Assurance"
        print(f"Verified job: {title}")

    # 5. Click on "View Role" and verify the application page
    view_role_button = job_listings[0].find_element(By.LINK_TEXT, "View Role")
    view_role_button.click()
    time.sleep(2)

    # Verify the application page
    assert "Apply" in driver.page_source, "Application page did not load correctly"
    print("Verified application page")

finally:
    # Close the browser
    driver.quit()
