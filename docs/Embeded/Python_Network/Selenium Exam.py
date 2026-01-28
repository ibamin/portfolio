import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

max_cnt = 20
keyword = "wallpaper"
url = f"https://www.pexels.com/ko-kr/search/{keyword}/"

options = webdriver.EdgeOptions()
options.use_chromium = True  # Microsoft Edge Chromium을 사용
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--start-maximized")
driver_path = "C:\\msedgedriver.exe"  # Microsoft WebDriver 경로 설정

browser = webdriver.Edge(options=options)
browser.get(url)

photo_items = browser.find_elements(By.CLASS_NAME, "MediaCard_card__PAVEg")
img_urls = [
    x.find_element(By.TAG_NAME, "img").get_attribute("srcset") for x in photo_items
]

idx = 1
for img_url in img_urls:
    res = requests.get(img_url)

    if res.ok:
        file_name = f"{keyword}_{idx}.jpeg"

        with open(file_name, "wb") as f:
            f.write(res.content)

        print(f"({idx}) {file_name}")
        idx += 1

    if idx > max_cnt:
        break

browser.quit()
