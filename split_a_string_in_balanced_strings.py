class Solution:

    def splitstring(self, s):
        """
        Balanced strings are those who have equal quantity of 'L' and 'R' characters.

        Given a balanced string s split it in the maximum amount of balanced strings.

        Return the maximum amount of splitted balanced strings. 

        Input: s = "RLRRLLRLRL"
        Output: 4
        Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.  

        Leetcode: 1221

        """

        """
        1) Use counters to count no. of occurances of R 
        2) If "R" then increase counter by 1
        3) Else decrease counter by 1
        4) if counter is zero , means one equal balanced split ; Increase answer by 1

        Time Complexity: O(N)
        Space Complexity: O(1)

        Reference : https://leetcode.com/problems/split-a-string-in-balanced-strings/discuss/522691/Two-Python-Solutions-(Stack-and-Counter) 

        """

        counter = 0
        ans = 0

        for letter in s:
            if letter == "R":
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                ans += 1
        return ans


obj = Solution()

print(obj.splitstring('RLRRLLRLRL'))
