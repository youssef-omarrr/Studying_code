# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        sorted_list = ListNode()
        current = sorted_list # pointer to the current node
        
        while list1 and list2:
        # append to the sorted list the smaller of the 2
            if list1.val > list2.val:
                current.next = list2 
                list2 = list2.next # iterate through the list we took the node from
            else:
                current.next = list1
                list1 = list1.next
            
            # go to the next node to fill its values (val and next)
            current = current.next
        
        # last nodes are the nodes left in the list that is not empty
        current.next = list1 if list1 else list2
        
        return sorted_list.next # as the first value is always init as zero
        
    
# too lazy to convert the lists into ListNode instances
# if __name__ == "__main__":
#     ans = Solution()
    
#     questions = [([1,2,4],[1,3,4])]
    
#     for q in questions:
#         print(f"'{q}' -> {ans.mergeTwoLists(*q)}")