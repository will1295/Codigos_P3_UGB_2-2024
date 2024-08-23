try:
    def div(num1,num2):
        total = num1/num2
        return total
    print(div(10/0))
except:
    print("No se puede dividir entre cero!")
