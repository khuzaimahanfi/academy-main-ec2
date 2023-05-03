## incomplete script
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import logging

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
driver.find_element(By.XPATH, "//input[@id='Email / Username']").send_keys("hanfi.kh99@gmail.com")
time.sleep(2)

logging.info("password")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("123456789@aA")
time.sleep(2)

logging.info("clicking on sign in button")
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
time.sleep(10)

logging.info("pressing 'go to home' button")
driver.find_element(By.XPATH, "//button[normalize-space()='Go to home']").click()
time.sleep(10)

# scene
logging.info("pressing tab 'about us'")
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='About Academy'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print('about us success')

# scene 2
logging.info("pressing tab 'faculty'")
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='Faculty'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("faculty success")

# scene 3
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='Schedule'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("schedule success")

# scene 3
logging.info("pressing tab ")
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='Student Resources'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("faculty success")

yearly_past_papers = driver.find_element(By.XPATH, "(//a[@href='/student-resources/yearly-past-papers'])[1]")
topical_past_papers = driver.find_element(By.XPATH, "(//a[@href='/student-resources/topical-past-papers'])[1]")
subject_notes = driver.find_element(By.XPATH, "(//a[@href='/student-resources/subject-notes'])[1]")
quiz = driver.find_element(By.XPATH, "(//a[@href='/student-resources/quiz'])[1]")

download_options ={"yearly_past_papers", "topical_past_papers", "subject_notes", "quiz"}
for download_option in download_options:
    download_options.click()

