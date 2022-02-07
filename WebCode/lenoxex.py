from selenium import webdriver
import time
import os

str1 = os.path.dirname(__file__)
str2 = "resume.pdf"
loc = str1 + "/" + str2


def web():
    web_driver = webdriver.Chrome()
    web_driver.get('https://lenoxexsearch.com/submit-resume/')

    time.sleep(2)

    your_name = "Ayesha"
    name = web_driver.find_element_by_xpath('//*[@id="candidate_name"]')
    name.send_keys(your_name)

    your_email = "Ayesha@gmail.com"
    email = web_driver.find_element_by_xpath('//*[@id="candidate_email"]')
    email.send_keys(your_email)

    your_city = "USA"
    city = web_driver.find_element_by_xpath('//*[@id="candidate_location"]')
    city.send_keys(your_city)

    your_num = "+1 91888234243"
    num = web_driver.find_element_by_xpath('// *[ @ id = "candidate_phone"]')
    num.send_keys(your_num)

    # Will test these later
    # sample_file = open("sample.txt", "rb")
    # upload_file = {"Uploaded file": sample_file}
    # r = requests.post(url, files = upload_file)

    element = web_driver.find_element_by_xpath('//*[@id="resume_file"]')
    # maybe like this: //input[@type="file"]
    element.send_keys(loc)

    submit = web_driver.find_element_by_xpath('//*[@id="submit-resume-form"]/p/input[5]')
    submit.click()
