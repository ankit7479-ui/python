# Detect if a linked list has a cycle.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def has_cycle(self, head):  
        if not head:
            return False
        
        slow = head
        fast = head.next if head.next else None
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node2
print(node1.has_cycle(node1)) 
            