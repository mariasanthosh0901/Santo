def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
        print(L)
        print(len(L))
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
arr=list(map(int,input().split()))
mergeSort(arr[1:])
printList(arr[1:])
