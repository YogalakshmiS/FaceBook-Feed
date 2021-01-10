
'''Exc 4: Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.'''



def len_arr(arr): 
    
    s = 0  
    for i in range(len(arr)):  
        sum = 0               
        for j in range(i, len(arr)):           
            sum += arr[j]            
            if sum == 0: 
                s = max(s, j-i + 1) 
    return s   
  
arr = [15, -2, 2, -8, 1, 7, 10, 13]   
print (len_arr(arr))
