from selenium import webdriver
from bs4 import BeautifulSoup
import selenium
import time 
import csv
from selenium.webdriver.common.by import By
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/hm/New folder/python/web-scraping/chromedriver.exe")
browser.get(START_URL)  
time.sleep(10)

def scraping(): 
    headers = ["Name", "Distance", "Mass", "Radius"]
    data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tbody_tag in soup.find_all("tbody"):
        tr_tags = tbody_tag.find_all("tr")
        for tr_tag in tr_tags:
            templist = []
            for td in tr_tag:
                _text = td.getText()
                if _text != '\n':
                    try:
                        templist.append(td.getText().strip("\n"))
                    except:
                        pass
            requireddata = []
            range1 = [1,3,5,6]
            for i in range1:
                requireddata.append(templist[i])
            data.append(requireddata)
            print(templist)
    with open("webscraping1.csv", "w", encoding = "utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        print(data)
        csv_writer.writerows(data)
        for i in data:
            if any(field.strip()for field in i):
                csv_writer.writerows(data)      
        print("success!!!")

scraping()
    