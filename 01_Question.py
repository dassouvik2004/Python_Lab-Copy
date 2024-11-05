# Write a program to find the maximum and minimum elements in a list
def find_maxMin(my_list):
    max_element = my_list[0]
    min_element = my_list[0]
    for num in my_list[1:]:
        if num>max_element:
            max_element = num
        if num<min_element:
            min_element = num
    return max_element,min_element
my_list = [10,20,50,30,15]
print("The List:",my_list)
max_element,min_element = find_maxMin(my_list)
print("Maximum element:",max_element)
print("Minimum element:",min_element)