#!/usr/bin/python3
# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Firefox()
driver.get('https://jinshuju.net/f/yrLCU8')

driver.find_element_by_xpath("//input[@id='submission_password']").send_keys("2")
driver.find_element_by_xpath("//input[@class='gd-btn gd-btn-primary-solid']").click()
time.sleep(1.5)
driver.find_element_by_xpath("//input[@class='ant-input']").send_keys("XXXXXX")
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[4]/div/div[2]/div[1]/div/span/input").send_keys("XXXXXX")
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[6]/div/div[2]/div[1]/div/span/input").send_keys("XXXXXX")

driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[8]/div/div[2]/div[1]/div/span/input").send_keys("XXXXXX")

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//div[@id='react-select-3-option-0']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//div[@id='react-select-4-option-3']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//input[@class='ant-input ant-input-sm']").send_keys("103")
driver.find_element_by_xpath("//div[@id='react-select-5-option-102']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//input[@class='ant-input ant-input-sm']").send_keys("XXXXXX")
driver.find_element_by_xpath("//div[@id='react-select-6-option-278']").click()

driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[20]/div/div[2]/div/div/span/div/div/button").click()

driver.find_element_by_xpath("//span[@class='ant-cascader-picker-label']").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[22]/div/div[2]/div/div/span/div/div/div/div/div/div/ul[1]/li[19]").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[22]/div/div[2]/div/div/span/div/div/div/div/div/div/ul[2]/li[12]").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[22]/div/div[2]/div/div/span/div/div/div/div/div/div/ul[3]/li[5]").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//*[@id='react-select-7-option-0']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__placeholder css-50ogt9-placeholder']").click()
driver.find_element_by_xpath("//div[@id='react-select-13-option-1']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//div[@id='react-select-8-option-1']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//input[@class='ant-input ant-input-sm']").send_keys("7")
driver.find_element_by_xpath("//div[@id='react-select-9-option-6']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//div[@id='react-select-10-option-0']").click()

driver.find_element_by_xpath("//div[@class='pretty-select__value-container css-55y0h0']").click()
driver.find_element_by_xpath("//div[@id='react-select-11-option-0']").click()

driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[38]/div/div[2]/div[1]/div/span/input").send_keys("XXXXXX")

driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[40]/div/div[2]/div/div/span/div/span/span").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[40]/div/div[2]/div/div/span/div/div/div/div/div/div/ul[1]/li[19]").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[40]/div/div[2]/div/div/span/div/div/div/div/div/div/ul[2]/li[12]").click()
driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[3]/div/div[40]/div/div[2]/div/div/span/div/div/div/div/div/div/ul[3]/li[5]").click()

driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[5]/div[1]/button").click()
while True:
        time.sleep(1.5)
        driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[5]/div[1]/div/div/div[2]/a[1]/img").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[4]/div/form/div[5]/div[2]/button").click()