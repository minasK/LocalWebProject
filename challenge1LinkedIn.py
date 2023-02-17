# factorial def
def factorial(fact):
    if type(fact) is not int:
        return None
    if fact < 0:
        return None
    if fact == 0:
        print("1")
        return 1


    n = fact
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("The factorial of the number you put is : ", end="")
    print(fact)


factorial(6)

print(1.2-1.0)