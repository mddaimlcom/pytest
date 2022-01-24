import pickle
import selenium.webdriver
from pathlib import Path


_exec_path = '~/WebDrivers/geckodriver'

exec_path = Path(_exec_path).expanduser()
driver = selenium.webdriver.Firefox(executable_path=exec_path)
driver.get("https://www.endava.com/")
cookies = pickle.load(open("tests/py_test/data_artifacts/endava_cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
driver.close()
driver.quit()
