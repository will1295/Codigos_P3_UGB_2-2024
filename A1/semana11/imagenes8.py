from PIL import Image
from urllib.request import urlopen

url = "https://upload.wikimedia.org/wikipedia/commons/f/f9/Magnolia_grandiflora1Stuart_Yeates.jpg"
img = Image.open(urlopen(url))
img.show()