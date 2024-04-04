# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        node_arr = [head]
        while node_arr[-1].next:
            node_arr.append(node_arr[-1].next)
        return node_arr[len(node_arr) // 2]

    def middleNodeSlowFast(self, head):
        mid = double_mid = head
        while double_mid and double_mid.next:
            mid = mid.next
            double_mid = double_mid.next.next
        return mid
