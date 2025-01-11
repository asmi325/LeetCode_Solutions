class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            # Check if the difference is already in the dictionary
            if diff in num_dict:
                return [num_dict[diff], i]
            # Store the number with its index
            num_dict[num] = i
        return []
