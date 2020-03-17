
class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        we solve this using krushal's algorithm 
        IF we make the wells as Nodes and the pipes as edges then this problem would be reduced as a MST problem 
        We use disjoin sets to solve this

        1) We create a map to keep track of the path with nodes d={i:i for i in range(n+1)}
        2) we create pipes cost
        3) we create wells cost
        4) total = pipes_cost +wells_cost  and we sort them based on cost 
        5) we write find function to find which set it belongs to 
                find(x):
                    if x != uf[x]:
                        uf[x]=find(uf[x])  # by doing this we update the set to which the node belongs ie, 
                                                when a node is pickes its updates here
        6) we choose the minimum cost elements if they are not already in the set then they are addes in the set

        """

        uf = {i: i for i in range(n+1)}

        well_cost = [[c, 0, i] for i, c in enumerate(wells, 1)]
        pipes_cost = [[c, i, j] for i, j, c in pipes]

        total = sorted(well_cost+pipes_cost)

        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
        ans = 0
        for c, x, y in total:

            x, y = find(x), find(y)

            if x != y:
                uf[x] = find(uf[y])
                ans += c
                n -= 1
            if n == 0:
                return ans


if __name__ == "__main__":
    n = 4
    wells = [1, 2, 2, 4]
    pipes = [[1, 2, 3], [2, 3, 1], [1, 3, 2], [1, 4, 4], [2, 4, 4]]

    obj = Solution()

    print(obj.minCostToSupplyWater(n, wells, pipes))
