from selenium import webdriver
import os
import booking.constants as const
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r'C:\selenium-drivers', tear_down = False):
        self.driver_path = driver_path
        self.tear_down = tear_down
        os.environ['PATH'] += driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tear_down:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)


    def change_currency(self, currency= None):
        currency_element = self.find_element(by=By.CSS_SELECTOR, value = "button[data-tooltip-text='Choose your currency']")
        currency_element.click()
        selected_currency_element = self.find_element(by=By.CSS_SELECTOR, value=f"a[data-modal-header-async-url-param='changed_currency=1;selected_currency={currency}']")
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_fild = self.find_element(by=By.ID, value='ss')
        search_fild.clear()
        search_fild.send_keys(place_to_go)
        place = self.find_element(by=By.CSS_SELECTOR, value="li[data-i='0']")
        place.click()


    def search_date(self, check_in, check_out):
        check_in_date = self.find_element(by=By.CSS_SELECTOR,value=f"td[data-date='{check_in}']")
        check_in_date.click()
        check_out_date = self.find_element(by=By.CSS_SELECTOR,value=f"td[data-date='{check_out}']")
        check_out_date.click()

    def search_adults(self,count = 1):
        adults = self.find_element(by=By.ID, value="xp__guests__toggle")
        adults.click()

        while True:

            decrease_adults = self.find_element(by=By.CSS_SELECTOR,
                                                    value="button[data-bui-ref='input-stepper-subtract-button']")

            decrease_adults.click()

            adult_count = self.find_element(by=By.ID,value="group_adults")
            adult_count_ = adult_count.get_attribute('value')

            if int(adult_count_)==1:
                break


        if count>1:
            count = count-1
            increase_adults = self.find_element(by=By.CSS_SELECTOR,
                                                value="button[data-bui-ref='input-stepper-add-button']")
            for i in range(0,count):
                increase_adults.click()

    def search_children(self,count = 0, age_list = []):
        if len(age_list) == count:
            while True:
                decrease_button = self.find_element(by=By.CSS_SELECTOR,value='button[aria-label="Decrease number of Children"]')
                decrease_button.click()

                children_count = self.find_element(by=By.ID,value='group_children')
                children_count_ = children_count.get_attribute('value')

                if int(children_count_) == 0:
                    break

            if count>0:
                for i in range(0,count):
                    increase_button = self.find_element(by=By.CSS_SELECTOR,value='button[aria-label="Increase number of Children"]')
                    increase_button.click()

            for i in range(0,count):
                age_element = self.find_element(by=By.CSS_SELECTOR, value=f'select[aria-label="Child {i+1} age"]')
                age_element.click()
                selection = self.find_element(by=By.XPATH, value=f'//*[@id="xp__guests__inputs-container"]/div/div/div[3]/select[{i+1}]/option[{age_list[i]+2}]')
                selection.click()

        else:
            print("Please enter the age rightly")
    def search_room(self,count):
        while True:
            decrease_room_element = self.find_element(by=By.CSS_SELECTOR,value='button[aria-label="Decrease number of Rooms"]')
            decrease_room_element.click()

            room_element = self.find_element(by=By.ID, value='no_rooms')
            room_element_count = room_element.get_attribute('value')
            if int(room_element_count) == 1:
                break
        count -=1
        if count> 1:
            for i in range(0,count):
                increase_button = self.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Increase number of Rooms"]')
                increase_button.click()


    def search_all_possible_situation(self):
        submit = self.find_element(by=By.CSS_SELECTOR, value='button[data-sb-id="main"]')
        submit.click()

