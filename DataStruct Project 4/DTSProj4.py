# Dom Scordino
# CSC145B
# March 25, 2022
# Assignment 4

# Start of Code

#Creates binary search tree with a certain array of numbers.
#Prints out the preorder, inorder, and post order of BST.
#Deletion of three seperate numbers and after deleting each one,
# will print out preorder, inorder, and postorder of BST.

#Create class Binary Search Tree
class DTSBinaryTree:
    #define init method
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
#Pseudo code
#create class DTSBinaryTree
        #define init method
        #set left to None
        #set right to None
        #set val to val

#define insert method
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = DTSBinaryTree(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = DTSBinaryTree(val)
#Pseudo Code
    #define insert method
        #if value is not existing
            #set value to itself
            #return
        #if value equals value
            #return the value
        #if value is less than value
                #insert left value
                #return
            #set left to Node Class Value
                #return
        #if right exists
            #insert right value
            #return
        #set right to Node Class Value

#define get minimum method
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val
#Pseudo Code
    #define get min methods
        #set current to self
        #while current left is not 0
            #set current to current.left
        #return currrent data value

#Define get maximum method
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
#Pseudo Code
    #Define get max methods
        #set current to self
        #whlle current right is not 0
            #set current to current right
        #return current value

#define delete method
    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
#Pseudo Code
    #define delete method
        #if self is equal to 0:
            #return self
        #if value is less than current
            #if self left:
                #set self left to delete its value
            #return self
        #if value is greater then current value
            #if self right
                #set right to delete its value
            #return self
        #if self right is equal to 0:
            #return self left
        #if self left os equal to 0:
            #return self right
        #set minimum larger node to self right
        #create while loop that runs while minimum larger node is left:
            #set minimum larger node to left
        #set self value to minimum larger node value
        #set self right to self right delete minimum larger node value
        #return self

#define exists method
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)
#Pseudo Code
    #define exists method
        #if value equals self value
            #return True
        #if value is less then self value
            #return False
        #return self right exists value

#define preorder method
    #Preorder traverses from root, to left subtree, to right subtree
    def preorder(self, values):
        if self.val is not None:
            values.append(self.val)
        if self.left is not None:
            self.left.preorder(values)
        if self.right is not None:
            self.right.preorder(values)
        return values
#Pseudo Code
    #define preorder method
        #if self value is not 0:
            #append the value
        #if self left is not 0:
            #run self left preorder value
        #if self right is not 0:
            #run self right preorder value
        #return value

#define inorder method
    #Inorder traverses from left subtree, to root, to right subtree
    def inorder(self, values):
        if self.left is not None:
            self.left.inorder(values)
        if self.val is not None:
            values.append(self.val)
        if self.right is not None:
            self.right.inorder(values)
        return values
#Pseudo Code
    #define inorder method
        #if self left is not 0:
            #run self left inorder value
        #if self value is not 0:
            #append value
        #if self right is not 0:
            #run self right inorder value
        #return value

#define postorder method
    #Postrder traverses from left subtree, to right subtree, to right subtree
    def postorder(self, values):
        if self.left is not None:
            self.left.postorder(values)
        if self.right is not None:
            self.right.postorder(values)
        if self.val is not None:
            values.append(self.val)
        return values
#Pseudo Code
    #define postorder method
        #if self left is not 0:
            #run self left postorder value
        #if self right is not 0:
            #run self right postorder value
        #if self value is not 0:
            #append value
        #return value

#define main
def main():
    #insert array of numbers in order given
    array = [100, 50, 150, 25, 45, 125, 175, 20, 30, 40, 47, 120, 135, 160, 180]
    
    #Set DTSBinaryTree to bst
    bst = DTSBinaryTree()
    for num in array:
        bst.insert(num)
    
    #print preorder of bst with original numbers
    print("BST - Print Preorder - original numbers:")
    print(bst.preorder([]))
    print(f'\n')
    
    #print postorder of bst with original numbers
    print("BST - Print Postorder - original numbers:")
    print(bst.postorder([]))
    print(f'\n')
    
    #print inorder of bst with original numbers
    print("BST - Print Inorder - original numbers:")
    print(bst.inorder([]))
    print(f'\n')
    
    #set number to delete bst number 100
    array = [100]
    print("Deleting number: " + str(100))
    for num in array:
        bst.delete(100)
    print(f'\n')

    #Prints postorder, preorder, and inorder of bst after deleting node 100
    print("Print All 3 orders without 100") 
    print(f'\n')
    print("Double checking code if 100 still exists...")
    print(f'\n')
    
    #prints whether or not 100 exists in bst    
    print("Existence of 100?: ")
    print(bst.exists(100))
    print(f'\n')
    
    print("BST - Print Preorder - no 100")
    print(bst.preorder([]))
    print(f'\n')
    
    print("BST - Print Postorder - no 100")        
    print(bst.postorder([]))
    print(f'\n')
    
    print("BST - Print Inorder - no 100")        
    print(bst.inorder([]))

    #deletes node 125
    array = [125]
    print("Deleting number: " + str(125))
    for num in array:
        bst.delete(125)
    print(f'\n')

    #prints postorder, preorder, and inorder of numbers after deleting 125
    print("Print All 3 orders without 100 or 125")
    print(f'\n')
    print("Double checking code if 125 still exists...")
    print(f'\n')
    
    #prints whether or not 125 exists in bst
    print("Existence of 125?: ")
    print(bst.exists(125))
    print(f'\n')
    
    print("BST - Print Preorder - no 100 or 125")
    print(bst.preorder([]))
    print(f'\n')
    
    print("BST - Print Postorder - no 100 or 125")        
    print(bst.postorder([]))
    print(f'\n')
    
    print("BST - Print Inorder - no 100 or 125")        
    print(bst.inorder([]))
    
    #deletes node 30
    array = [30]
    print("Deleting the number:" + str(30))
    for num in array:
        bst.delete(30)
    print(f'\n')
    
    #prints postorder, preorder, and inorder of numbers after deleting 30
    print("Print All 3 orders without 100 or 125 or 30")
    print(f'\n')
    print("Double checking code if 30 still exists...")
    print(f'\n')
    
    #prints whether or not 125 exists in bst
    print("Existence of 30?: ")
    print(bst.exists(30))
    print(f'\n')
    
    print("BST - Print Preorder - no 100 or 125 or 30")
    print(bst.preorder([]))
    print(f'\n')
    
    print("BST - Print Postorder - no 100 or 125 or 30")        
    print(bst.postorder([]))
    print(f'\n')
    
    print("BST - Print Inorder - no 100 or 125 or 30")        
    print(bst.inorder([]))
        
#calls main function to run
main()

#End of Code