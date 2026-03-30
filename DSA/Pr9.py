#insertion sort
class InsertionSort:
    def insertiosort(self,nums):
        n = len(nums)
        for i in range (1,n):
            key = nums[i]
            j = i - 1
            
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j] 
            j -= 1   
            
        return nums   
    
if __name__ :"__main__"
InsertionSort = InsertionSort()
nums = [13, 46, 24, 52, 20, 9]     
print("Before using Insertion Sort")
for num in nums:
        print(num, end=" ")
        print()
        

nums = InsertionSort.insertiosort(nums)
print("After using Insertion sort")
for num in nums:
    print(num,end=" ")
    print()