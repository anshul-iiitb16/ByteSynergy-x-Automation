from selenium import webdriver
import time
import os
import requests as requests

str1 = os.path.dirname(__file__)
str2 = "resume.pdf"
loc = str1 + "/" + str2

firefox_path = str1 + "/../drivers/geckodriver"

def web():
    # web_driver = webdriver.Chrome()
    web_driver = webdriver.Firefox(executable_path=firefox_path)

    url = 'https://lenoxexsearch.com/submit-resume/'
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

    resume_file = web_driver.find_element_by_xpath('//*[@id="resume_file"]')
    resume_file.send_keys(loc)

    #It will submit so dont uncomment
    # submit = web_driver.find_element_by_xpath('//*[@id="submit-resume-form"]/p/input[5]')
    # submit.click()
