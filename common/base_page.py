import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.log_utills import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 浏览器操作封装  -->  二次封装
    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开url地址：%s' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新')

    def get_title(self, title):
        value = self.driver.title.text
        logger.info('获取元素名称:%s' % value)

    '''self.username_input_box = {'element_name': '用户名输入框','locator_type': 'XPATH',
    'locator_value': '//input[@name="account"]','timeout': 3}'''
    def find_element(self, element_info):
        locator_element_name = element_info['element_name']
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']

        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'id':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'XPATH':
            locator_type = By.XPATH

        logger.info('%s元素识别成功' % locator_element_name)

        elment = WebDriverWait(self.driver, locator_timeout)\
            .until(lambda x: x.find_element(locator_type, locator_value_info))

        return elment

        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')))

    def click(self, element_info):
        locator_element_name = element_info['element_name']
        self.find_element(element_info).click()
        logger.info('%s点击操作成功' % locator_element_name)

    def input(self, element_info, content):
        locator_element_name = element_info['element_name']
        self.find_element(element_info).send_keys(content)
        logger.info('%s输入内容【%s】' % (locator_element_name, content))




