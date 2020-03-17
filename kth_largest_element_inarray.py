import random


class Solution:

    def kLargestElement(self, nums, k):
        """
        Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

        Example 1:

        Input: [3,2,1,5,6,4] and k = 2
        Output: 5
        Example 2:

        Input: [3,2,3,1,2,4,5,5,6] and k = 4
        Output: 4
        """

        """
        We will solve this using pivot element logic 
        
        1) lets have two variables L =0 and R = len(arr) if L==R  only one element
        2) pivot element is a random element pivot_index=random.randint(l,r)
        3) pivot_index = partition(l,r,pivot_index)
        4) if pivot_index == n-k : return pivot index , elif < then select(l,pivot_index-1,n-k) else select(pivot_index+1,r,n-k)


        partition:

        pivot= arr[pivot_index]
        move pivot index to right:
        arr[pivot_index],arr[right]=arr[right],arr[pivot_index]

        actucal_p=left

        for i from l to r:
            if arr[i] < pivot:
                arr[l],arr[pivot] =arr[pivot],arr[l]
                actucal_p+=1

        Moving to actual position of the element 
            arr[r],arr[actual_p]=arr[actual_p],arr[r]

            return actual_p

        Time COmplexity : O(n) average case 
        Spcae Complexity : O (1)

        """

        def partition(L, R, pivot_index):
            """
            Finds the actual index position of the element in actual sorted arr
            """
            pivot = nums[pivot_index]

            nums[pivot_index], nums[R] = nums[R], nums[pivot_index]
            actual_p = L
            for i in range(L, R):
                if nums[i] < pivot:
                    nums[actual_p], nums[i] = nums[i], nums[actual_p]
                    actual_p += 1

            # putting the pivot element in theor correct index

            nums[R], nums[actual_p] = nums[actual_p], nums[R]
            print(nums)
            return actual_p

        def select(L, R, n_smallest):

            if L == R:
                return nums[L]

            pivot_index = random.randint(L, R)

            pivot_index = partition(L, R, pivot_index)

            if pivot_index == n_smallest:
                return nums[n_smallest]
            elif n_smallest < pivot_index:
                return select(L, pivot_index-1, n_smallest)

            else:
                return select(pivot_index+1, R, n_smallest)

        return select(0, len(nums)-1, len(nums)-k)


if __name__ == "__main__":

    obj = Solution()

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    print(obj.kLargestElement(nums, k))
