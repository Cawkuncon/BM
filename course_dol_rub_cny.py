import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class CourseCnyRub:
    response = requests.get('https://fx-rate.net/CNY/RUB/').text
    soup = BeautifulSoup(response, 'lxml')
    rub = soup.find('input', {'class': 'ip_amount cal_amount_to'}).get('value')
    yuan = soup.find('input', {'class': 'ip_amount cal_amount_from'}).get('value')

    @classmethod
    def get_course(cls):
        return round(float(cls.rub) / float(cls.yuan), 2)


class CourseDolRub:
    option = webdriver.ChromeOptions()
    option.headless = True
    browser = webdriver.Chrome(options=option)

    @classmethod
    def get_course(cls):
        cls.browser.get('https://t.me/s/steamrub')
        messages = cls.browser.find_elements(By.CLASS_NAME, 'tgme_widget_message_bubble')
        text_course = messages[-1].text
        index = text_course.find('=')
        rub = text_course[index + 2:index + 7]
        cls.browser.close()
        return float(rub)
