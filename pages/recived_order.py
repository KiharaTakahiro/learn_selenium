from common.page import BasePage, Icon, Pulldown, TextInput
from selenium.webdriver.common.by import By

class CreateRecivedOrderPage(BasePage):
  def set_page_url(self):
      return 'http://localhost:9527/#/sales/recived-order/save-recived-order'

  def set_element(self):
    self.clients_input: TextInput = TextInput(self._driver, By.XPATH, '/html/body/div[2]/div/div[2]/section/div/form/div[1]/div/div/div/div/input')
    self.clients_input_pulldown: Icon = Icon(self._driver, By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[1]')
    self.company_input: TextInput = TextInput(self._driver, By.XPATH, '/html/body/div[2]/div/div[2]/section/div/form/div[2]/div/div[1]/div/div/div/div[1]/input')
    self.depart_input: TextInput = TextInput(self._driver, By.XPATH, '/html/body/div[2]/div/div[2]/section/div/form/div[2]/div/div[2]/div/div/div/div[1]/input')
    self.recived_order_date_input: TextInput = TextInput(self._driver, By.XPATH, '/html/body/div[2]/div/div[2]/section/div/form/div[3]/div/div/input')

  def change_clients(self, target_str: str):
    self.clients_input.add(target_str)
    self.clients_input_pulldown.click()

