import requests
import os 
#getting and saving an image
r  = requests.get('https://imgs.xkcd.com/comics/python.png')
if not os.path.exists('comic.png'):
    with open('comic.png', 'wb') as f:
        f.write(r.content)
    print("Image saved successfully!")
else:
    print("Image already exists. Skipping download.")

