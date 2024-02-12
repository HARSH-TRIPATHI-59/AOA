list = {}
n = int(input("Enter the number"))
for i in range(0,n):
        list[i] = int(input("Enter the number"))
low = 0
high = n
key = int(input("Enter the key"))
  
while(low<=high):
      mid = int((high+low)/2)
    
      if(list[mid] == key):
        print("Element found at", mid)
        break
        
      elif(list[mid] < key):
        low = mid+1
      else:
        high = mid-1
        

    
           



 
        
    

    

