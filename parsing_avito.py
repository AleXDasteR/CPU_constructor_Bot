import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.avito.ru/kazan/tovary_dlya_kompyutera?cd=1&q=rtx+3080'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
time.sleep(3)
bs = BeautifulSoup(response.text, 'html')

print(response)
