from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import requests as requests

str1 = os.path.dirname(__file__)
str2 = "resume.pdf"
loc = str1 + "/" + str2

#if not using firefox Comment this out this is for firefox
firefox_path = str1 + "/../drivers/geckodriver"
chrome_path = str1 + "/../drivers/chromedriver"

def web():
    #Uncomment this line to use Chrome
    # web_driver = webdriver.Chrome(executable_path=chrome_path )
    
    #if not using firefox Comment this out this is for firefox
    web_driver = webdriver.Firefox(executable_path=firefox_path)

    url = 'https://irionline.jobs.net/en-US/join'
    web_driver.get('https://irionline.jobs.net/en-US/join')

    time.sleep(2)

    first_name = "Ayesha"
    name = web_driver.find_element_by_xpath('//*[@id="formly_1_input_jf_first_name_4"]')
    name.send_keys(first_name)

    last_name = "K"
    lname = web_driver.find_element_by_xpath('//*[@id="formly_1_input_jf_last_name_5"]')
    lname.send_keys(last_name)

    your_email = "Ayesha@gmail.com"
    email = web_driver.find_element_by_xpath('//*[@id="formly_1_input_jf_email_address_0"]')
    email.send_keys(your_email)

    your_city = "Ajmer"
    city = web_driver.find_element_by_xpath('//*[@id="location_free_text"]')
    city.send_keys(your_city)

    your_num = "QA"
    num = web_driver.find_element_by_xpath('//*[@id="formly_1_input_jf_desired_job_title_3"]')
    num.send_keys(your_num)

    el = web_driver.find_element_by_id("formly_1_select_jf_country_code_1")
    drp = Select(el);
    drp.select_by_visible_text("India");

    resume_file = web_driver.find_element_by_xpath('//*[@id="browse"]')
    resume_file.send_keys(loc)

    #It will submit so dont uncomment
    # submit = web_driver.find_element_by_xpath('//*[@id="join-button"]')
    # submit.click()
