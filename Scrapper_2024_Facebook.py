from facebook_scraper import get_posts
from facebook_page_scraper import Facebook_scraper


for post in get_posts('nintendo', pages=5):
    print(post['likes'][:50])



from selenium import webdriver
from selenium.webdriver.chrome.options import Options



from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(options=options)
#################
driver.get('https://realpython.com/openpyxl-excel-spreadsheets-python/')

page_or_group_name = "CuitlahuacGarciaJimenez"
posts_count = 5
browser = "firefox"
proxy = "usuario.scrapper.2024@outlook.com:prueba12345@IP:PORT" #if proxy requires authentication then user:password@IP:PORT
timeout = 200 #600 seconds
headless = True
isGroup= False

meta_ai = Facebook_scraper(page_or_group_name, posts_count, browser, proxy=proxy, timeout=timeout,
                            headless=headless, isGroup=isGroup)

json_data = meta_ai.scrap_to_json()
print(json_data)