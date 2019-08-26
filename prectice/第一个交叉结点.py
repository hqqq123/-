from django.test import TestCase

# Create your tests here.
class Node(object):
    def __init__(self,val,next=None):
        self.value=val
        self.next=next
def get_length(head):
    length=0
    while head:
        length+=1
        head=head.next
    return length

def get_first_node(head1,head2):
    len1=get_length(head1)
    len2=get_length(head2)
    cur1=head1
    cur2=head2
    if len1>len2:
        while len1-len2>0:
            cur1=cur1.next
            len1-=1
    elif len1<len2:
        while len2-len1>0:
            cur2=cur2.next
            len2-=1
    else:
        pass
    while cur1 and cur2:
        if cur1.value==cur2.value:
            print(cur1.value)
            return cur1.value
        cur1=cur1.next
        cur2=cur2.next
    print('没有')
if __name__ == '__main__':
    a = Node('a1', Node('a2', Node('c1', Node('c2', Node('c3')))))  # 构造不带头结点的链表：a1→a2→c1→c2→c3
    b = Node('b1', Node('b2', Node('b3', Node('c1', Node('c2', Node('c3'))))))  # 构造不带头结点的链表：b1→b2→b3→c1→c2→c3

    get_first_node(a,b)