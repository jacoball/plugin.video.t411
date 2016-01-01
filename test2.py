# coding: utf-8
import requests
browser = requests.Session()
page = "https://www.t411.in/users/login/?returnto=/t/5358656"
response = browser.get(page)

print response.text