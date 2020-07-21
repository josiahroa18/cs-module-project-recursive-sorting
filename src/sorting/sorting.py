# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    a_pointer = b_pointer = 0
    while a_pointer < len(arrA) and b_pointer < len(arrB):
        if arrA[a_pointer] < arrB[b_pointer]:
            merged_arr.append(arrA[a_pointer])
            a_pointer += 1
        else:
            merged_arr.append(arrB[b_pointer])
            b_pointer += 1

    # Add remaining values from arrA
    while a_pointer < len(arrA):
        merged_arr.append(arrA[a_pointer])
        a_pointer += 1

    # Add remaining values from arrB
    while b_pointer < len(arrB):
        merged_arr.append(arrB[b_pointer])
        b_pointer += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

