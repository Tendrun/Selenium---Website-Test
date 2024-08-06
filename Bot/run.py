from selenium import webdriver
from booking.booking import Booking

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-search-engine-choice-screen")

with Booking(chrome_options, False) as bot:
    bot.land_first_page()
    print("Exiting....")

input("Press Enter to close the browser...")