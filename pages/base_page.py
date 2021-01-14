from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
	"""基于原生的selenium做二次封装"""
	def __init__(self, driver):
		self.driver = driver
		self.timeout = 10
		self.t = 0.5

	def find_element(self, locator):
		"""定位单个元素, 返回元素对象, 若没定位到, Timeout异常"""
		if not isinstance(locator, tuple):
			print("locator参数类型错误, 必须是tuple类型")
		else:
			print(f"正在定位元素信息, 定位方式: {locator[0]}, value值: {locator[1]}")
			return WebDriverWait(self.driver, self.timeout, self.t).until(
				EC.presence_of_element_located(locator))

	def find_elements(self, locator):
		"""定位多个元素, 返回元素对象, 若没定位到, Timeout异常"""
		if not isinstance(locator, tuple):
			print("locator参数类型错误, 必须是tuple类型")
		else:
			try:
				print(f"正在定位元素信息, 定位方式: {locator[0]}, value值: {locator[1]}")
				return WebDriverWait(self.driver, self.timeout, self.t).until(
					EC.presence_of_all_elements_located(locator))
			except Exception:
				return []

	def send_keys(self, locator, text=""):
		"""向输入框元素输入文本信息"""
		ele = self.find_element(locator)
		ele.send_keys(text)

	def click(self, locator):
		ele = self.find_element(locator)
		ele.click()

	def clear(self, locator):
		ele = self.find_element(locator)
		ele.clear()

	def is_selected(self, locator):
		"""判断元素是否被选中, 返回bool值"""
		ele = self.find_element(locator)
		return ele.is_selected()

	def is_element_exist(self, locator):
		try:
			self.find_element(locator)
			return True
		except Exception:
			return False

	def is_title(self, _title=""):
		"""判断是否为title, 返回bool值"""
		try:
			return WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
		except Exception:
			return False

	def is_title_contains(self, _title=""):
		try:
			return WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
		except Exception:
			return False

	def is_text_in_element(self, locator, _text=""):
		if not isinstance(locator, tuple):
			print("locator参数类型错误, 必须是tuple类型")
		else:
			try:
				return WebDriverWait(self.driver, self.timeout, self.t).until(
					EC.text_to_be_present_in_element(locator, _text))
			except Exception:
				return False

	def is_value_in_element(self, locator, _value=""):
		if not isinstance(locator, tuple):
			print("locator参数类型错误, 必须是tuple类型")
		else:
			try:
				return WebDriverWait(self.driver, self.timeout, self.t).until(
					EC.text_to_be_present_in_element_value(locator, _value))
			except Exception:
				return False

	def is_alert(self, timeout=3):
		try:
			return WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
		except Exception:
			return False

	def get_title(self):
		return self.driver.title

	def get_text(self, locator):
		try:
			return self.find_element(locator).text
		except Exception:
			print("获取元素text失败, 返回")
			return ""

	def get_attribute(self, locator, name):
		"""获取元素属性"""
		try:
			ele = self.find_element(locator)
			return ele.get_attribute(name)
		except Exception:
			print(f"获取{name}属性失败, 返回")
			return ""

	def js_focus_element(self, locator):
		"""聚焦元素"""
		target = self.find_element(locator)
		self.driver.execute_script("argument[0].scrollIntoView()", target)

	def js_scroll_top(self):
		"""回到顶部"""
		js = "window.scrollTop(0, 0)"
		self.driver.execute_script(js)

	def js_scroll_end(self, x=0):
		"""滚到底部"""
		js = f"window.scrollTo({x}, document.body.scrollHeight)"
		self.driver.execute_script(js)

	def select_by_index(self, locator, index=0):
		"""通过index定位select元素"""
		ele = self.find_element(locator)
		Select(ele).select_by_index(index)

	def select_by_value(self, locator, value):
		ele = self.find_elements(locator)
		Select(ele).select_by_value(value)

	def select_by_text(self, locator, text):
		ele = self.find_element(locator)
		Select(ele).select_by_visible_text(text)

	def switch_iframe(self, id_index_locator):
		"""切换frame"""
		try:
			if isinstance(id_index_locator, int):
				self.driver.switch_to.frame(id_index_locator)
			elif isinstance(id_index_locator, str):
				self.driver.switch_to.frame(id_index_locator)
			elif isinstance(id_index_locator, tuple):
				ele = self.find_element(id_index_locator)
				self.driver.switch_to.frame(ele)
		except Exception:
			print("iframe 切换异常")

	def switch_window(self, window_name):
		self.driver.switch_to.window(window_name)

	def switch_alert(self):
		r = self.is_alert()
		if not r:
			print("alert 不存在")
		else:
			return r

	def move_to_element(self, locator):
		"""鼠标悬停"""
		ele = self.find_element(locator)
		ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	web = BasePage(driver)
	driver.get("https://home.cnblogs.com/u/yoyoketang/")
	loc_1 = ("id", "header_user_left")
	t = web.get_text(loc_1)
	driver.quit()
