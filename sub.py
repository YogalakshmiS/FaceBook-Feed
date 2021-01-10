
'''Exc 3:  Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.'''


def rev_arr(arr, n, k): 
    i = 0
    while(i<n): 
        left = i  
        right = min(i + k - 1, n - 1)  
        while (left < right): 
            arr[left], arr[right] = arr[right], arr[left] 
            
            left=left+1
            right=right-1
        i=i+k 
arr = [1, 2, 3, 4, 5]  
  
k = 3
n = len(arr)  
rev_arr(arr, n, k) 
  
for i in range(0, n): 
        print(arr[i], end =" ") 
          
