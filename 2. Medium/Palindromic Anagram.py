'''
Given a string s, determine whether any anagram of s is a palindrome.
'''

class Solution:
    def solve(self, s):
        ones = 0
        print(set(s))
        for i in(set(s)):
            x=s.count(i)
            print(x)
            if(x%2==1):
                ones+=1
                if(ones>1 or len(s)%2==0):
                    return False
        return True

print(Solution().solve([-9, -2, 0, 2, 3]))