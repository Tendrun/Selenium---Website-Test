from selenium import webdriver
from booking.booking import Booking

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-search-engine-choice-screen")

with Booking(chrome_options, False) as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_place_to_go(place_to_go="New York")
    bot.select_dates(check_in_date='2024-08-22', check_out_date='2024-08-31')

input("Press Enter to close the browser...")