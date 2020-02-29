class Solution:
    def rearrange(self, people):
        """
        Suppose you have a random list of people standing in a queue.
        Each person is described by a pair of integers (h, k), where h is the height of the person and
        k is the number of people in front of this person who have a height greater than or equal to h.
        Write an algorithm to reconstruct the queue.

        Input:  [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

        Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

        """

        """
        Greedy:

        Intution:

        Arranging all taller people first then , inserting the second highest based on index(no. of taller people infront of them)

        1) sort all the values on decreasing height h ,then k
        2) Insert all values based on k - index position

        Time Complexity : O(N^2)
        Space Complexity : O(N)

        """
        people.sort(key=lambda x: (-x[0], x[1]))

        ans = []

        for p in people:
            ans.insert(p[1], p)
        return ans

    def custom_sort(self, people):
        ans = []
        heights = {}
        for h in people:
            if h[0] not in heights:
                heights[h[0]] = [h]
            else:
                heights[h[0]].append(h)

        for h in sorted(heights.keys(), reverse=True):
            internal = {}
            for i in heights[h]:
                if i[1] not in internal:
                    internal[i[1]] = i

            for i in sorted(internal.keys()):
                ans.append(internal[i])
        return ans


obj = Solution()

print(obj.rearrange([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
