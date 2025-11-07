'''Design and implement a hash table of fixed size. Use the division method for the hash function and resolve collisions using linear probing. Allow the user to perform the following operations: 
• Insert a key 
• Search for a key 
• Delete a key 
• Display the table
-----------------------------------------------------------------------------------------
Name:- Deore Om Yashwant
Roll No.:- 29
Batch:- SEA-2
'''
class LinearProbingHash:
	def __init__(self,size = 10):
		self.size = size
		self.table = [None]*size
		self.Deleted = "<DELETED>"
		
	def hash_function(self,key):
	    return key % self.size
	    
	def display(self):
	    print("Hash Table")
	    for i,key in enumerate (self.table):
	        print(f"Index {i} : {key}")
	        
	def insertion(self,key):
	    index = self.hash_function(key)
	    original_index = index
	    while self.table[index] not in (None,self.Deleted):
	        if self.table[index]==key:
	            print(f"Key {key} is already exists at index {index}.")
	            return
	        index = (index+1)% self.size
	        if index == original_index:
	            print("Hash Table is Full. Cannot Inssert .")
	            return
	    self.table[index] = key
	    print(f"Inserted Key {key} at index {index}.")
	def search(self,key):
	    index = self.hash_function(key)
	    original_index = index
	    while self.table[index] is not None:
	        if self.table[index]==key:
	            print(f"Key {key} is Found at index {index}.")
	            return index
	        index = (index+1)% self.size
	        if index == original_index:
	            break
	    print(f"Key {key} is Not Found!!")
	    return None
	def delete(self,key):
	    index = self.search(key)
	    if index is not None:
	        self.table[index] = self.Deleted
	        print(f"Key {key} is Deleted from index {index}")
	def menudrive(self):
	    gescoe@gescoe-OptiPlex-3020:~/Downloads$ python3 hash.py
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 1
Enter the Element you want to Insert:- 11
Inserted Key 11 at index 1.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 1
Enter the Element you want to Insert:- 22
Inserted Key 22 at index 2.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 1
Enter the Element you want to Insert:- 333
Inserted Key 333 at index 3.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 4
Hash Table
Index 0 : None
Index 1 : 11
Index 2 : 22
Index 3 : 333
Index 4 : None
Index 5 : None
Index 6 : None
Index 7 : None
Index 8 : None
Index 9 : None
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 2
Enter the Element you want to Search:- 1
Key 1 is Not Found!!
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 2
Enter the Element you want to Search:- 11
Key 11 is Found at index 1.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 3
Enter the Element you want to Delete:- 22
Key 22 is Found at index 2.
Key 22 is Deleted from index 2
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 5
EXITING>>>>!!!
while True:
	        print("##########MENU###########")
	        print("1. Insert a key") 
	        print("2. Search for a key ")
	        print("3. Delete a key") 
	        print("4. Display the table")
	        print("5. EXIT!!!")
	        choice = int(input("Enter your choice:- "))
	        if choice==1:
	            key = int(input("Enter the Element you want to Insert:- "))
	            self.insertion(key)
	        elif choice==2:
	            key = int(input("Enter the Element you want to Search:- "))
	            self.search(key)
	        elif choice==3:
	            key = int(input("Enter the Element you want to Delete:- "))
	            self.delete(key)
	        elif choice==4:
	            self.display()
	        elif choice==5:
	            print("EXITING>>>>!!!")
	            break
obj=LinearProbingHash()
obj.menudrive()

'''
gescoe@gescoe-OptiPlex-3020:~/Downloads$ python3 hash.py
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 1
Enter the Element you want to Insert:- 11
Inserted Key 11 at index 1.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 1
Enter the Element you want to Insert:- 22
Inserted Key 22 at index 2.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 1
Enter the Element you want to Insert:- 333
Inserted Key 333 at index 3.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 4
Hash Table
Index 0 : None
Index 1 : 11
Index 2 : 22
Index 3 : 333
Index 4 : None
Index 5 : None
Index 6 : None
Index 7 : None
Index 8 : None
Index 9 : None
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 2
Enter the Element you want to Search:- 1
Key 1 is Not Found!!
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 2
Enter the Element you want to Search:- 11
Key 11 is Found at index 1.
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 3
Enter the Element you want to Delete:- 22
Key 22 is Found at index 2.
Key 22 is Deleted from index 2
##########MENU###########
1. Insert a key
2. Search for a key 
3. Delete a key
4. Display the table
5. EXIT!!!
Enter your choice:- 5
EXITING>>>>!!!
'''
