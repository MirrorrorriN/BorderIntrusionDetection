class Node():
    def __init__(self,value,p):
        self.data=value
        self.next=p
class Linkedlist():
    def __init__(self):
        self.head=0
    def append(self,data):
        if head==0


def test(L1,L2):
    L=Linkedlist()
    hl=0
    p=L1.head
    q=L1.head
    s=""
    while(L1.head!=0)or(L2.head!=0):
        if(L1.head==0):
            hl.next=Node((q.data+flag)%10)
            hl=hl.next
            flag=(q.data+flag)/10
            q=q.next
        if(L2.head==0):
            h1.next=Node((p.data+flag)%10)
            h1=h1.next
            flag=(p.data+flag)/10
            p=p.next
        else:
            hl.next=Node((p.data+q.data+flag)%10)
            hl=hl.next
            p=p.next
            q=q.next
            flag=(p.data+q.data+flag)/10
    t=L.head
    while (t.next!=0):
        s=s+str(t.data)
        t=t.next
        s=s+"->"
    s=s+str(t.data)
    return s
if __name__=="__main__":
    L1=
    test()
