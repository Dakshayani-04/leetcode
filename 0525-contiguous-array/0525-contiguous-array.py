class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp={0:-1}
        sum=0
        max_length=0
        for i,num in enumerate(nums):
            if num == 1:
                sum += 1
            else:
                sum -= 1
            if sum in mp:
                max_length=max(max_length,i-mp[sum])
            else:
                mp[sum]=i
        return max_length
        