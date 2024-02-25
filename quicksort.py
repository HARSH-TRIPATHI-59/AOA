

def QuickSort(arr,low,high):
    if low < high:
        q = partition(arr,low,high)
        QuickSort(arr,low,q-1)
        QuickSort(arr,q+1,high)
        
   
   
    
def partition(arr,low,high):
        X = arr[high]
        i = low-1

        for j in range(low,high):
            if arr[j] <= X:
               i = i+1
               (arr[i],arr[j]) = (arr[j],arr[i])
        (arr[i+1],arr[high]) = (arr[high],arr[i+1])
        return i+1



    


data = [10,80,30,90,40,50,70]
print(data)

size = len(data)

QuickSort(data,0,size-1)
print(data)






   










    

    



            
    
