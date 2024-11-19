from facebook_page_scraper import Facebook_scraper

#instantiate the Facebook_scraper class

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
