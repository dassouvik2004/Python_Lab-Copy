list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = []

for num in list1:
    if num in list2 and num not in intersection:
        intersection.append(num)

print("Intersection of two lists:",intersection)