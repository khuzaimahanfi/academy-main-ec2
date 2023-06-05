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
chrome_options.add_argument('--headless')
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

logging.info("entering email")
email_input = driver.find_element(By.XPATH, "//input[@id='Email / Username']")
email_input.send_keys("hanfi.kh99@gmail.com")
time.sleep(2)

logging.info("password")
password_input = driver.find_element(By.XPATH, "//input[@id='Password']")
password_input.send_keys("123456789@aA")
time.sleep(2)

logging.info("clicking on sign in button")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
time.sleep(10)

logging.info("pressing 'go to home' button")
driver.find_element(By.XPATH, "//button[normalize-space()='Go to home']").click()
time.sleep(20)

logging.info("pressing tab faculty")
driver.get("https://alnafi.academy/faculty")
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
print("successful")
driver.quit()
