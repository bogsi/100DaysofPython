num = []
def is_prime(num):
    global number
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter your Number: "))
print(is_prime(number))
