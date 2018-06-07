# -*- coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get("http://www.bing.com/")

print(driver.title)
#微软 Bing 搜索 - 国内版

data = driver.find_element_by_id("scpl1").text

print(data)

driver.find_element_by_id("sb_form_q").send_keys(u"python爬虫")
driver.find_element_by_id("sb_form_go").click()
driver.save_screenshot("python爬虫.png")


# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
driver.quit()