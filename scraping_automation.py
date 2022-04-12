from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
from bs4 import BeautifulSoup
import time


chrome_path="D:\Web Development\chromedriver.exe"

driver=webdriver.Chrome(executable_path=chrome_path,options=options)
driver.get("https://www.amazon.in")
searchbar=driver.find_element_by_id("twotabsearchtextbox")
searchbar.send_keys("iphone")
searchbar.send_keys(Keys.RETURN)
time.sleep(2)
iphones=driver.find_elements_by_class_name("a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2")
iphonesprice=driver.find_elements_by_class_name("a-price-whole")
iphonelink=driver.find_elements_by_css_selector(".s-line-clamp-2 a")

for phones in range(len(iphones)-1):
    driver=webdriver.Chrome(executable_path=chrome_path)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfYwyQb9oQUTs5ab-A5HdKdwzD2uou-OOEhO5OWDou5tM55-w/viewform?usp=sf_link")
    time.sleep(5)
    formname=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    formprice=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    formlink=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    formname.click()
    formname.send_keys(iphones[phones].text)
    formprice.click()
    formprice.send_keys(iphonesprice[phones].text)
    formlink.click()
    formlink.send_keys(iphonelink[phones].get_attribute('href'))
    submit=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    driver.quit()
# for phones in range(len(iphones)-1):
#     # print(iphones[phones].text,iphonesprice[phones].text,iphonelink[phones].get_attribute('href'))
#     form.send_keys(iphones[phones].text)
# form.send_keys(iphones[phones].text)
# form.send_keys(iphones[phones].text)
# searchbar.send_keys(Keys.RETURN)
