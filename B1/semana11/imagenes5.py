from PIL import Image
from urllib.request import urlopen

direcs = "https://upload.wikimedia.org/wikipedia/commons/a/a1/Lamiastrum_galeobdolon.jpg"
img = Image.open(urlopen(direcs))
img.show()