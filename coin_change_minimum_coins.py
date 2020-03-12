class Solution:

    def minCoins(self, coins, amount):
        """
        Given an infinite supply of coins , find the min no. of coins required to form that amount

        Input: coins = [1, 2, 5], amount = 11
        Output: 3 
        Explanation: 11 = 5 + 5 + 1

        """

        """
        We can solve this using Dynamic Programming

        1) Declare a dp table of size = len(amount)+1
        2) Assign temp highest value , say amount+1
        3) Let dp[0] be equal to 0 , Initialization
        4) For ever c_amount ,for every coin in coins, check if coin value is less than or equal to c_amount
        5) If yes then let that value be stored as temp i,e  temp_amount= c_amount-coin
        6) if this value is less than dp[c_amount] and if dp[temp_amount] +1 is less than dp[c_amount]
            dp[c_amount]= dp[temp_amount]+1

        Time complexity :   O(n*m) n is no. of coins , m is amount
        Space complexity : O(m)

        """

        dp = [amount+9999 for i in range(amount+1)]
        dp[0] = 0

        for c_amount in range(1, amount+1):
            for coin in coins:
                if c_amount-coin >= 0:
                    temp_amount = c_amount-coin

                    if dp[temp_amount] != dp[c_amount] and dp[temp_amount]+1 < dp[c_amount]:
                        dp[c_amount] = dp[temp_amount]+1

        return dp[-1]


if __name__ == "__main__":

    obj = Solution()

    print(obj.minCoins([1, 2, 5], 11))
