import matplotlib.pyplot as plt
from collections import Counter

op = ["azul","rosado","morado","rojo"
      ,"azul","amarillo","gris","lila"
      ,"magenta","flamingo","verde"
      ,"morado","cyan","rojo","magenta",
      "rojo","negro","rojo","azul","aqua"]

fr = Counter(op)
plt.pie(fr.values()
        ,labels=fr.keys(),autopct="%1.1f%%")
plt.show()
