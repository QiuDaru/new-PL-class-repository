from selenium import webdriver
import selenium

# 初始化 Chrome 瀏覽器驅動
driver = webdriver.Chrome()

# 打開 Google 首頁
driver.get("https://www.google.com")

# 找到搜尋框
search_box = driver.find_element_by_name("q")

# 在搜尋框中輸入關鍵字並提交搜尋
search_box.send_keys("OpenAI")
search_box.send_keys(Keys.RETURN)

# 等待一些時間，讓頁面加載完成
driver.implicitly_wait(5)

# 獲取搜索結果的標題並打印出來
search_results = driver.find_elements_by_css_selector("h3")
for result in search_results:
    print(result.text)

# 關閉瀏覽器
driver.quit()
