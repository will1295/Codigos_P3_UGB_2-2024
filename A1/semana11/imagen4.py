from PIL import Image

#imagent = Image.open("tigre.png")
#imgrot=imagent.rotate(45,expand=True)
#imgrot.show()
imagent = Image.open("tigre.png").rotate(45,expand=True)
imagent.show()

imageres = Image.open("tigre.png").resize((300,200))
imageres.show()
