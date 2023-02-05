from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import random
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# place holder for Data/variables
first = "Gyandeep"
last = "Kumar"
email = "gruwaneukofau-5672@yopmail.com"
DOB = "01-01-1994"
phone = "9845265489"
street = "Alelo"
APT = "5"
city = "Waipahu"
state = "hawai"
zip = "41014"
height = "6.0"
weight = "190"
answer_1 = "This a text given for only testing purpose"
onset = "2019-12"
duration = "4"
recovery = "full"
answer_2 = "Gyandeep kumar lorem ipsum. This a text given for only testing purpose"

class SignupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Initialization of webdriver for chrome
        cls.driver = webdriver.Chrome(executable_path= "C:\Driver\chromedriver.exe")
        # Initialization of webdriver for chrome(If required to test on firefox then comment out the webdriver for chrome and initilize the firefox)
        # cls.driver=webdriver.Firefox()

        cls.driver.get("https://d3j8nuwp74eyml.cloudfront.net/5U5PU/S2xbn/UGFnZV8w")
        #verifying the title
        # assert "Select Application" in cls.driver.title
        # Maximizing window for better view.
        cls.driver.maximize_window()
        # A 60 sec implicit wait.
        cls.driver.implicitly_wait(60)
    def test_01_get_started(self):
        # Locate the Get started button button and click on it.
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Welcome")

    def test_02_Applicant_type(self):
        # Locate and checkmark Employee
        employee_radio = self.driver.find_element(By.XPATH, "//input[@name='answer'][@tabindex='1']")
        employee_radio.click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Applicant Type")

    def test_03_Product(self):
        # Locate and checkmark Short term disability
        employee_radio = self.driver.find_element(By.XPATH, "//input[@name='answers.1'][@tabindex=2]")
        employee_radio.click()
        # Here we can select multiple options so we are going to select one more option
        # Locate and checkmark supplemental life
        time.sleep(2)
        employee_radio = self.driver.find_element(By.XPATH, "//input[@name='answers.0'][@tabindex=1]")
        employee_radio.click()
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Product")

    def test_04_your_name(self):
        # Locate first name and input text
        first_name= self.driver.find_element(By.NAME, "first")
        first_name.send_keys(first)
        # Locate last name and input text
        last_name = self.driver.find_element(By.NAME, "last")
        last_name.send_keys(last)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Name")


    def test_05_email(self):
        # Locate email and send input text
        email_input = self.driver.find_element(By.NAME, "answer")
        email_input.send_keys(email)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Email")

    def test_06_Select_a_coverage_amount(self):
        # locate the slider handel and drag it by 40 px in X direction
        slider = self.driver.find_element(By.CLASS_NAME, 'rc-slider-handle')
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 40, 0).perform()
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Coverage")
        time.sleep(5)

    def test_07_date_of_birth(self):
        DOB_input = self.driver.find_element(By.ID, "date")
        DOB_input.send_keys(DOB)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Date of birth")

    def test_08_Gender(self):
        male_input = self.driver.find_element(By.XPATH, "//input[@name='answer'][@tabindex='1']")
        male_input.click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Gender")

    def test_09_phone_number(self):
        time.sleep(5)
        ph_input = self.driver.find_element(By.NAME, "answer")
        ph_input.send_keys(phone)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Phone")

    def test_10_address(self):
        # Locate and click on "I can't find my address"
        self.driver.find_element(By.XPATH, "//div[@class='underline cursor-pointer text-primary-main']").click()
        time.sleep(4)
        # Locate 'enter a address' and send input text
        street_input = self.driver.find_element(By.NAME, "address.street")
        street_input.send_keys(street)
        # Locate 'APT/Unit' and send input text
        apt_input = self.driver.find_element(By.ID, "apt_unit")
        apt_input.send_keys(APT)
        # Locate 'enter a address' and send input text
        city_input = self.driver.find_element(By.NAME, "address.city")
        city_input.send_keys(city)
        # Locate 'enter a address' and send input text
        state_input = self.driver.find_element(By.NAME, "address.state")
        state_input.click()
        # We can use any one of the following method to select hawai from the dropdown

        # time.sleep(2)
        # state_input.send_keys("h")
        # time.sleep(2)
        # state_input.send_keys(Keys.ENTER)

        # Select the dropdown element by its ID attribute
        dropdown = Select(self.driver.find_element(By.ID, "state"))
        # Select the desired option using its value attribute
        dropdown.select_by_value("HI")

        # Locate 'Zip code' and send input text
        zip_input = self.driver.find_element(By.NAME, "address.zipCode")
        zip_input.send_keys(zip)
        # Locate and checkmark on two checkmarks
        self.driver.find_element(By.NAME, "isAuthReleaseAgree").click()
        self.driver.find_element(By.NAME, "isConsentBusiness").click()
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Address")

    def test_11_What_is_your_height_and_weight(self):
        # Locate 'height' and send input text
        hight_input = self.driver.find_element(By.NAME, "height")
        hight_input.click()
        # Select the dropdown element by its ID attribute
        dropdown = self.driver.find_element(By.ID, "height")
        dropdown.click()
        # Select the desired option using its value attribute(6'0")
        dropdown.send_keys("6")
        time.sleep(1)
        dropdown.send_keys(Keys.ENTER)
        # Locate 'weight' and send input text
        weight_input = self.driver.find_element(By.NAME, "weight")
        weight_input.send_keys(weight)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Height & Weight")

    def test_12_Codition(self):
        """"" There are multiple options here also we can select multiple options at once
        but to keep the testcases simple we are going to only select one option and
        follow its flow"""
        # locate and checkmark "Type I/Insulin-Dependent Diabetes"
        self.driver.find_element(By.NAME, "answers.8").click()
        time.sleep(2)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Question")

    def test_13_Type_I_Insulin_Dependent_Diabetes(self):
        #Locate the txt fiels and input text
        detail_input = self.driver.find_element(By.NAME, "answer")
        detail_input.send_keys(answer_1)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Hepatitis B or C")
        time.sleep(10)


    def test_14_onset(self):
        # Locate the date fiels and input text
        date_input = self.driver.find_element(By.NAME, "answer")
        date_input.send_keys(onset)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Hepatitis B or C")
        time.sleep(10)

    def test_15_duration(self):
        # Locate the duration fiels and input text
        duration_input = self.driver.find_element(By.NAME, "answer")
        duration_input.send_keys(duration)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Hepatitis B or C")
        time.sleep(10)

    def test_16_Degree_of_recovery(self):
        # Locate the duration fiels and input text
        recovery_input = self.driver.find_element(By.NAME, "answer")
        recovery_input.send_keys(recovery)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Hepatitis B or C")
        time.sleep(10)

    def test_17_Name_address_phone_of_attending_physician(self):
        # Locate the duration fiels and input text
        recovery_input = self.driver.find_element(By.NAME, "answer")
        recovery_input.send_keys(answer_2)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Hepatitis B or C")
        time.sleep(10)

    def test_18_following_condition(self):
        # locate and checkmark "none of the above"
        self.driver.find_element(By.NAME, "noneOfAbove").click()
        time.sleep(2)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Question")
        time.sleep(10)

    def test_19_indicated_above(self):
        # locate and checkmark on yes
        self.driver.find_element(By.ID, "yes").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Question")
        time.sleep(10)


    def test_20_details_of_yes_answer(self):
        # Locate the duration fiels and input text
        details_input = self.driver.find_element(By.NAME, "answer")
        details_input.send_keys(answer_2)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Consultation")
        time.sleep(10)

    def test_21_consultation_onset(self):
        # Locate the date fiels and input text
        date_input = self.driver.find_element(By.NAME, "answer")
        date_input.send_keys(onset)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Consultation")
        time.sleep(10)

    def test_22_consultation_duration(self):
        # Locate the duration fiels and input text
        duration_input = self.driver.find_element(By.NAME, "answer")
        duration_input.send_keys(duration)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Consultation")
        time.sleep(10)

    def test_23_Degree_of_recovery(self):
        # Locate the duration fiels and input text
        recovery_input = self.driver.find_element(By.NAME, "answer")
        recovery_input.send_keys(recovery)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Consultation")
        time.sleep(10)

    def test_24_Name_address_phone_of_attending_physician(self):
        # Locate the duration fiels and input text
        recovery_input = self.driver.find_element(By.NAME, "answer")
        recovery_input.send_keys(answer_2)
        # locate and click on the next button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Consultation")
        time.sleep(10)

    def test_25_medication(self):
        # Locate and checkmark on 'no"
        self.driver.find_element(By.ID, "no").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Question")
        time.sleep(10)

    def test_26_review_application(self):
        # Locate first name and input text
        first_name = self.driver.find_element(By.ID, "first_name")
        first_name.send_keys(first)
        # Locate last name and input text
        last_name = self.driver.find_element(By.ID, "last_name")
        last_name.send_keys(last)
        # locate and click on the sign your application button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "Review")
        time.sleep(10)

    def test_27_download_your_application(self):
        # Locate and click on "download PDF" button
        # locate and click on the sign your application button
        self.driver.find_element(By.XPATH, "//button[@type='button']").click()
        # Asserting the title and verifying it.
        title = self.driver.title
        print(title)
        self.assertTrue(title == "All completed")
        # here we need to enter the OTP received in the given mail we are doing it manually
        time.sleep(30)
        # Also we are not getting any OTP in our mail as tere is no payload in the API https://uyitte0e54.execute-api.us-west-2.amazonaws.com/dev/life/app/wEwc3-0/generate

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(30)
        cls.driver.quit()
        print("Test completed")