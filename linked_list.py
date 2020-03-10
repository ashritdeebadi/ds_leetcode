import math


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def to_decimal(self, head):
        h = head
        temp = ''
        while h is not None:
            temp += str(h.val)
            h = h.next
        return int(temp, 2)

    def middle(self, head):
        h = head
        l = 0

        while h is not None:
            l += 1
            h = h.next

        if l % 2 == 0:
            m = int(l/2)+1
        else:
            m = int(math.ceil(l/2))
        print(m)
        h = head
        while m != 1:
            h = h.next
            m -= 1
        return h

    def reverse_ll(self, head):

        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == "__main__":

    ll = LinkedList(1)
    head = ll
    ll.next = LinkedList(2)
    ll.next.next = LinkedList(3)
    ll.next.next.next = LinkedList(4)
    ll.next.next.next.next = LinkedList(5)
    ll.next.next.next.next.next = LinkedList(6)

    obj = Solution()

    print(obj.reverse_ll(head).next.val)
