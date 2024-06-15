

def bubble_sort(a):
    for x in range(len(a)-1,0,-1):  
        for j in range(x):
              if a[j]>a[j+1]:
                  a[j],a[j+1] = a[j+1],a[j]



list1 = [6,3,1,5,9,8]
bubble_sort(list1)
print(list1)

list2 = [2,3,5,39,11,8,9,166,45,23]
bubble_sort(list2)
print(list2)

list3 = [1,2,3,4,5,6,7,8,9,10]
bubble_sort(list3)
print(list3)

list4 = [10,9,8,7,6,5,4,3,2,1]
bubble_sort(list4)
print(list4)

list5 = [4]
bubble_sort(list5)
print(list5)





class Node:
    def __init__(self,value):
        self.info = value 
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root == None
           
    def insert(self,x):
        self.root = self._insert(self.root, x)
                 
    def _insert(self,p, x):
        if p is None:
            p = Node(x)
        elif x < p.info :
            p.lchild = self._insert(p.lchild, x) 
        else:
            p.rchild = self._insert(p.rchild, x)   
        return p

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None :
            return
        self._inorder(p.lchild)
        print(p.info, " ")
        self._inorder(p.rchild) 

    
n = int(input("Enter the number of elements to be sorted : "))

tree = BinarySearchTree()          
for i in range(n):
    x = int(input("Enter element : "))
    tree.insert(x)
    
tree.inorder()  
