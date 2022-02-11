from selenium import webdriver
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

    url = 'https://www.newagesys.com/submit_resume.php'
    web_driver.get(url)

    time.sleep(2)

    your_name = "Ayesha"
    name = web_driver.find_element_by_xpath('//*[@id="txtname"]')
    name.send_keys(your_name)

    your_email = "Ayesha@gmail.com"
    email = web_driver.find_element_by_xpath('//*[@id="txtmail"]')
    email.send_keys(your_email)

    your_num = "+1 91888234243"
    num = web_driver.find_element_by_xpath('//*[@id="txtphone"]')
    num.send_keys(your_num)

    job_title = "Web Developer"
    web_driver.find_element_by_xpath('//*[@id="txttitle"]').send_keys(job_title)

    resume_file = web_driver.find_element_by_xpath('//*[@id="resume"]')
    resume_file.send_keys(loc)

    message = "I have 5 years of experience"
    web_driver.find_element_by_xpath('//*[@id="message"]').send_keys(message)

    #It will submit so dont uncomment
    # submit = web_driver.find_element_by_xpath('/html/body/div/div[2]/div[4]/div/form/table/tbody/tr[7]/td[2]/a/img')
    # submit.click()
