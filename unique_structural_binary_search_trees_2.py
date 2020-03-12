class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def uniqueTrees(self, n):
        """
        Input: 3

        Output:
        [
        [1,null,3,2],
        [3,2,null,1],
        [3,1,null,null,2],
        [2,1,3],
        [1,null,2,null,3]
        ]

        """

        """
        Using the same intution of Catalan Numbers:
        left child = G(i-1)
        right child = G(n-i)

        we use memoization for cutting repeated operations

        1) For each point as center  
            construct left trees
            construct right trees
            Build Tree for each of these sub trees with point as center

        """

        def dfs(start, end, memo):
            if start > end:
                return [None]

            if (start, end) in memo:
                return memo[start, end]

            temp = []

            for center in range(start, end+1):

                l_left = dfs(start, center-1, memo)
                l_right = dfs(center+1, end, memo)

                for l in l_left:
                    for r in l_right:

                        root = TreeNode(center)
                        root.left = l
                        root.right = r

                        temp.append(root)

            memo[start, end] = temp

            return temp

        if n == 0:
            return []

        return dfs(1, n, {})


if __name__ == "__main__":

    obj = Solution()

    print(len(obj.uniqueTrees(4)))
