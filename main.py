class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def deleteDuplicates(self, head):
        #Initialize the current node as the head of the linked list
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next
        

list_nodes = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
solution = Solution()
new_list = solution.deleteDuplicates(list_nodes)

print_linked_list(new_list)

