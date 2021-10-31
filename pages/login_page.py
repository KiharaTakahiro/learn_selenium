from common.page import BasePage, TextInput, Button
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
  def set_page_url(self):
      return 'http://localhost:9527/#/login?redirect=%2Fdashboard'

  def set_element(self):
    self.user_name_input: TextInput = TextInput(self._driver, By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
    self.password_input: TextInput = TextInput(self._driver, By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input')
    self.login_button: Button = Button(self._driver, By.XPATH, '//*[@id="app"]/div/form/button')