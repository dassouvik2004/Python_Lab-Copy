def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2  # Find the middle index

        # Check if the target is at the middle
        if arr[mid] == target:
            return True
        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            end = mid - 1
        # If target is greater, ignore the left half
        else:
            start = mid + 1

    
    return False


input_list = list(map(int, input("Enter a list of integers (separated by spaces): ").split()))

input_list.sort()


target = int(input("Enter the element to search for: "))

if binary_search(input_list, target):
    print(f"{target} is found in the list.")
else:
    print(f"{target} is not found in the list.")