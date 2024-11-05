# Write a program to find the union of two lists (i.e., all unique elements from both lists).

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

union = list1.copy()

for num in list2:
    if num not in union:
        union.append(num)

print("Union of two lists:",union)