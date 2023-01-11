"""https://leetcode.com/problems/contains-duplicate/"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return len(unique) < len(nums)


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        return list(nums_set) != nums