# -*- coding: utf-8 -*-

from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

#������� �������
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#�������
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

#���� ��������
input = browser.find_element_by_id("answer")
input.send_keys(y)

#����������� ��������
input1 = browser.find_element_by_id("robotCheckbox")
input1.click()

#�������� �����������
input2 = browser.find_element_by_id("robotsRule")
input2.click()

#����������
button = browser.find_element_by_css_selector('button')
button.click()