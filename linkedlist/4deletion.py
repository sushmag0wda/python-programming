#deletion in LL:
'''
1.head
    10-->40-->50-->50-->
    curr head==>10
    delete(curr_head)
    new_head==>20
2.tail
    10-->40-->60-->50-->
    curr tail==>50
    delete(curr_tail)
    new_tail==>60
3.element
    1-->2-->3-->4-->
    ele=3
    1-->2-->4
4.pos
    1-->2-->3-->4-->5-->
    pos=4
    1-->2-->3-->5-->
'''
class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def createarray(self):
        l1=[]
        while True:
            try:
                n=int(input("enter a number"))
                l1.append(n)
            except Exception as e:
                return l1


    def convert(self,arr):
        if arr==[]:
            return None
        newnode=Node(arr[0])
        head=newnode
        mover=head
        for i in range(1,len(arr)):
            temp=Node(arr[i])
            mover.next=temp
            mover=temp
        return head
    def traversal(self,head):
        mover=head
        while mover:
            print(mover.data,"-->",end=" ")
            mover=mover.next

    def deletehead(self,head):
        if head==None:
            return None
        if head.next==None:
            return None
    
        mover=head
        head=mover.next
        return head
    def delattail(self,head):
        if head==None:
            return None
        if head.next==None:
            return None
        mover=head
        while mover:
            if mover.next.next==None:
                mover.next=None
            mover=mover.next
        return head
    def deleteatpos(self,head,pos):
        if head==None:
            return None
        if head.next==None:
            if pos==1:
                return None
            else:
                return None
        mover=head
        count=0
        prev=None
        while mover:
            count+=1
            if count==pos:
                prev.next=mover.next
                break
            prev=mover
            mover=mover.next
        return head
    
    def deleteele(self,head,ele):
        if head==None:
            return None
        if head.next==None:
            if head.data==ele:
                return None
            else:
                return None
        mover=head
        count=0
        prev=None
        while mover:
            count+=1
            if mover.data==ele:
                prev.next=mover.next
                break
            prev=mover
            mover=mover.next
        return head

        

    
    
l1=linkedlist()
arr=l1.createarray()
head=l1.convert(arr)
print("original linked list")
l1.traversal(head)

head=l1.deletehead(head)
print("\nlinked list after deleting the head node")
l1.traversal(head)

head=l1.delattail(head)
print("\nlinked list after deleting the tail node")
l1.traversal(head)


pos=int(input("enter the position val"))
print("\nlinked list after deleting the pos")
head=l1.deleteatpos(head,pos)
l1.traversal(head)

ele=int(input("enter the element"))
print("\nlinked list after deleting the element")
head=l1.deleteatpos(head,ele)
l1.traversal(head)
