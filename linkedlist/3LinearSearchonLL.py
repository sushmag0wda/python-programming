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
        count=0
        while mover:
            print(mover.data,"--->",end=" ")
            mover=mover.next
            count+=1
        return count
    def countlen(self,head):
        mover=head
        count=0
        while mover!=None:
            count+=1
            mover=mover.next
        return count
    def linearsearch(self,head,tar):
        if head==None:
            return False
        pos=0
        mover=head
        while mover:
            pos+=1
            if mover.data==tar:
                return True,pos
            else:
                mover=mover.next
        return False


l1=Linkedlist()
arr=l1.cratearr()
head=l1.convert(arr)
c=l1.traversal(head)
co=l1.countlen(head)

print("total nodes are:",c)
print("len of ll=",co)
tar=int(input("enter the target element"))
flag,pos=l1.linearsearch(head,tar)
if flag:
    print("the target is found in node:",pos)
else:
    print("target is not found")