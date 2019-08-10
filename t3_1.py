# -*- coding: utf-8 -*-
"""
@File    :   t3_1.py
@Author  :   Li Changtai
@E-mail  :   lichangtai17@gmail.com
@Date    :   2019/8/9 14:31
@Software:   PyCharm
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://mail.163.com/ ')
    method = browser.find_element_by_id('lbNormal')
    method.click()
    browser.switch_to.frame(0)
    input_email = browser.find_element_by_name('email')
    input_passwd = browser.find_element_by_name('password')
    btn_login = browser.find_element_by_id('dologin')
    input_email.send_keys('lichangtai181')
    input_passwd.send_keys('lct521521')
    btn_login.click()
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
finally:
    pass
    # browser.close()