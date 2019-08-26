class ListNode:
    def __init__(self,value,next=None):
        self.val=value
        self.next=next
def swap_list_node(head):

    if head and head.next:
        next_node=head.next
        head.next=swap_list_node(next_node.next)
        next_node.next=head
        return next_node
    return head
def print_list_node(head):
    while head:
        print(head.val)
        head=head.next


if __name__ == '__main__':
    list_node=list()

    for i in range(4,0,-1):
        list_node.append(ListNode(i,list_node[-1] if list_node else None))
    list_node=list(reversed(list_node))
    print_list_node(list_node[0])
    list_node=swap_list_node(list_node[0])
    print_list_node(list_node)
