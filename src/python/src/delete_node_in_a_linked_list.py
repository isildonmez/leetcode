# https://leetcode.com/problems/delete-node-in-a-linked-list/?envType=problem-list-v2&envId=a6ezkna5&difficulty=MEDIUM%2CHARD


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
