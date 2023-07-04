def maximum():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    c = int(input("enter third number: "))

    print(max(a, b, c))

maximum()

def sum_of_number():
    li = [8, 2, 3, 0, 7]

    print(sum(li))
sum_of_number()

def multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


print(multiply([8, 2, 3, -1, 7]))

def reverse_stirng():
    st = input("enter one string: ")
    print(st[::-1])
reverse_stirng()

def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        print("please enter positive number.")
    else:
        return num * factorial(num-1)


num = int(input("Input a number to compute the factorial : "))
print(factorial(num))
