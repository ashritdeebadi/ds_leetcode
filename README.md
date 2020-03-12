"# ds_leetcode" 

Binary Search Trees :

1. If you want to find out distinct structural BST's for n : Hack : Catalan Number Formula or use Dynamic Programming



Dynamic Programming :

1.  If you want to find out distinct structural BST's for n  dfs(start,i-1,memo) and dfs(i+1,end,memo)
2.  Coin change 
    1. If finding all possible sums them sum problem is : dp[c_amount]+=dp[c_amount-coin]
    2. If finding minimum then dp[c_amount]= min(dp[c_amount],dp[c_amount-coin]+1)


Linked list:

1. Add two numbers : head is at right end, use while h1 or h2 or carry 


Two Pointers:

1. Cointainer with most no. of water  hint : while start < end  ; if heights[start] < heights[end]: start +=1 else end-=1

2. Sort colors hint: use three pointers 0_boundary to keep track of right most boundary of 0's 2_boundary to keep track of left boundary of 2 , increment curr in 0 case and else case 