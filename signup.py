from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

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
driver.get("https://alnafi.academy/")
time.sleep(20)
driver.find_element(By.XPATH, "(//a[normalize-space()='Sign up'])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='contact']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='address']").send_keys("a")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(20)
