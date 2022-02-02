import sys
from datetime import date
import csv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)


def dashboard():
    driver.get("https://secure.spindlelive.com/#/Health/41100")
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[2]/table/tbody/tr[1]/td')))
    time.sleep(2)
    driver.save_screenshot("latest.png")


def temperature():
    driver.get("https://secure.spindlelive.com/#/WAE/Meters/41100/Temperatures")
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]')))

    rows = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr"))
    print("Rows in table are " + repr(rows))
    columns = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[2]/td"))
    print("cols in table are " + repr(columns))

    #prepare to iterate over table
    before_XPath = "/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr["

    aftertd_XPath = "]/td["
    aftertr_XPath = "]"
    lst = []
    for t_row in range(2, (rows + 1), 1):
        sub_list = []
        for t_column in range(2, (columns + 1), 1):
            FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
            cell_text = driver.find_element_by_xpath(FinalXPath).text
            sub_list.append(cell_text)
        print(repr(sub_list))
        lst.append(sub_list)
    print("--")
    print(repr(lst))


    #write the table data out to csv file
    path_to_file = "/home/sandworm/Workspace/Work/spindle/temperature.csv"

    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(' ')
    today = date.today()
    csvWriter.writerow([repr(today), "today", "yesterday"])
    for element in lst:
        csvWriter.writerow(element) 

def hours():
    driver.get("https://secure.spindlelive.com/#/Analysis/DLM/41100/Employees")
    #wait for "equipment" button to load
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[4]/div[3]/div/div/div[2]/div/div[2]/div[1]/div/button[3]')))
    print("pressing \'equipment\' button")

    driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[2]/div/div[2]/div[1]/div/button[3]").click()

    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[4]/div[3]/div/div/div[4]/div/div/div[3]/table[2]/tbody[2]/tr[1]/td[1]')))
    rows = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[4]/div/div/div[3]/table[2]/tbody"))
    print("Rows in table are " + repr(rows))
    columns = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[4]/div/div/div[3]/table[2]/tbody[2]/tr[1]/td"))
    print("cols in table are " + repr(columns))
    print("reading from table")

    #prepare to iterate over table
    before_XPath = "/html/body/div[4]/div[3]/div/div/div[4]/div/div/div[3]/table[2]/tbody["

    aftertd_XPath = "]/tr[1]/td["
    aftertr_XPath = "]"
    lst = []
    for t_row in range(2, (rows + 1), 1):
        sub_list = []
        for t_column in range(2, (columns + 1), 1):
            FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
            cell_text = driver.find_element_by_xpath(FinalXPath).text
            sub_list.append(cell_text)
        print(repr(sub_list))
        lst.append(sub_list)
    print("--")
    print(repr(lst))


    #write the table data out to csv file
    path_to_file = "/home/sandworm/Workspace/Work/spindle/loggedhours.csv"

    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(' ')
    today = date.today()
    csvWriter.writerow([repr(today), "weighed productivity", "logged hours", "standard hours", "non-standard hours", "lost hours"])
    for element in lst:
        csvWriter.writerow(element) 

def pieces():
    print("todo")



def gasUsage():
    driver.get("https://secure.spindlelive.com/#/WAE/Meters/41100/Gas")
    #wait for one of the table cells to load so we know the table is available
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]')))

    #get table size
    rows = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr"))
    print("Rows in table are " + repr(rows))
    columns = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[2]/td"))
    print("cols in table are " + repr(columns))

    #prepare to iterate over table
    before_XPath = "/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr["

    aftertd_XPath = "]/td["
    aftertr_XPath = "]"
    lst = []
    for t_row in range(2, (rows + 1), 1):
        sub_list = []
        for t_column in range(2, (columns + 1), 1):
            FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
            cell_text = driver.find_element_by_xpath(FinalXPath).text
            sub_list.append(cell_text)
        print(repr(sub_list))
        lst.append(sub_list)
    print("--")
    print(repr(lst))


    #write the table data out to csv file
    path_to_file = "/home/sandworm/Workspace/Work/spindle/gasusage.csv"

    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(' ')
    today = date.today()
    csvWriter.writerow([repr(today), "today", "yesterday"])
    for element in lst:
        csvWriter.writerow(element) 

def equipmentLoggedOut():
    driver.get("https://secure.spindlelive.com/#/Analysis/EQM/Maintenance%20Worker%20Hours/41100")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "eqm-maint-worker")))
    print("eqm-maint-worker located")

    #select maintenace worker hours dropdown by xpath, set to equipment
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/button").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/ul/li[1]/a").click()

    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[4]/div[3]/div/div/div[4]/div/div/div/div[2]/table/tbody/tr[2]/th[2]/div/a')))
    


    rows = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[4]/div/div/div/div[2]/table/tbody/tr"))
    print("Rows in table are " + repr(rows))
    columns = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[4]/div/div/div/div[2]/table/tbody/tr[2]/th"))
    print("cols in table are " + repr(columns))

    before_XPath = "/html/body/div[4]/div[3]/div/div/div[4]/div/div/div/div[2]/table/tbody/tr["
    aftertd_XPath = "]/th["
    aftertr_XPath = "]"


    lst = []
    for t_row in range(2, (rows), 2):
        sub_list = []
        for t_column in range(2, (columns + 1), 1):
            FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
            cell_text = driver.find_element_by_xpath(FinalXPath).text
            sub_list.append(cell_text)
        print(repr(sub_list))
        lst.append(sub_list)
    print("--")
    print(repr(lst))


    #write the table data out to csv file
    path_to_file = "/home/sandworm/Workspace/Work/spindle/downtime.csv"

    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(' ')
    today = date.today()
    csvWriter.writerow([repr(today)])
    for element in lst:
        csvWriter.writerow(element) 



def waterUsage():
    #go to meters page
    driver.get("https://secure.spindlelive.com/#/WAE/Meters/41100/Water")
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, r'/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[3]/td[3]')))

    #get table size
    rows = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr"))
    print("Rows in table are " + repr(rows))
    columns = len (driver.find_elements_by_xpath("/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr[2]/td"))
    print("cols in table are " + repr(columns))

    #prepare to iterate over table
    before_XPath = "/html/body/div[4]/div[3]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[1]/table/tbody/tr["

    aftertd_XPath = "]/td["
    aftertr_XPath = "]"
    lst = []
    for t_row in range(2, (rows + 1), 1):
        sub_list = []
        for t_column in range(2, (columns + 1), 1):
            FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
            cell_text = driver.find_element_by_xpath(FinalXPath).text
            sub_list.append(cell_text)
        print(repr(sub_list))
        lst.append(sub_list)
    print("--")
    print(repr(lst))


    #write the table data out to csv file
    path_to_file = "/home/sandworm/Workspace/Work/spindle/waterusage.csv"

    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(' ')
    today = date.today()
    csvWriter.writerow([repr(today), "today", "yesterday"])
    for element in lst:
        csvWriter.writerow(element) 



def login():
    driver.get("https://secure.spindlelive.com")
    driver.get("https://secure.spindlelive.com/#/Login")
    driver.find_element_by_id("username").send_keys('peter@laundrytechsolutions.com')
    driver.find_element_by_id("password").send_keys('FDLULMRPZ')
    driver.find_element_by_xpath("//button[@type='submit']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "corp-dlm-portlet")))
    dashboard()
