def max_min(input_list):
    max = input_list[0]
    min = input_list[0]
    
    for item in input_list:
        if item > max:
            max = item
        if item < min:
            min = item
    
    return max, min


input_list = list(map(int,input("Enter numbers separated by spaces: ").split()))
maximum, minimum = max_min(input_list)
print("Maximum:", maximum)
print("Minimum:",minimum)