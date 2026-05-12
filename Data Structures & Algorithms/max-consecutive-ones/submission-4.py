class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    
        current = nums[0]
        count = 0
        c_list = []
        for n in nums:
            if n == 1:
                count+=1
                print(count)
            else:
                if count>0:
                    c_list.append(count)
                count = 0
        c_list.append(count)
        print(c_list)
        if len(c_list)<1:
            return 0
        return max(c_list)
        