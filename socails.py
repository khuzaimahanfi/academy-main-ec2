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

driver.find_element(By.XPATH, "//img[@src='/_ipx/_/icons/facebook.svg']").click()
time.sleep(5)
print("facebook-success")
driver.find_element(By.XPATH, "//img[@alt='yotube']").click()
time.sleep(5)
print("youtube-success")
driver.find_element(By.XPATH, "//img[@src='/_ipx/_/icons/linkedin.svg']").click()
time.sleep(5)
print("linked-in-success")

driver.quit()