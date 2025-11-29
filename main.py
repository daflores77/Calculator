
def doMath(x, y, oper):
    match oper:
        case "+":
            sum = x + y
        case "-":
            sum = x - y
        case "*":
            sum = x * y
        case "/":
            if (num2 == 0):
                return 0
            sum = x / y

    return sum


num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
operation = input("Please enter the operation: ")

while (operation != "+" and operation != "-" and operation != "/" and operation != "*"):
    operation = input("Please enter the operation: ")
    print(operation)


print(num1,operation,num2)

answer = doMath(num1, num2, operation)

print("The answer is:",answer)