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

class RomanToInt(object):
    def romanToInt(self, s):
        data = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and data[s[i]] < data[s[i+1]]:
                num -= data[s[i]]
            else:
                num += data[s[i]]
        return num