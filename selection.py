data = [5,2,1,4,3]
n = len(data)

for i in range(n):
    min = i
    for j in range(i+1,n):
        if data[j] < data[min]:
           min = j
           
         
    data[i],data[min] = data[min],data[i]
    
print(data)
         