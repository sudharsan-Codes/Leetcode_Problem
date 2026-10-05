class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count ={}
        ans = 0
        for num in nums:
            if num in count:
                ans += count[num]
            count[num] = count.get(num,0 ) + 1 
        return ans