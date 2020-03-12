class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def addNumbers(self, l1, l2):
        """
        Given two linked list in reverse order  add the numbers and return it in the form of a linked list

        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.

        """

        """
        Approach :
        1) create a answer node (-1) and carry =0
        2)while l1 or l2 or carry 
        3) if l1 then add l1 value to carry , if l2 add l2 value to carry 
        4) create next node and assign value carry % 10
        5) carry = carry  by 10 

        return answer.next

        Time Complexity : O(n)  where n is the length of longest linled list
        Space Complexity : O(n) where n is the final answer length

        """

        ans = new_node = ListNode(-1)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            ans.next = ListNode(carry % 10)
            ans = ans.next
            carry = carry // 10

        return new_node.next


if __name__ == "__main__":

    n1 = ListNode(7)
    n1.next = ListNode(8)
    n1.next.next = ListNode(9)

    h1 = n1

    n2 = ListNode(3)
    n2.next = ListNode(5)
    n2.next.next = ListNode(9)

    h2 = n2

    obj = Solution()

    ans = obj.addNumbers(h1, h2)

    while ans:
        print(ans.val)
        ans = ans.next
