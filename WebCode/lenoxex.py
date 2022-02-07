from selenium import webdriver
import time

def web():
    web = webdriver.Chrome()
    web.get('https://lenoxexsearch.com/submit-resume/')

    time.sleep(2)

    YourName = "Ayesha"
    name = web.find_element_by_xpath('//*[@id="candidate_name"]')
    name.send_keys(YourName)

    YourEmail = "Ayesha@gmail.com"
    email = web.find_element_by_xpath('//*[@id="candidate_email"]')
    email.send_keys(YourEmail)

    YourCity = "USA"
    city = web.find_element_by_xpath('//*[@id="candidate_location"]')
    city.send_keys(YourEmail)

#Will test these later
# sample_file = open("sample.txt", "rb")
# upload_file = {"Uploaded file": sample_file}
# r = requests.post(url, files = upload_file)

    element = web.find_element_by_xpath('//*[@id="resume_file"]')
# maybe like this: //input[@type="file"]
    element.send_keys("your file path")

# Submit = web.find_element_by_xpath('//*[@id="submit-resume-form"]/p/input[5]')
# Submit.click()