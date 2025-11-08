class Solution(object):
    def kthSmallest(self, matrix, k):
        arr=[]
        for i in matrix:
            for j in i:
                arr.append(j)
        for i in range(len(arr)):
            mini=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[mini]:
                    mini=j
            arr[mini],arr[i]=arr[i],arr[mini]
        
        for i in range(len(arr)):
            if k<0:
                return -1
            if i==(k-1):
                return arr[i]
        return -1

        
        
arr=[[1,2],[1,3]]
k=2
sol=Solution()
output=sol.kthSmallest(arr,k)
print(output)