
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ZentaoPage(BasePage):
	username_locator = (By.ID, "account")
	password_locator = (By.CSS_SELECTOR, "[name='password']")
	submit_locator = (By.XPATH, "//*[@id='submit']")

	login_user = (By.XPATH, '//span[@class="user-name"]')

	def __init__(self, driver):
		super().__init__(driver)

	def submit_login(self, username, password):
		self.send_keys(self.username_locator, username)
		self.send_keys(self.password_locator, password)
		time.sleep(2)
		self.click(self.submit_locator)

	def get_alert(self):
		"""判断alert是否存在, 存在就返回text文本内容, 不存在返回空字符"""
		try:
			alert = self.is_alert()
			text = alert.text
			alert.accept()
			return text
		except Exception as e:
			return ""

	def login_result(self, _text):
		"""登录成功后, 获取当前页面的用户名, 判断用户"""
		r = self.is_text_in_element(self.login_user, _text)
		return r


if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.get("http://127.0.0.1/pro/user-login.html")
	zentao = ZentaoPage(driver)
	zentao.submit_login("admin", "Ft123456")
