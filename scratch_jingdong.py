from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

times = '2023-02-25 00:08:00'
browser = webdriver.Chrome()
browser.get("https://www.jd.com/")
browser.find_element("link text", "你好，请登录").click()
print("请扫码")
browser.get("https://cart.jd.com/cart_index")

while True:
	if browser.find_element(By.NAME, "select-all"):
		browser.find_element(By.NAME, "select-all").click()
		break

while True:
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
	print(now)
	if now > times:
		while True:
			try:
				if browser.find_element("link text", "去结算"):
					print("去结算")
					browser.find_element("link text", "去结算").click()

					break
			except:
				pass
	while True:
		try:
			if browser.find_element(By.ID, "order-submit"):
				print("抢到")
				browser.find_element(By.ID, "order-submit").click()
				print("已抢到")
				break
		except:
			pass
