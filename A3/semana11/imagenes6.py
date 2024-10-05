from PIL import Image,ImageFilter
from urllib.request import urlopen

url = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Lago_di_Arosa.jpg"
img = Image.open(urlopen(url))
#img.show()
img.filter(ImageFilter.CONTOUR).show()
#img.save("paisaje2.jpeg")