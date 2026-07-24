# Merge 2 Sorted Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 == None and list2 == None:
        return None

    res = ListNode()
    head = res

    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            res.val =  list1.val
            list1 = list1.next
        else:
            res.val = list2.val
            list2 = list2.next
        temp = ListNode()
        res.next = temp
        res = res.next
        
    while list1 != None:
        res.val =  list1.val
        list1 = list1.next
        if list1 == None:
            break
        temp = ListNode()
        res.next = temp
        res = res.next

    while list2 != None:
        res.val =  list2.val
        list2 = list2.next
        if list2 == None:
            break
        temp = ListNode()
        res.next = temp
        res = res.next

    return head