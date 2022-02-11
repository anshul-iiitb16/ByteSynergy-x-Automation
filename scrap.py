from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from selenium.webdriver.common.by import By

def scroll():
	initialScroll = 0
	finalScroll = 1000
	start = time.time()

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
username.send_keys("codetest1011@gmail.com")

# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element
# tag used here.

# Enter Your Password
pword.send_keys("Codetest@1011")

# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.
profile_url = "https://www.linkedin.com/in/mayank1609/"	#"https://www.linkedin.com/in/anshul-jindal-420109230/"  # "https://www.linkedin.com/in/mayank1609/" 	#"https://www.linkedin.com/in/shreeyav/"

driver.get(profile_url)

# will be used in the while loop
scroll()

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
print('\n')

Common = soup.find_all("section", {"class": "artdeco-card ember-view break-words pb3 mt4"})

for i in range(len(Common)):
	if(Common[i].find("div", {"id": "experience"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):
		driver.get(profile_url)
		scroll()
		src = driver.page_source

		soup = BeautifulSoup(src, 'lxml')
		time.sleep(5)

		Experience_loc = Common[i].find("ul", {"class": "pvs-list ph5 display-flex flex-row flex-wrap"})
		Experience_loc_0 = Experience_loc.find_all("li", {"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})

		Experiences = []
		for j in range(len(Experience_loc_0)):
			Experiences.append([])
			Experience_loc_1 = Experience_loc_0[j].find_all("span", {"aria-hidden": "true"})

			for k in range(len(Experience_loc_1)):
				Experiences[j].append(Experience_loc_1[k].get_text().strip())

		print("Experiences:", Experiences)

	if (Common[i].find("div", {"id": "education"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):
		driver.get(profile_url)
		scroll()
		src = driver.page_source

		soup = BeautifulSoup(src, 'lxml')
		time.sleep(5)

		Education_loc = Common[i].find("ul", {"class": "pvs-list ph5 display-flex flex-row flex-wrap"})
		Education_loc_0 = Education_loc.find_all("li", {
			"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})

		Qualifications = []
		for j in range(len(Education_loc_0)):
			Qualifications.append([])
			Education_loc_1 = Education_loc_0[j].find_all("span", {"aria-hidden": "true"})

			for k in range(len(Education_loc_1)):
				Qualifications[j].append(Education_loc_1[k].get_text().strip())

		print("Qualifications:", Qualifications)

	if (Common[i].find("div", {"id": "skills"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):
		is_Futher = Common[i].find("div", {"class": "pvs-list__footer-wrapper"})

		if(is_Futher):
			Skill_link = profile_url + "details/skills/"
			driver.get(Skill_link)
			scroll()
			src = driver.page_source

			# Now using beautiful soup
			soup1 = BeautifulSoup(src, 'lxml')
			time.sleep(5)

			Skills_list_loc = soup1.find("ul", {"class": "pvs-list"})
			Skills_list_loc_1 = Skills_list_loc.find_all("span", {"aria-hidden": "true"})

			Skills_list = []
			for j in range(len(Skills_list_loc_1)):
				Skills_list.append(Skills_list_loc_1[j].get_text().strip())

			print("List of Skills:", Skills_list)
		else:
			driver.get(profile_url)
			scroll()
			src = driver.page_source

			soup = BeautifulSoup(src, 'lxml')
			time.sleep(5)

			Skills_list_loc = Common[i].find("ul", {"class": "pvs-list ph5"})
			Skills_list_loc_1 = Skills_list_loc.find_all("span", {"aria-hidden": "true"})

			Skills_list = []
			for j in range(len(Skills_list_loc_1)):
				Skills_list.append(Skills_list_loc_1[j].get_text().strip())

			print("List of Skills:", Skills_list)

	if (Common[i].find("div", {"id": "projects"}) and Common[i].find("div", {"class": "pv-profile-card-anchor"})):
		is_Futher = Common[i].find("div", {"class": "pvs-list__footer-wrapper"})

		if(is_Futher):
			Project_link = profile_url + "details/projects/"
			driver.get(Project_link)
			scroll()
			src = driver.page_source

			# Now using beautiful soup
			soup2 = BeautifulSoup(src, 'lxml')
			time.sleep(5)

			Projects_loc = soup2.find("ul", {"class": "pvs-list"})
			Projects_list_loc_1 = Projects_loc.find_all("li", {"class": "pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
			print(len(Projects_list_loc_1))
			Projects = []

			for j in range(len(Projects_list_loc_1)):
				Projects_list_loc_2 = Projects_list_loc_1[j].find_all("span", {"aria-hidden": "true"})

				Projects.append([])
				for k in range(len(Projects_list_loc_2)):
					Projects[j].append(Projects_list_loc_2[k].get_text().strip())

			for j in range(len(Projects)):
				print(Projects[j])
		else:
			driver.get(profile_url)
			scroll()
			src = driver.page_source

			soup = BeautifulSoup(src, 'lxml')
			time.sleep(5)

			Projects_loc = Common[i].find("ul", {"class": "pvs-list ph5 display-flex flex-row flex-wrap"})
			Projects_list_loc_1 = Projects_loc.find_all("li", {"class": "artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"})

			print(len(Projects_list_loc_1))
			Projects = []

			for j in range(len(Projects_list_loc_1)):
				Projects_list_loc_2 = Projects_list_loc_1[j].find_all("span", {"aria-hidden": "true"})

				Projects.append([])
				for k in range(len(Projects_list_loc_2)):
					Projects[j].append(Projects_list_loc_2[k].get_text().strip())

			for j in range(len(Projects)):
				print(Projects[j])


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