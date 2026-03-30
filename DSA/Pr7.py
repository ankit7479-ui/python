# selection sort
def selection_sort(arr):
    n = len(arr)
        
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("After selection sort:")
    print(*arr)


# Driver code
arr = [13, 46, 24, 52, 20, 9]

print("Before selection sort:")
print(*arr)
selection_sort(arr)
        