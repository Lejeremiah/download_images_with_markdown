import os
import requests
import re
from urllib.parse import urlparse
import shutil
def download_img(url,save_path):
    proxies = {
        'http':'http://127.0.0.1:7890',
        'https':'http://127.0.0.1:7890'
    }
    r = requests.get(url,proxies=proxies, stream=True)
    if r.status_code == 200:
        open(save_path, 'wb').write(r.content)
    del r

tmp = os.chdir('bugs')
if os.path.exists("markdown_source"):
    tmp = os.listdir()
    os.chdir("markdown_source")
else:
    os.mkdir("markdown_source")
    tmp = os.listdir()
    os.chdir("markdown_source")

markdown_name_list = tmp
for item in markdown_name_list:
    print(item.encode())
    if not item[-2:] == 'md':
        continue
    if not os.path.exists(item):
        os.mkdir(item)
    else:
        continue
    
    with open(f"../{item}","r",encoding="utf8") as f:
        text = f.read()
    try:
        image_links = re.findall("\!\[.*?\]\((.*?)\)",text)
        for image_link in image_links:
            print(image_link)


            url_parse = urlparse(image_link).path[1:].replace('/','_')
            save_path = f'./{item}/{url_parse}'
            download_img(image_link,save_path)

            text = text.replace(image_link,f'./markdown_source/{item}/{url_parse}')
        with open(f"../{item}",'w',encoding="utf8") as f:
            f.write(text)
    except:
        shutil.rmtree(item)
