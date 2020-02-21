class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader  reader.get(k) gives value at index k 
        :type target: int
        :rtype: int
        """

        """
        1) Find the rightmost boundray , Since the r is unknown start with 1 and keep multiplying it with 2 
        2) Once the boundray is found do binary search to find element value 

        Time COmplexity  : O(logT) where T is the index of target  
        Space Complexity : O(1)

        """

        left = 0
        right = 1

        while left <= right:

            mid = left + (right-left)//2

            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid-1
            else:
                left = mid+1
                right *= 2           # doing this to find boundary
        return -1
