class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = 0
        index = 0
        count = 0
        tmp = [0]*len(arr)
        for i in range(len(arr)):
            new = i+1
            for j in range(new,len(arr)):
                if arr[j] >= max:
                    max = arr[j]
            tmp[i] = max
            max = 0
            
        tmp[len(arr)-1] = -1
        return tmp


