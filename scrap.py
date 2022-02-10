from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from selenium.webdriver.common.by import By

str1 = os.getcwd()
str2 = "chromedriver"
loc = str1 + "/" + str2

# Creating a webdriver instance
driver = webdriver.Chrome(loc)
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")

# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element_by_id("username")

# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address
username.send_keys("")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("")

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
profile_url = "https://www.linkedin.com/in/shreeyav/"		#"https://www.linkedin.com/in/mayank1609/"
  
driver.get(profile_url)

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
	# this command scrolls the window starting from
	# the pixel value stored in the initialScroll
	# variable to the pixel value stored at the
	# finalScroll variable
	initialScroll = finalScroll
	finalScroll += 1000

	# we will stop the script for 3 seconds so that
	# the data can load
	time.sleep(3)
	# You can change it as per your needs and internet speed

	end = time.time()

	# We will scroll for 20 seconds.
	# You can change it as per your needs and internet speed
	if round(end - start) > 20:
		break

src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

# In case of an error, try changing the tags used here.

name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces

Roles_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
Roles = Roles_loc.get_text().strip()

intro = soup.find('div', {'class': 'pb2 pv-text-details__left-panel'})

location = intro.find("span", {'class': 'text-body-small'}).get_text().strip()

print('\n')
print('Name: ', name)
print('Roles: ', Roles)
#print('Company: ', company)
#print('College: ', college)
print('Location: ', location)
#print('URL: ', linkedin_url)
print('\n')



contact_url = profile_url + "overlay/contact-info/"

driver.get(contact_url)

time.sleep(10)

src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

Link = soup.find('div', {'class': 'pv-contact-info__ci-container t-14'})

if Link:
	Profile_link_loc = Link.find("a")
	if Profile_link_loc:
		Profile_link = Profile_link_loc.get_text().strip()
	else:
		Profile_link = "None"
else:
	Profile_link = "None"

Phone_Number = soup.find('span', {'class': 't-14 t-black t-normal'})

if Phone_Number:
	Number = Phone_Number.get_text().strip()
else:
	Number = "None"

Address_sec = soup.find('section', {'class': 'pv-contact-info__contact-type ci-address'})

if Address_sec:
	Address_loc_0 = Address_sec.find('div', {'class': 'pv-contact-info__ci-container t-14'})
	if Address_loc_0:
		Address_loc_1 = Address_loc_0.find("a")
		if Address_loc_1:
			Address = Address_loc_1.get_text().strip()
		else:
			Address = "None"
	else:
		Address = "None"
else:
	Address = "None"


Email_sec = soup.find('section', {'class': 'pv-contact-info__contact-type ci-email'})

if Email_sec:
	Email_loc_0 = Email_sec.find('div', {'class': 'pv-contact-info__ci-container t-14'})
	if Email_loc_0:
		Email_loc_1 = Email_loc_0.find("a")
		if Email_loc_1:
			Email = Email_loc_1.get_text().strip()
		else:
			Email = "None"
	else:
		Email = "None"
else:
	Email = "None"

print("Profile_link: ", Profile_link)
print("Phone_Number: ", Number)
print("Address: ", Address)
print("Email: ", Email)