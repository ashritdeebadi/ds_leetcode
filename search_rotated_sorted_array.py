class Solution:
    def search(self, nums, target):

        # input : [0,1,2,4,5,6,7] before calling will change at some pivot value [4,5,6,7,0,1,2] and target =0
        # return index in pivot list : 4
        """
        1) Find the point at which the pivot is created
        2) Binary search at left if the target is less than the pivot index 
        3) Binary search at right if the target is greater than pivot index

        Time Complexity     : O(log(n))
        Space COmplexity    : O(1) 

        Reference           : https://www.youtube.com/watch?v=QdVrY3stDD4

        """

        # Finding pivot index

        left = 0
        right = len(nums)-1

        while left < right:

            mid = left + (right-left) // 2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        print("Pivot found at {}".format(left))

        # Check if has to search from right of pivot or left of pivot

        start = left
        left = 0
        right = len(nums)-1

        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start-1

        while(left < right):
            mid = left+(right-left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                # be careful over here if you wont increment it will fail for NOT FOUND (-1) cases
                left = mid + 1
        return -1


Test = Solution()

print(Test.search([4, 5, 6, 7, 0, 1, 2], 10))
