class ListNode:
    def __init__(self,value,next=None):
        self.val=value
        self.next=next

def print_list(list_node):
    while list_node:
        print(list_node.val)
        list_node=list_node.next
def reverse_list(list_node):
    pre=list_node
    cur=list_node.next
    pre.next=None
    while cur:
        temp=cur.next
        cur.next=pre
        pre=cur
        cur=temp
    return pre

if __name__ == '__main__':
    li=list()
    for i in range(4,0,-1):
        li.append(ListNode(i,li[-1] if li else None))
    li=list(reversed(li))
    print_list(li[0])
    list_node=reverse_list(li[0])
    print_list(list_node)