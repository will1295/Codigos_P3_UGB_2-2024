from PIL import Image
from urllib.request import urlopen

url = "https://upload.wikimedia.org/wikipedia/commons/6/6b/Mimulus_nectar_guide_UV_VIS.jpg"
imagen = Image.open(urlopen(url))
#imagen.show()
imagen.save("flor.jpeg")