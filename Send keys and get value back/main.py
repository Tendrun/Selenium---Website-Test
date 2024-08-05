from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open google chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://planetcalc.com/8183/")
driver.implicitly_wait(10)

# agree to policy
driver.find_element("class name", "css-47sehv").click()

# send number to add
text_area = driver.find_element("xpath", "//textarea")
text_area.click()
text_area.clear()
text_area.send_keys(Keys.NUMPAD1, Keys.NUMPAD2)  # 12
text_area.send_keys(Keys.SPACE)
text_area.send_keys(Keys.NUMPAD3, Keys.NUMPAD4)  # 34

# get result
calculate_button = driver.find_element("id", "dialogv6411c55e0cc72_calculate")
calculate_button.click()
output_value = driver.find_element("id", "dialogv6411c55e0cc72_sum")
print(output_value.text)

input("Press Enter to close the browser...")
