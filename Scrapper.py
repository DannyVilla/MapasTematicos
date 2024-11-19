from facebook_scraper import get_posts,set_cookies
import pandas as pd
from http import cookiejar
import requests
def format_comment(c):
    obj = {
        "comment_id": c["comment_id"],
        "comment_text": c["comment_text"],
        "comment_reaction_count": c["comment_reaction_count"] or 0,
        "reply_count": len(c["replies"]) if "replies" in c else 0,
        "comment_time": c["comment_time"]
    }
    if c["comment_reactions"]:
        obj.update(c["comment_reactions"])
    return obj

fb_comments = []

file = 'facebook.com_cookies.txt'
cookie = cookiejar.MozillaCookieJar()
cookie.load(file)
cookies = requests.utils.dict_from_cookiejar(cookie)
set_cookies(cookies)  #error message

posts = get_posts(group='atomyprobiotics', pages=2, options={"comments":True,"posts_per_page":4})
for post in posts:
    #print(post['comments_full'])
    if post['comments_full']:
        for comment in post['comments_full']:
            fb_comments.append(format_comment(comment))
            for reply in comment['replies']:
                fb_comments.append(format_comment(reply))
print(fb_comments)

pd.DataFrame(fb_comments).to_csv('fbcomments.csv',index=False)