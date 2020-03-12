class Solution:
    def sortColors(self, nums):
        """
        Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
        Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

        Input: [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]

        Constraints: 
        Do it in single pass and using O(1) space

        """

        """
        We use 3 pointers 0_boundary , 2_boundary and curr
        0_boundary is used to maintain the right boundary of 0's 
        2_boundary is used to maintain the left boundary of 2's

        let 0_boundary, curr  be 0  and 2_boundary be len(input)

        if curr element is 0 then we swap curr and 0_boundary , increment 0_boundary and curr
        if element is 2 then we swap 2_boundary and curr, decrement 2_boundary
        else increment curr

        """

        z_boundary = curr = 0
        t_boundary = len(nums)-1

        while curr < t_boundary:

            if nums[curr] == 0:
                nums[z_boundary], nums[curr] = nums[curr], nums[z_boundary]
                curr += 1
                z_boundary += 1

            elif nums[curr] == 2:
                nums[curr], nums[t_boundary] = nums[t_boundary], nums[curr]
                t_boundary -= 1
            else:
                curr += 1


if __name__ == "__main__":

    obj = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    obj.sortColors(nums)

    print(nums)
