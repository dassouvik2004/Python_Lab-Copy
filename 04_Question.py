# Write a program to filter out even or odd numbers from a list.
def oddEven_Numbers(my_list):
    oddNumbers = []
    evenNumbers = []
    for num in my_list:
        if num%2==0:
            evenNumbers.append(num) 
        else:
            oddNumbers.append(num)
            
    return oddNumbers,evenNumbers

my_list = [1,2,3,4,5,6,7,8,9,10]
odd_num,even_num = oddEven_Numbers(my_list)
print("The odd numbers are:",odd_num)
print("The even numbers are:",even_num)