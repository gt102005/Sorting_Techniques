#Insertion Sort without Recursion

def Insertion_Sort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1
    return arr


arr=[3,4,52,12,2,24,4,6]
output=Insertion_Sort(arr)
print(output)
