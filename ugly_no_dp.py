class Solution:

    def uglyNo(self, n):

        ugly_list = [0]*n

        ugly_list[0] = 1

        i2, i3, i5 = 0, 0, 0

        i2n = 2
        i3n = 3
        i5n = 5

        for i in range(1, n):
            ugly_list[i] = min(i2n, i3n, i5n)

            if ugly_list[i] == i2n:
                i2 += 1
                i2n = 2 * ugly_list[i2]

            if ugly_list[i] == i3n:
                i3 += 1
                i3n = 3 * ugly_list[i3]

            if ugly_list[i] == i5n:
                i5 += 1
                i5n = 5 * ugly_list[i5]

            print(ugly_list, i2, i2n, i3, i3n, i5, i5n)
        return ugly_list[-1]


obj = Solution()

print(obj.uglyNo(10))
