def armstrong(num):
    original = num
    digits = len(str(num))
    sum = 0

    while(num > 0):
        rem = num % 10
        sum = sum + (rem ** digits)
        num = num // 10

    return original == sum


num = int(input("Enter a number: "))
if armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")