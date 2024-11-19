import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2F482375515237611%2Fphotos%2Fa.484333898375106%2F2449768388498304%2F%3Ftype%3D3&show_text=false&width=350"

req = requests.get(url)

content = req.text

soup = BeautifulSoup(content, 'html.parser')

imagen_width = soup.find('img', class_='scaledImageFitWidth img')
for img in imagen_width:
    print(img['src'])

imagen_height = soup.find_all('img', {'class': 'scaledImageFitHeight img'})
for img in imagen_height:
    print(img['src'])





