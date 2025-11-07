''' Group D- Assignment No 3
STATEMENT:Implement various operations on a Binary Search Tree, such as insertion, deletion, display,
and search.

Name:Prachi Vinod Balak
Roll no:14

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print(f"Key {key} already exists in the BST.")
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")
def menu():
    bst = BST()
    root = None
    
    while True:
        print("\n=======Menu:=======")
        print("1. Insert keys")
        print("2. Search key")
        print("3. Delete key")
        print("4. Inorder traversal")
        print("5. Preorder traversal")
        print("6. postorder traversal")
        print("7. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            keys = input("Enter keys to insert (space separated): ").split()
            for key in keys:
                root = bst.insert(root, int(key))
            print(f"Inserted keys {', '.join(keys)} into the BST.")
        
        elif choice == '2':
            key = int(input("Enter key to search: "))
            result = bst.search(root, key)
            if result:
                print(f"Key {key} found in BST.")
            else:
                print(f"Key {key} not found in BST.")
        
        elif choice == '3':
            key = int(input("Enter key to delete: "))
            root = bst.delete(root, key)
            print(f"Deleted {key} from the BST if it existed.")
        
        elif choice == '4':
            print("Inorder traversal of the BST:")
            bst.inorder(root)
            print()
        
        elif choice == '5':
            print("Preorder traversal of the BST:")
            bst.preorder(root)
            print()
            
        elif choice == '6':
            print("Postorder traversal of the BST:")
            bst.postorder(root)
            print()
        
        elif choice == '7':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
 bst=BST()
 bst=menu()
 
 Output:
 =======Menu:=======
1. Insert keys
2. Search key
3. Delete key
4. Inorder traversal
5. Preorder traversal
6. postorder traversal
7. Exit
Enter your choice (1-6): 1
Enter keys to insert (space separated): 12 43 54 65 6 87 98 40 20
Inserted keys 12, 43, 54, 65, 6, 87, 98, 40, 20 into the BST.

=======Menu:=======
1. Insert keys
2. Search key
3. Delete key
4. Inorder traversal
5. Preorder traversal
6. postorder traversal
7. Exit
Enter your choice (1-6): 2
Enter key to search: 6
Key 6 found in BST.

=======Menu:=======
1. Insert keys
2. Search key
3. Delete key
4. Inorder traversal
5. Preorder traversal
6. postorder traversal
7. Exit
Enter your choice (1-6): 3
Enter key to delete: 6
Deleted 6 from the BST if it existed.

=======Menu:=======
1. Insert keys
2. Search key
3. Delete key
4. Inorder traversal
5. Preorder traversal
6. postorder traversal
7. Exit
Enter your choice (1-6): 4
Inorder traversal of the BST:
12 20 40 43 54 65 87 98 

=======Menu:=======
1. Insert keys
2. Search key
3. Delete key
4. Inorder traversal
5. Preorder traversal
6. postorder traversal
7. Exit
Enter your choice (1-6): 5
Preorder traversal of the BST:
12 43 40 20 54 65 87 98 

=======Menu:=======
1. Insert keys
2. Search key
3. Delete key
4. Inorder traversal
5. Preorder traversal
6. postorder traversal
7. Exit
Enter your choice (1-6): 6
Postorder traversal of the BST:
20 40 98 87 65 54 43 12 

=======Menu:=======
1. Insert keys
2. Search key
3. Delete key
4. Inorder traversal
5. Preorder traversal
6. postorder traversal
7. Exit
Enter your choice (1-6): 7
Exiting program.

 '''
 

