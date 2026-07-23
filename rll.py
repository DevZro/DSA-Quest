# Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    prevNode = None
    currentNode = head
    nextNode = head.next if head != None else None

    while currentNode != None:
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
        nextNode = currentNode.next if currentNode != None else None

    return prevNode