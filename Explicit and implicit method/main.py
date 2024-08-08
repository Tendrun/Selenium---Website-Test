from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(10)
my_element = driver.find_element("id", "downloadButton")
my_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),  # Element filtration
        'Complete!'  # The expected text
    )
)

# input("Press Enter to close the browser...")
