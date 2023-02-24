from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

times = '2023-02-25 00:08:00'
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
browser.find_element("link text", "亲，请登录").click()
print("请扫码")
browser.get("https://cart.taobao.com/cart.htm")

while True:
	if browser.find_element(By.ID, "J_SelectAll1"):
		browser.find_element(By.ID, "J_SelectAll1").click()
		break

while True:
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
	print(now)
	if now > times:
		while True:
			try:
				if browser.find_element("link text", "结 算"):
					print("结算")
					browser.find_element("link text", "结 算").click()

					break
			except:
				pass
	while True:
		try:
			if browser.find_element("link text", "提交订单"):
				print("抢到")
				browser.find_element("link text", "提交订单").click()
				print("已抢到")
				break
		except:
			pass
