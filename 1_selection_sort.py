"Selection Sort Techniques"

def selection_sort(arr):
    for i in range(len(arr)-1):
        mini=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[mini]:
                mini=j
        arr[mini],arr[i]=arr[i],arr[mini]
    return arr

arr=[50,60,23,56,76,33,234,56]
output=selection_sort(arr)
print(output)