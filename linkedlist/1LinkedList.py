class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def cratearr(self):
        l1=[]
        while True:
            try:
                n=int(input("enter a number"))
                l1.append(n)
            except Exception as e:
                return l1
    def convert(self,arr):
        firstnode=Node(arr[0])
        head=firstnode
        mover=head
        for i in range(1,len(arr)):
            temp=Node(arr[i])
            mover.next=temp
            mover=temp
        return head
    def traversal(self,head):
        mover=head
        while mover:
            print(mover.data,"--->",end=" ")
            mover=mover.next
l1=Linkedlist()
arr=l1.cratearr()
head=l1.convert(arr)
l1.traversal(head)

