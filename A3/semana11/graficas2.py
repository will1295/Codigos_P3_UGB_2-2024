import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,9,8,7,6]

#plt.plot(x,y)
#plt.bar(x,y) 
plt.pie(y,labels=x)
plt.show()