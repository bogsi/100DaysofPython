''''
somewhere to store result
+
-
*
/
Calculator
'''

def add(n1, n2):
    return n1 + n2

# TODO: Write out  3 Functions - subtrakt, divide, multiply
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": subtract, 
    "*": multiply,
    "/": divide
}
def calculator():
    should_acumulate = True
    num1 = float(input("What is the first number? "))

    while should_acumulate:
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the  second number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.")
        if choice == "y":
            num1 = answer
        else:
            should_acumulate = False
            print("\n" * 20)


calculator()
