# Write a program to flatten a nested list (i.e., convert a list of lists into a single list)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list = []

for sublist in nested_list:
    for item in sublist:
        flatten_list.append(item)

print("The flatten list:",flatten_list)