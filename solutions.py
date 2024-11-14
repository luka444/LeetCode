class TwoSum(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]

class IsPalindrome(object):
    def isPalindrome(self, x):
        x = str(x)
        reversed_num = x[::-1]
        return x == reversed_num