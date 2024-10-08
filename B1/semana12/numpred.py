import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

modelo = tf.keras.datasets.mnist

(x_train,y_train), (x_test,y_test) =modelo.load_data()

x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255

red = models.Sequential([
    layers.Flatten(input_shape=(28,28)), #Neurona de entrada
    layers.Dense(128,activation="relu"), #Neurona(s) de procesam.
    layers.Dropout(0,2), #Neurona de regulacion
    layers.Dense(10,activation="softmax") #Neurona de salida
])

red.compile(optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"])

entranm = red.fit(x_train,y_train,epochs=10,
                    batch_size=32,validation_split=0.32)

test_loss,test_acc = red.evaluate(x_test,y_test,verbose=2)
print(test_acc)
print(test_loss)
