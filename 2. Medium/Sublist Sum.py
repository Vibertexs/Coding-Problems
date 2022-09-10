'''
Given a list of integers nums, return whether there is a sublist such that its sum is strictly larger than the total sum of the list.

Example 1
    Input
        nums = [1, -2, 3, 4]
    Output
        True

Explanation
    The sum of the list is 6 and the sum of the sublist [3, 4] is 7 which is strictly larger.

Example 2
    Input
        nums = [-2]
    Output
        True
Explanation
    The sum of the list is -2 and we can choose the empty sublist ([]) for a sum of 0.
'''
class Solution:
    def solve(self, nums):

        summ = sum(nums)
        counts = 0

        if len(nums) == 1 and summ >= 0:
            return False

        if summ < 0:
            return True


        for i in nums:
            counts += i
            if counts > 0:
                if counts > summ:
                    return True
            else:
                counts = 0

        return False