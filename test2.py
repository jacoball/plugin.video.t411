# coding: utf-8
import requests
import os

browser = requests.Session()
page = "https://www.t411.in/users/login/?returnto=/t/5358656"
response = browser.get(page)
dirPath = xbmc.translatePath('special://temp')
path = os.path.join(dirPath, '1.torrent')
with open(path, 'wb') as handle:
    for block in response.iter_content(1024):
        handle.write(block)
# Set-up the plugin
link = 'plugin://plugin.video.torrenter/?action=playSTRM&url=' + path + '&not_download_only=True'
