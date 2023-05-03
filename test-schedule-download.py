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

driver.find_element(By.XPATH, "//input[@id='Email / Username']").send_keys("hanfi.kh99@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("123456789@aA")
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
time.sleep(10)
driver.find_element(By.XPATH, "//button[normalize-space()='Go to home']").click()
time.sleep(10)
# scene 3
driver.find_element(By.XPATH, "(//a[@class='py-3 text-gray-700 hover:text-[#6813CC] focus:text-purpleHeart text-sm font-medium transition-colors duration-300 transform'][normalize-space()='Student Resources'])[1]").click()
time.sleep(10)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
print("student resources success")

yearly_past_papers = driver.find_element(By.XPATH, "(//a[@href='/student-resources/yearly-past-papers'])[1]")
topical_past_papers = driver.find_element(By.XPATH, "(//a[@href='/student-resources/topical-past-papers'])[1]")
subject_notes = driver.find_element(By.XPATH, "(//a[@href='/student-resources/subject-notes'])[1]")
quiz = driver.find_element(By.XPATH, "(//a[@href='/student-resources/quiz'])[1]")

download_options = ["yearly_past_papers", "topical_past_papers", "subject_notes", "quiz"]
for download_option in download_options:
    download_options.click()
