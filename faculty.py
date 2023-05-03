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
driver.get("https://alnafi.academy/auth/signin")
time.sleep(20)

email_input = driver.find_element(By.XPATH, "//input[@id='Email / Username']")
email_input.send_keys("hanfi.kh99@gmail.com")
time.sleep(2)
password_input = driver.find_element(By.XPATH, "//input[@id='Password']")
password_input.send_keys("123456789@aA")
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
time.sleep(10)

driver.find_element(By.XPATH, "//button[normalize-space()='Go to home']").click()
time.sleep(20)

driver.get("https://alnafi.academy/faculty")
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
print("successful")
driver.quit()
