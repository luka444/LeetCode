class Solution(object):
    def twoSum(self, nums, target):
       data = {}
       for i, num in enumerate(nums):
            diff = target - num
            if diff in data:
                return [data[diff], i]
            data[num] = i

class IsPalindrome(object):
    def isPalindrome(self, x):
        x = str(x)
        reversed_num = x[::-1]
        return x == reversed_num