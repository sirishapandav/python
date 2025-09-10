#iteration
class solution:
    def subsets(self,nums:list[int])->list(list[int]):
        result=[[]]
        for num in nums:
            subset=[curr+[num] for curr in result]
            result+=subset
        return result
        
#backtrack method#
class solution:
    def subsets(self,nums:list[int])->list(list[int]):
        result=[]
        def bt(start,subset):
            result.append(subset.copy())
            for i in range(start,len(nums)):
                subset.append(nums[i])
                bt(i+1,subset)
                subset.pop()
        bt(0,[])
        return result        

#bitmasking
class solution:
    def subsets(self,nums:list[int])->list(list[int]):
        n=len(nums)
        res=[]
        for i in range(1<<n):
            sub=[]
            for j in range(n):
                if i&(1<<j):
                    sub.append(nums[j])
            res.append(sub)
        return res            
            

