class Solution:
    def containerWithWater(self, heights):
        """
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
        n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
        Find two lines, which together with x-axis forms a container, such that the container contains the most water.

        Input: [1,8,6,2,5,4,8,3,7]
        Output: 49

        """

        """
        Approach: 

        Capacity is the min value at index start and index end * distance between them   
        capacity= min(heights[start],heights[end])*(end-start)

        We will keep a track of max_capacity while we traversing from start to end

        1) let start =0 , end = len(heights)-1 and  max_capacity =0
        2) Calculate c_capaity by using the above formula if it is greater than max_capacity assign it to it
        3) If height[start] > height[end] start +=1  , end -=1

        Time Complexity  : O(n)  n is length of the heights
        Space Complexity : O(1)

        """

        start = 0
        end = len(heights)-1
        max_capacity = 0

        while start < end:
            c_capacity = min(heights[start], heights[end])*(end-start)

            if c_capacity > max_capacity:
                max_capacity = c_capacity

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_capacity


if __name__ == "__main__":

    obj = Solution()

    print(obj.containerWithWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
