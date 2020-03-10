class Solution:

    def uniqueBST(self, n):
        """
        input: n   -> number of continuous elements 

        return  : number of structural binary search Trees

        Example : n=3

        return  : 5           refer : https://leetcode.com/problems/unique-binary-search-trees/

        """

        """
        The solution is a catalen number, it can be calculated by either using catalen number formula (refer : readme ) or using Dynamic Programming

        G(0)=G(1)=1

        G(n) = Sum i to n   G(i-1) * G(n-i)   is the intution
        F(i,n) = G(i-1)*G(n-i)

        G(3) = F(1,3) + F(2,3) + F(3,3)
             = G(0)*G(2) +G(1)*G(1) + G(2)*G(0)
             = G(0)*(F(1,2)+F(2,2)) + G(1)*G(1) + (F(1,2)+F(2,2)) *G(0)
             = G(0) * ((G(0)*G(1)) + G(1)*G(0))  +  G(1)*G(1) +  ((G(0)*G(1)) + G(1)*G(0)) * G(0) )
             = 1    *  (  (1*1)    +   (1*1)  )  +    (1*1)   +   (  (1*1)    +    (1*1) )  *  1 )
             = 1 *2         +    1      + 2*1
             = 5


        Time Complexity  : O(n*2) worst case
        Space Complexity : O(n)
         
        """

        C = [0]*(n+1)

        C[0] = C[1] = 1

        for center in range(2, n+1):
            for i in range(1, center+1):
                C[center] += C[i-1]*C[center-i]

        return C[-1]

    def uniqueBST_catalen(self, n):
        """
        Catalan Formula :      C(n+1) = (2 * C (n) * (2n+1) ) / n+2

        Time Complexity :      O(n)
        Space Complexity:      O(1)

        """

        C = 1

        for i in range(n):
            C = (2*C*(i*2 + 1)) / (i+2)
        return int(C)


if __name__ == "__main__":

    obj = Solution()

    print(obj.uniqueBST(3))
    print(obj.uniqueBST(4))

    print(obj.uniqueBST_catalen(3))
    print(obj.uniqueBST_catalen(4))
