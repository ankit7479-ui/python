# Bubble sort
from ast import arg


class BubbleSort:
     def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1, -1, -1):
            for j in range(i):  
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  
        
        print("After Using Bubble Sort:")
        print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Using Bubble Sort:")
    print(" ".join(map(str, arr)))

    sorter = BubbleSort()
    sorter.bubble_sort(arr)