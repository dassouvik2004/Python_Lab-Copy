# Write a program to remove all occurrences of a specific element from a list

my_list = [1,2,3,4,5,3,6,3]

remove_num = 3

new_list = []

for item in my_list:
    if item!= remove_num:
        new_list.append(item)
    
print(f"List after removing all occurance of {remove_num}:",new_list)