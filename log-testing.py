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
driver.get("https://alnafi.academy/")
time.sleep(20)

logging.info("Clicking on 'Sign up' button")
driver.find_element(By.XPATH, "(//a[normalize-space()='Sign up'])[1]").click()
time.sleep(5)

logging.info("Entering username")
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("a")
time.sleep(5)

logging.info("Entering first name")
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("a")
time.sleep(5)

logging.info("Entering last name")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("a")
time.sleep(5)

logging.info("Entering email")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("a")
time.sleep(5)

logging.info("Entering password")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("a")
time.sleep(5)

logging.info("Confirming password")
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("a")
time.sleep(5)

logging.info("Entering contact information")
driver.find_element(By.XPATH, "//input[@id='contact']").send_keys("a")
time.sleep(5)

logging.info("Entering address")
driver.find_element(By.XPATH, "//input[@id='address']").send_keys("a")
time.sleep(5)

logging.info("Submitting form")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(20)

logging.info("Closing the webdriver")
driver.quit()
