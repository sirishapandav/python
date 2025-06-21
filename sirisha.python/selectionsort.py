def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        lower=i
        for j in range (1+i,n):
            if arr[j] < arr[lower]:
                lower = j
        arr[i], arr[lower] = arr[lower], arr[i]   
arr=[5,4,3,2,1] 
selection_sort(arr)
print(arr)        