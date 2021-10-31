import abc
import time
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Driver(object, metaclass = abc.ABCMeta):

  def __init__(self, options: list, executable_path: str = '', time_out: int = 100):
    """コンストラクタ

    Args:
        options (list): オプション
        executable_path (str, optional): ドライバのパス. Defaults to ''.
        time_out (int, optional): タイムアウトの設定. Defaults to 100.
    """
    self.start_time = time.time()
    self.prev_action_time = time.time()
    self.driver = self._set_driver(executable_path)
    self.wait: WebDriverWait = WebDriverWait(self.driver, time_out)
    self.actions: ActionChains = ActionChains(self.driver)
    self._time_out: int = time_out
    self.history: list = []
    self._set_options(options)
    self.alarm = Schadule(5, self._handler)
    self.alarm.run()

  @abc.abstractmethod
  def _set_driver(self, executable_path: str):
    """ドライバ設定処理を実装する
       実装すべき処理)self._driverにWEBドライバの値を入れる

    Args:
        executable_path (str): 設定が必要な場合のみ設定する
    """
    pass

  @abc.abstractmethod
  def _set_options(self, options_param: list):
    """オプション設定処理を実装する

    Args:
        options (options): 設定すべきオプション
    """
    pass

  def _handler(self):
    print(self.prev_action_time)
    print(time.time())

  def close(self):
    """終了
    """
    self.driver.close()

  def __str__(self):
    str_format = {
      'class_name': self.__class__.__name__,
      'time_out': self._time_out,
      'history': self.history
    }
    return str(str_format)

class ChromeDriver(Driver):
  def _set_driver(self, executable_path: str):
      return webdriver.Chrome(executable_path=executable_path)

  def _set_options(self, options_param: list):
    options = webdriver.ChromeOptions()
    for option in options_param:
      options.add_argument(option)
    
class Schadule():
  def __init__(self, timer, call_back):
    self.call_back = call_back
    self.timer = timer

  def __setting_hanndler(self):
    t = threading.Timer(self.timer, self.call_back)
    t.start()

  def run(self):
    self.all_thread = threading.Thread(target=self.__setting_hanndler)
    self.all_thread.start()