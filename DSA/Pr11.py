#check if the array is sorted or not
def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [1,2,3,4,5]
if isSorted(arr):
    print("The array is sorted.")
else:
    print("The array is not sorted.")
