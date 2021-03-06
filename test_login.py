#!/usr/bin/env python
#_*_coding:utf-8_*_

import unittest
import time
import conf
import xpaths

class TestLogin(unittest.TestCase):
    """Test Login"""
    def setUp(self):
        self.driver = conf.get_driver(proxy=True)
    def tearDown(self):
        self.driver.close()

    def test_login_success(self):
        self.driver.get(conf.login_url)
        name = self.driver.find_element_by_xpath(xpaths.login_username)
        name.send_keys(conf.username)
        password = self.driver.find_element_by_xpath(xpaths.login_password)
        password.send_keys(conf.password)
        login = self.driver.find_element_by_xpath(xpaths.login_btn)
        login.click()
        #self.assertEqual(self.driver.title, u'东阳大数据平台', msg=u'login failed with correct password')
        self.assertTrue(u'version' in self.driver.page_source, msg=u'login failed with correct password')

    def test_login_wrong_password(self):
        self.driver.get(conf.login_url)
        name = self.driver.find_element_by_xpath(xpaths.login_username)
        name.send_keys(conf.username)
        password = self.driver.find_element_by_xpath(xpaths.login_password)
        password.send_keys("some_random_chars")
        login = self.driver.find_element_by_xpath(xpaths.login_btn)
        login.click()
        #print self.driver.current_url, conf.login_url
        #self.assertEqual(self.driver.current_url, conf.login_url, msg=u'login success with wrong password')
        self.assertIn('login', self.driver.current_url, msg=u'login success with wrong password')
