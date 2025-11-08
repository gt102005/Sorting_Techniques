class Solution(object):
    def sort_first(self,a,b):
        a=str(a)
        b=str(b)
        if a+b>b+a:
            return True
        else:
            return False

    def largestNumber(self, nums):
        if any(nums) != False:
            for i in range(len(nums)-1):
                mini=i
                for j in range(i+1,len(nums)):
                    if self.sort_first(nums[j],nums[mini]):
                        mini=j
                nums[mini],nums[i]=nums[i],nums[mini]

            output=""
            for i in range(len(nums)):
                output+=str(nums[i])
            return [output, nums]
        else:
            return 0



arr=[0,1]
solution=Solution()
output=solution.largestNumber(arr)
print(output)
