import requests
from bs4 import BeautifulSoup
import os

def search_img(query):
    url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch'.format(query)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img', {'class':'yWs4tf'})
    img_url = []
    for image in images:
        url = image['src']
        print(url)
        img_url.append(url)
    return img_url

save_path = "---" # Wherever you want to safe the file on your system.

def download_img(img_url, query):
    for i, url in enumerate(img_url[:5]):
        response = requests.get(url)
        if response.status_code == 200:
            filename = f'{query}{i}.jpg'
            filepath = os.path.join(save_path, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)


query = 'Microsoft' # Enter the query to download the images 
img_url = search_img(query + ' logo')
download_img(img_url, query+' logo')
