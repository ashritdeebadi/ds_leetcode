class Solution:

    def increasingTriplets(self, nums):
        """
        Given a sequence find if there exists an increasing subsequence triplets such that nums[f] <nums[m]<nums[l]
        Need not be continuous

        Input: [1,2,3,4,5]
        Return : True

        Input: [5,4,3,2,1]
        return : False

        Input: [5,1,5,5,2,5,4]
        return : True

        Constraints:

        TimeComplexity: O(n)
        SpaceComplexity: O(1)

        """

        """
        Approach:

        1) Lets create two variables first , second and let them be inf
        2) check for the first least element and assign it to first
        3) check for the second least element and assign it to second
        4) if there exists third element greater then first and second return True  else False

        """

        first = second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


if __name__ == "__main__":

    obj = Solution()
    print(obj.increasingTriplets([1, 2, 3, 4, 5]))
    print(obj.increasingTriplets([5, 4, 3, 2, 1]))
    print(obj.increasingTriplets([5, 1, 5, 5, 2, 5]))
