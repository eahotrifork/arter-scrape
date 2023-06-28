from bs4 import BeautifulSoup
from selenium import webdriver
# for waiting until page is loaded -- remove if don´t need
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# access the Chrome browser driver in incognito mode and 
# without actually opening a browser window (headless argument)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# instantiate a driver object and assign the URL
url = "https://arter.dk/search/record-search?taxonIds=0558ddf8-f785-ea11-aa77-501ac539d1ea&excludeUnderlyingTaxons=true&periodMode=40&periodFilterField=1&hasMedia=false&includeDescendantTaxons=true&includeSpeciesGroupFacet=true&includeOrphanRecords=false&sortBy=1&tabMode=Regular"
driver.get(url)

# wait until page is loaded, or give timeout error
timeout = 5 # wait time of 5 seconds
try:
    element_present = EC.presence_of_element_located((By.ID, 'tab1'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

# get html from loaded page
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())  # TODO remove

observances = soup.find_all("a")
print(observances)  # TODO remove

observances_urls = []

# get the url of each result from the search
for obs in observances:
    print(obs)  # TODO remove
    observances_urls.append(obs)

driver.close()