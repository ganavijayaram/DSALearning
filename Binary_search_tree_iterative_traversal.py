class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = 0

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, data):
        if(self.root == None):
            self.root = Node(data)
            self.display_inorder_iterative()
            return
        curr = self.root
        while(curr):
            prev = curr
            if(data < curr.data):
                curr = curr.left
                left = 1
            else:
                curr = curr.right
                left = 0
        if(left == 1):
            prev.left = Node(data)
        else:
            prev.right = Node(data)
        self.display_inorder_iterative()

    def display_preorder_iterative(self):
        print("Iteratice Pre-Order Traversal")
        stack = [None]
        curr = self.root
        while(curr != None and len(stack) != 0):
            if(curr.visited == 0):
                print("{0}-->".format(curr.data), end = "")
                curr.visited = 1
                stack.append(curr)
            if(curr.left != None and curr.left.visited == 0):
                curr = curr.left
            elif(curr.right != None and curr.right.visited == 0):
                curr = curr.right
            else:
                curr = stack.pop()
        

    def display_postorder_iterative(self):
        print("Iterative Post-Order Traversal")
        stack = [None]
        curr = self.root
        while(curr != None or len(stack) != 0):
            while(curr.left != None and curr.left.visited == 0):
                stack.append(curr)
                curr = curr.left
            if(curr.right != None and curr.right.visited == 0):
                stack.append(curr)
                curr = curr.right
            else:
                print("{0}-->".format(curr.data), end = "")
                curr.visited = 1
                curr = stack.pop()
        print()

    def initialising_visit(self):
        print("Iterative In-Order Traversal")
        curr = self.root
        stack = []
        #using one loop
        while True:
            if(curr != None):
                stack.append(curr)
                curr = curr.left
            elif(len(stack)):
                curr = stack.pop()
                #print("{0}-->".format(curr.data), end = "")
                curr.visited = 0
                curr = curr.right
            else:
                break
        print()
        
    def display_inorder_iterative(self):
        print("Iterative In-Order Traversal")
        curr = self.root
        stack = []
        #using one loop
        while True:
            if(curr != None):
                stack.append(curr)
                curr = curr.left
            elif(len(stack)):
                curr = stack.pop()
                print("{0}-->".format(curr.data), end = "")
                curr = curr.right
            else:
                break
        print()
                
        #using two loops
        '''
        stack = [None]
        while(len(stack) != 0 or curr):
            #print("length of stack ", len(stack))
            while True:
                stack.append(curr)
                #print("Appending curr ", curr.data)
                if(curr.left == None):
                    break
                curr = curr.left
            curr = stack.pop()
            #print("curr = ", curr.data)
            print("{0}-->".format(curr.data), end = "")
            while(curr and curr.right == None):
                curr = stack.pop()
                if(curr != None):
                    print("{0}-->".format(curr.data), end = "")
            if(curr and curr.right != None):
                curr = curr.right
        '''
            
        

obj = Binary_Search_Tree()
obj.insert_iterative(16)
obj.insert_iterative(10)
obj.insert_iterative(21)
obj.insert_iterative(23)
obj.insert_iterative(18)
obj.insert_iterative(15)
obj.insert_iterative(7)
obj.insert_iterative(27)
obj.insert_iterative(13)
obj.insert_iterative(14)
obj.insert_iterative(25)
obj.insert_iterative(17)
obj.insert_iterative(8)
obj.display_inorder_iterative()
obj.display_postorder_iterative()
obj.initialising_visit()
obj.display_preorder_iterative()

