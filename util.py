from datetime import datetime
from selenium import webdriver 
import requests
import time
import random
from timeit import default_timer as timer

# pip install selenium etc..

# 0.
def start_program():  
  now = datetime.now()
  current_time = now.strftime("%Y-%m-%d %H:%M:%S")
  print(
  """
  -------------------------------------------------
  Custom Web Scraper 
  Simonas Mulevičius
  https://github.com/simonasmulevicius
  """ + 
  current_time +
  """
  -------------------------------------------------
  """)

# 1.
def get_user_input():
  return input("Enter a link: ") 

# 2.
def validate_URL(url):
  return url.startswith("https://") or url.startswith("http://")

# 3.
def get_valid_URL():
  url = get_user_input()
  while(not(validate_URL(url))):
    url = get_user_input()
  return url

# 4.
def get_html(url):
  requestObject = requests.get(url)
  return requestObject.text


# 5.
def get_all_links_in_page(driver, url):
  driver.get(url)
  links = driver.find_elements_by_css_selector("a")
  for link in links:
    print("LINK:" + link.get_attribute("href"))

# 7.
def get_title(driver, url):
  driver.get(url)
  return driver.title

def test__get_title__when_url_aruodas__should_return_default_name():
  PATH = "C:\\Users\\Simonas\\Desktop\\Python Lessons\\WebScrapping\\Lesson1\\chromedriver.exe"
  driver = webdriver.Chrome(PATH)
  title = get_title(driver, "https://www.aruodas.lt/")
  return title == "Nekilnojamo turto skelbimai - Aruodas.lt Nekilnojamo turto skelbimai - Aruodas.lt"
  driver.quit()


# 8. 
def wait():
  time.sleep(random.gauss(1, 0.25))

# 9.
def test__wait__when_measure_multiple_times__should_return_waiting_average_equal_to_mean():
  number_of_experiments = 100
  start = timer()
  for x in range(number_of_experiments):
    wait()
  end = timer()
  elapsed_time = end - start
  average_waiting_time = elapsed_time/number_of_experiments
  print(average_waiting_time)
  return 0.5 < average_waiting_time and average_waiting_time < 1.5


# -----------------------

start_program()
# url = getValidURL()
url = "https://startupcodingschool.lt/"
PATH = "C:\\Users\\Simonas\\Desktop\\Python Lessons\\WebScrapping\\Lesson1\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

get_html(url)
get_all_links_in_page(driver, url)

print(test__get_title__when_url_aruodas__should_return_default_name())

#print(test__wait__when_measure_multiple_times__should_return_waiting_average_equal_to_mean())

driver.quit()

# -----------------------