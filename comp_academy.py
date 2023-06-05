from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
# import logging

# Set up logging
# logging.basicConfig(filename='academy_logs.log', level=logging.INFO,
#                   format='%(asctime)s - %(levelname)s - %(message)s')


# Set up ChromeDriver options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


# service = Service(ChromeDriverManager().install())
# executable_path = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(service=service, options=chrome_options)
webdriver_service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=webdriver_service)
driver.maximize_window()


# Set up ChromeDriver instance
# driver = webdriver.Chrome(service=service, options=chrome_options, executable_path=executable_path)
# driver.maximize_window()

# logging.info("Navigating to https://alnafi.academy/")
driver.get("https://alnafi.academy/auth/signin")
time.sleep(20)

# logging.info("entering email")
driver.find_element(By.XPATH, "//input[@id='Email / Username']").send_keys("hanfi.kh99@gmail.com")
time.sleep(2)

# logging.info("password")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("123456789@aA")
time.sleep(2)

# logging.info("clicking on sign in button")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
time.sleep(10)
# logging.info("SIgn in successful")
# Confirm button click
driver.find_element(By.XPATH, "(//button[normalize-space()='Confirm'])[1]").click()
time.sleep(10)
print("login successful")
# logging.info("pressing 'go to home' button")
# driver.find_element(By.XPATH, "//button[normalize-space()='Go to home']").click()
# time.sleep(10)
# logging.info("main page opened")

# scene
# logging.info("pressing tab 'about us'")
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='About Academy'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("about us OK ")
# logging.info('About us successfully opened and closed')

# scene 2
# logging.info("pressing tab 'faculty'")
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='Faculty'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("Faculty OK")
# logging.info("faculty successfully opened and closed")

# scene 3
# logging.info("pressing tab 'schedule'")
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='Schedule'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("schedule OK")
# logging.info("schedule successfully opened and closed")

# scene 3
# logging.info("pressing tab student resources")
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='Student Resources'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("Student resources OK")
# logging.info("student resources successfully opened and closed ")

# logging.info("clicking on download button of different papers")
yearly_past_papers = driver.find_element(By.XPATH, "(//a[@href='/student-resources/yearly-past-papers'])[1]")
topical_past_papers = driver.find_element(By.XPATH, "(//a[@href='/student-resources/topical-past-papers'])[1]")
subject_notes = driver.find_element(By.XPATH, "(//a[@href='/student-resources/subject-notes'])[1]")
quiz = driver.find_element(By.XPATH, "(//a[@href='/student-resources/quiz'])[1]")

###############################################
yearly_past_papers.click()
time.sleep(10)
driver.back()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("download past papers button clicked and OK")
#
# topical_past_papers.click()
# time.sleep(10)
# driver.back()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 500)")
# time.sleep(10)
# print("download button clicked")
#
# subject_notes.click()
# time.sleep(10)
# driver.back()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 500)")
# time.sleep(10)
# print("download button clicked")
#
# quiz.click()
# time.sleep(10)
# driver.back()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 500)")
# time.sleep(10)
# print("download button clicked")
#
# scene
# logging.info("navigating to pricing page")
driver.get("https://alnafi.academy/pricing")
time.sleep(10)
# verify price
# logging.info("monthly bundle price verification")
# monthly_bundle_price = driver.find_element(By.XPATH, "(//div[@class='flex flex-col gap-2 text-purpleHeart font-bold text-[50px]'])[2]")
# time.sleep(2)
# monthly_act_price = "10000"
# time.sleep(2)
# assert monthly_act_price == monthly_bundle_price.text, "Text not found in the element"
# time.sleep(2)
monthly_bundle_price = driver.find_element(By.XPATH, "(//div[@class='flex flex-col gap-2 text-purpleHeart font-bold text-[50px]'])[2]")
# Get the text of the element
actual_text = monthly_bundle_price.text
# Expected text
expected_text = "85 Per Month"
# Compare the actual and expected text
if actual_text == expected_text:
    print("Text matches!")
else:
    print("Text does not match!")
driver.find_element(By.XPATH, "(//span[@class='text-brightGray font-medium flex items-center gap-3 px-20 py-5 cursor-pointer w-max'][normalize-space()='Buy Now'])[2]").click()
driver.find_element(By.XPATH, "(//label[@for='22'])[1]").click()
driver.find_element(By.XPATH, "(//label[@for='18'])[1]").click()
driver.find_element(By.XPATH, "(//label[@for='24'])[1]").click()
print("plan select success")
time.sleep(5)

# logging.info("processing to checkout")
driver.find_element(By.XPATH, "(//button[normalize-space()='Go to Checkout'])[1]").click()
time.sleep(10)

# logging.info("entering easypaisa account number")
driver.find_element(By.XPATH, "(//input[@id='easypaisa_number_input'])[1]").send_keys("0316")
time.sleep(10)

# logging.info("clicking on pay button")
driver.find_element(By.XPATH, "(//button[normalize-space()='Pay'])[1]").click()
# logging.info("verify the easypaisa payment on your phone")
time.sleep(25)

driver.quit()
