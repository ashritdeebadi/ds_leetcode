

class BinaryTree:
    def binary_search_recursive(self, arr, target, left, right):
        if left > right:
            # input : sorted arr [1,2,3,5,6,8,10] , target =8 , left =0 , right = 7
            # return  index if present (5) else -1

            mid = left+(right-left) // 2
            print("The number at {} : {} ".format(mid, arr[mid]))

            if arr[mid] == target:  # if target found
                return mid

            if target > arr[mid]:  # element present in right
                return self.binary_search_recursive(arr, target, mid, right)
            else:  # element present in left
                return self.binary_search_recursive(arr, target, left, mid-1)
        else:
            return -1

    def binary_search_iter(self, arr, target):
        left = 0
        right = len(arr)

        while left < right:
            mid = left+(right-left)//2

            if target == arr[mid]:
                return mid

            if target > arr[mid]:
                left = mid
            else:
                right = mid-1

        return -1


arr = [1, 2, 3, 5, 6, 8, 10]

ans = BinaryTree()
print(ans.binary_search_recursive(arr, 0, 0, len(arr)))

print(ans.binary_search_iter(arr, 10))
