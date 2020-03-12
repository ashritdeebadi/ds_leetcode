class Solution:

    def coinChange(self, amount, coins):
        """
        Given an infinite supply  of coin demoninations Return all possible way to create a sum of Amount

        Input: amount = 5, coins = [1, 2, 5]
        Output: 4
        Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1 

        """

        """
        We can solve this efficiently using Dynamic programming , the intution is using 0-1 Knapsack problem 

        1) Build a Matrix of M[r][c] = [amount+1][len(coins)+1]
        2) Fill the first row with zeros's (As sum 0 can be produced without taking any coin)
        3) At each point M[c_amount][coin] = value if we dont include the coin M[c_amount][coin-1] and 
            if value of the amount is less that current value  include it i.e, coins[coin-1]<=c_amount
            Then M[c_amount][coin]+= M[c_amount-coins[coin-1]][coin]
        4) Return the last M[-1][-1]

        Time Complexity : O(m*n) m=len(coins) n=amount
        Space COmplexity : O(m*n) 

        """

        matrix = [[0 for i in range(len(coins)+1)] for j in range(amount+1)]

        for i in range(len(coins)+1):
            matrix[0][i] = 1

        for c_amount in range(1, amount + 1):
            for coin in range(1, len(coins)+1):

                matrix[c_amount][coin] = matrix[c_amount][coin-1]

                if coins[coin-1] <= c_amount:
                    matrix[c_amount][coin] += matrix[c_amount-coins[coin-1]][coin]

        return matrix[-1][-1]

    def coinChange_optmized(self, amount, coins):
        """
        Same intution as above we optimize the space by restricting the coin range from coin to unt+1

        Space Complexity : O(m)  where m is the value 

        """

        M = [0 for i in range(amount+1)]
        M[0] = 1

        for coin in coins:
            for C_amount in range(coin, amount+1):
                M[C_amount] += M[C_amount-coin]

        return M[-1]


if __name__ == "__main__":

    obj = Solution()

    print(obj.coinChange(5, [1, 2, 5]))
    print(obj.coinChange_optmized(5, [1, 2, 5]))
