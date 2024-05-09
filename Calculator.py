class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        else:
            return x / y


cal = Calculator()


a1 = float(input('Enter first number:'))

a2 = str(input('Enter the operation number:'))

a3 = float(input('Enter second number:'))

if a2 == '+' :
    print(cal.add(a1 , a2))

elif a2 == '-':
    print(cal.subtract(a1 , a3))

elif a2 == '*':
    print(cal.multiply(a1 , a3))

elif a2 == '/':
    print(cal.divide(a1 , a3))

else:
    print("Invalid input")
    