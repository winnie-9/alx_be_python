def perform_operation(num1,num2,operation):


    operation = input("Enter operation:(add,subtract,multiply,divide) ").lower()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation" 
result = perform_operation(1,1 , 'add')
print(f"Result: {result}")