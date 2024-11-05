# Write a program to rotate a list by a given number of positions

def rotate(list,positions):
    if not list:
        return list
    positions = positions % len(list)

    rotate_list = list[-positions:] + list[:-positions]

    return rotate_list

my_list = [10,20,30,40,50,60,70]
positions = 4
rotate_list = rotate(my_list,positions)
print(rotate_list)