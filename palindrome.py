def is_palindrome(num):
    original = num
    reversed_num = 0

    while num > 0:
        rem = num % 10 
        reversed_num = reversed_num * 10 + rem
        num = num // 10  


    return original == reversed_num


num = int(input("Enter an integer number: "))


if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
