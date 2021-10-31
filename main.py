from selenium.webdriver.common.by import By
from common.setting import ChromeDriver
from pages.login_page import LoginPage
from pages.recived_order import CreateRecivedOrderPage


try:
  # ドライバの設定
  driver = ChromeDriver(options=[], executable_path="./chromedriver")

  # ログイン処理
  login_page = LoginPage.visit(driver)
  login_page.user_name_input.change('test')
  login_page.password_input.change('test')
  login_page.login_button.click()

  create_recived_order_page = CreateRecivedOrderPage.visit(driver)
  create_recived_order_page.change_clients('string')
  create_recived_order_page.company_input.add('string')
  create_recived_order_page.depart_input.add('string')
  create_recived_order_page.recived_order_date_input.add('20210909')
except Exception as e:
  print(e)
  if driver:
    print(driver)
    driver.close()
    driver.alarm.cancel()
# top_page = TopPage.load(driver)
# top_page.top_icon.click()
# top_page.salse_icon.click()
# top_page.recived_order_icon.click()
# top_page.recived_order_list_icon.click()
# driver.close()