from common.page import BasePage, Icon
from selenium.webdriver.common.by import By

class TopPage(BasePage):
  def set_page_url(self):
      return 'http://localhost:9527/#/dashboard'

  def set_element(self):
    self.top_icon: Icon = Icon(self._driver, By.ID, 'hamburger-container')
    self.salse_icon: Icon = Icon(self._driver, By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div/ul/div[3]/li/div')
    self.recived_order_icon: Icon = Icon(self._driver, By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div/ul/div[3]/li/ul/div[2]/li/div')
    self.recived_order_list_icon: Icon = Icon(self._driver, By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div/ul/div[3]/li/ul/div[2]/li/ul/div[1]/a/li')
