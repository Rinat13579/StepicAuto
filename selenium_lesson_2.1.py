# -*- coding: utf-8 -*-

from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

#Функция расчета
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Рассчет
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

#Ввод значения
input = browser.find_element_by_id("answer")
input.send_keys(y)

#Выставление чекбокса
input1 = browser.find_element_by_id("robotCheckbox")
input1.click()

#Отмечаем радиокнопку
input2 = browser.find_element_by_id("robotsRule")
input2.click()

#Отправляем
button = browser.find_element_by_css_selector('button')
button.click()