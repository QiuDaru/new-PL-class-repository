from selenium import webdriver

# 创建 Chrome WebDriver
driver = webdriver.Chrome()

# 打开网页
driver.get('https://www.youtube.com/')

# 获取网页源代码
pageSource = driver.page_source

# 打印网页源代码
print(pageSource)

# 关闭浏览器
driver.quit()
