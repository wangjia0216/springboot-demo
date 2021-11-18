# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestbaidu():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testbaidu(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(1550, 838)
    self.driver.find_element(By.ID, "kw").send_keys("selenium学习")
    self.driver.find_element(By.ID, "su").click()
    self.driver.close()
