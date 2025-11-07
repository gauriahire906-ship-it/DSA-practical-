'''GROUP:C        Asssignment no: 1
Name:  sakshi sharad burkul Roll No:24

PROBLEM STATEMENT : Implement a hash table of size 10 and use the division method as a hash function. In case of a collision, use chaining. Implement the following operations:
• Insert(key): Insert key-value pairs into the hash table.
• Search(key): Search for the value associated with a given key.
• Delete(key): Delete a key-value pair from the hash table
'''

class HashTable:
   def __init__(self,size = 10):
      self.size = size
      self.table = [[] for _ in range(size)]
      
   def hash_function(self,key):
      return key % self.size
      
   def insert(self,key):
      index = self.hash_function(key)
      if key not in self.table[index]:
         self.table[index].append(key)
         
   def search (self,key):
      index = self.hash_function(key)
      return key in self.table[index]
      
   def delete (self,key):
      index = self.hash_function(key)
      if key in self.table[index]:
         self.table[index].remove(key)
         return True
      return False
      
   def display(self):
      for i ,bucket in enumerate(self.table):
         print(f"Index{i}: {bucket}")
         
if __name__ == "__main__":
  h1 = HashTable()       
  while True:
     print("===Menu===")
     print("1.Insert")
     print("2.Search")
     print("3.Delete")
     print("4.Display")
     print("5.Exit")
     choice = int(input("Enter the choice :"))
     if choice == 1:
       key = int(input("Enter key to be insert : "))
       h1.insert(key)
       
     elif choice == 2:
       key = int(input("Enter key to be search : "))
       res = h1.search(key)
       if res:  
          print(f"Key {key} found ")
       else:
          print(f"Key {key} not found")
     elif choice==3:
       key = int(input("Enter key to be deleted : "))
       res = h1.delete(key)
       if res:  
          print(f"Key {key} deleted")
       else:
          print(f"Key {key}not found")
     elif choice == 4:
       h1.display()
     elif choice == 5:
       print("Exit")
       break
     else:
       print("Enter a valid choice.")
       
'''
OUTPUT
gescoe@gescoe-OptiPlex-3020:~/Desktop/SE-A15$ python3 Chaining.py 
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :1 
Enter key to be insert : 12
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :1
Enter key to be insert : 43
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :1
Enter key to be insert : 56
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :1
Enter key to be insert : 87
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :39
Enter a valid choice.
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :2
Enter key to be search : 87
Key 87 found 
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :3
Enter key to be deleted : 56
Key 56 deleted
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :4
Index0: []
Index1: []
Index2: [12]
Index3: [43]
Index4: []
Index5: []
Index6: []
Index7: [87]
Index8: []
Index9: []
===Menu===
1.Insert
2.Search
3.Delete
4.Display
5.Exit
Enter the choice :5
Exit
'''
