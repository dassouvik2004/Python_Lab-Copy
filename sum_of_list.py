def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = sum_of_list(numbers)
print(f"The sum of the list {numbers} elements:",result)