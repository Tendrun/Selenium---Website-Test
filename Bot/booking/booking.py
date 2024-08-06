import booking.constants as const
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, options, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)