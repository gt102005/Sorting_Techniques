# Implementation of the buubble sort

def Bubble_Sort(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr=[2,3,4,1,2,65,753,22,12]
output=Bubble_Sort(arr)
print(output)
