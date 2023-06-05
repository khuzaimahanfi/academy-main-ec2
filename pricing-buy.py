import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

# Set up logging
logging.basicConfig(filename='selenium_logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Set up ChromeDriver options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())
executable_path = "/usr/local/bin/chromedriver"  # executable on your EC2 instance

# Set up ChromeDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options, executable_path=executable_path)
driver.maximize_window()

logging.info("Navigating to https://alnafi.academy/")
driver.get("https://alnafi.academy/auth/signin")
time.sleep(20)

logging.info("entering user name")
driver.find_element(By.XPATH, "//input[@id='Email / Username']").send_keys("hanfi.kh99@gmail.com")
time.sleep(2)

logging.info("entering password")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("123456789@aA")
time.sleep(2)

logging.info("clicking on 'sign in' button")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
time.sleep(20)

logging.info("clicking on 'go to home' button")
driver.find_element(By.XPATH, "//button[normalize-space()='Go to home']").click()
time.sleep(15)
# scene
logging.info("navigating to to pricing page")
driver.get("https://alnafi.academy/pricing")
time.sleep(10)
# verify price
logging.info("monthly bundle price verification")
# monthly_bundle_price = driver.find_element(By.XPATH, "(//div[@class='flex flex-col gap-2 text-purpleHeart font-bold text-[50px]'])[2]")
# time.sleep(2)
# monthly_act_price = "10000 Per Month"
# time.sleep(2)
# assert monthly_act_price == monthly_bundle_price.text, "Text not found in the element"
# time.sleep(2)
monthly_bundle_price = driver.find_element(By.XPATH, "(//div[@class='flex flex-col gap-2 text-purpleHeart font-bold text-[50px]'])[2]")

# Get the text of the element
actual_text = monthly_bundle_price.text

# Expected text
expected_text = "10000 Per Month"

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

logging.info("processing to checkout")
driver.find_element(By.XPATH, "(//button[normalize-space()='Go to Checkout'])[1]").click()
time.sleep(10)

logging.info("entering easypaisa account number")
driver.find_element(By.XPATH, "(//input[@id='easypaisa_number_input'])[1]").send_keys("0316******")
time.sleep(5)

logging.info("clicking on pay button")
driver.find_element(By.XPATH, "(//button[normalize-space()='Pay'])[1]").click()
time.sleep(25)
driver.quit()
