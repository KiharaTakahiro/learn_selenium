import abc
import time
from common.setting import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage(object, metaclass = abc.ABCMeta):
  def __init__(self, driver: Driver):
    """コンストラクタ

    Args:
        driver (Driver): driverを渡す
    """
    self.page_url = self.set_page_url()
    self._driver = driver

  @abc.abstractclassmethod
  def set_page_url(self):
    """ページURLの設定処理を実装する
    """
    pass

  @abc.abstractclassmethod
  def set_element(self):
    """ エレメント設定処理を実装する
    """
    pass
  
  @classmethod
  def visit(cls, driver: Driver):
    """ページ遷移処理

    Args:
        driver (Driver): ページ遷移の処理
    """
    driver.prev_action_time = time.time()
    this_page = cls(driver)
    driver.driver.get(this_page.page_url)
    this_page.set_element()
    history = {
      'action': 'visit',
      'time': driver.prev_action_time,
      'detail': {
        'url': this_page.page_url
      }
    }
    driver.history.append(history)
    driver.prev_action_time = time.time()
    return this_page

  @classmethod
  def load(cls, driver: Driver):
    """既に遷移している場合に画面情報の読み込みを行う処理

    Args:
        driver (Driver): [description]

    Returns:
        Page: ロードしたページ情報
    """
    driver.prev_action_time = time.time()
    this_page = cls(driver)
    this_page.set_element()
    history = {
      'action': 'load',
      'time': driver.prev_action_time,
      'detail': {
        'url': this_page.page_url
      }
    }
    driver.history.append(history)
    return this_page

  def check_current_page(self):
    """ 現在のページがこのページと一致するか？
    """
    return self._driver.driver.current_page == self._page_url

class PageItem():
  def __init__(self, driver: Driver, option: str, find_value: str):
    """ボタン初期化処理

    Args:
        driver (Driver): ドライバー
        option (str): 何で検索するか
        find_value (str): 検索対象判定ロジック
        wait_element (bool): エレメントが読み込まれるのを待つか？
    """
    self.driver: Driver = driver
    self.option: str = option
    self.find_value: str = find_value

  def get_element(self):
    """要素を取得する

    Returns:
        element: 取得した要素を返却
    """
    self.driver.wait.until(EC.presence_of_element_located((self.option, self.find_value)))
    if not self.driver.driver.find_element(self.option, self.find_value).is_displayed():
      self.driver.actions.move_to_element(self.get_element()).perform()
    return self.driver.driver.find_element(self.option, self.find_value)

  def is_display(self):
    """表示されているかの判定処理

    Returns:
        bool: 画面表示されているか？
    """
    return self.get_element().is_displayed()

  def mouse_over(self):
    """マウスオーバーさせる
    """
    self.driver.actions.move_to_element(self.get_element()).perform()

class Button(PageItem):    
  def click(self):
    """ボタン押下処理
    """
    self.driver.prev_action_time = time.time()
    self.get_element().click()
    history = {
      'action': 'button click',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display()
      }
    }
    self.driver.history.append(history)

class Icon(PageItem):
  def click(self):
    """ボタン押下処理
    """
    self.driver.prev_action_time = time.time()
    self.get_element().click()
    history = {
      'action': 'icon click',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display()
      }
    }
    self.driver.history.append(history)


class Link(PageItem):
  def get_link(self):
    """リンク先の取得

    Returns:
        str: リンク先を取得する
    """
    return self.get_element().get_attribute('href')

  def click(self):
    """ボタン押下処理
    """
    self.driver.prev_action_time = time.time()
    self.get_element().click()
    history = {
      'action': 'link click',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display()
      }
    }
    self.driver.history.append(history)

class TextInput(PageItem):
  def add(self, input: str):
    """追記入力処理

    Args:
        input (str): 入力内容
    """
    self.driver.prev_action_time = time.time()
    self.get_element().send_keys(input)
    history = {
      'action': 'add text',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display(),
        'text': input
      }
    }
    self.driver.history.append(history)

  def change(self, input: str):
    """入力欄変更処理

    Args:
        input (str): 入力内容
    """
    self.driver.prev_action_time = time.time()
    self.get_element().clear()
    self.get_element().send_keys(input)
    history = {
      'action': 'change text',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display(),
        'text': input
      }
    }
    self.driver.history.append(history)

  def clear(self):
    """入力欄のクリア処理
    """
    self.driver.prev_action_time = time.time()
    self.get_element().clear()
    history = {
      'action': 'clear text',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display()
      }
    }
    self.driver.history.append(history)

  def get_value(self):
    """入力値の取得

    Returns:
        str: 入力値
    """
    return self.get_element().get_attribute('value')

class Pulldown(PageItem):
  def get_value(self):
    """入力値の取得

    Returns:
        str: 入力値
    """
    return self.get_element().get_attribute('value')

  def get_disp_value(self):
    return self.get_element().get_attribute('outerHTML')

  def get_all_options(self):
    return Select(self.get_element()).all_selected_options

  def change_by_index(self, index: int):
    """インデックスをもとにプルダウンを設定する

    Args:
        value (any): 入力値を設定する
    """
    self.driver.prev_action_time = time.time()
    select = Select(self.get_element())
    select.select_by_index(index)
    history = {
      'action': 'change select (index)',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display(),
        'index': index
      }
    }
    self.driver.history.append(history)

  def change_by_value(self, value: str):
    """Valueをもとにプルダウンを設定する

    Args:
        value (any): 入力値を設定する
    """
    self.driver.prev_action_time = time.time()
    select = Select(self.get_element())
    select.select_by_value(value)
    history = {
      'action': 'change select (value)',
      'time': self.driver.prev_action_time,
      'detail': {
        'element': self.get_element(),
        'find_value': self.find_value,
        'options': self.option,
        'display': self.is_display(),
        'value': value
      }
    }
    self.driver.history.append(history)
