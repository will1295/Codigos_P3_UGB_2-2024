from PIL import Image

img = Image.open("logob.jpg")
imgr = img.resize((450,200))
imgrot = img.rotate(90,expand=True)
imgrot.show()
#img.show()
#imgr.save("logoreco.jpg")