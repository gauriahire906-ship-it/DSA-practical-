''' Group B-Assignment No 4
STATEMENT:Create a Student Record Management System using linked list

• Use a singly/doubly linked list to store student data (Roll No, Name, Marks).
• Perform operations: Add, Delete, Update, Search, and Sort.
• Display records in ascending/descending order based on marks or roll number.

 NAME:Prachi Vinod Balak
 ROLL NO:14
class StudentNode:
    def __init__(self,roll_no,name,marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None
        
class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self,roll_no,name,marks):
        new_node = StudentNode(name,roll_no,marks)
        if self.head is None:
           self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("Student Record is added.")

    def delete_student(self,roll_no):
        current = self.head
        prev = None
        while current:
            if current.roll_no == roll_no:
               if prev:
                  prev.next = current.next
               else:
                  self.head = current.next
               print("Student Record deleted.")
               return
            prev = current
            current = current.next
        print("Student not found.")
        
    def update_student(self,roll_no,new_name,new_marks):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.name == new_name
                current.marks == new_marks
                print("Student Record updated.")
                return
            current = current.next
        print("Student not found.")
        
    def search_student(self,roll_no):
        current = self.head
        while current:
            if current.roll_no==roll_no:
                print(f"Found: Roll No:{current.roll_no}, Name:{current.name}, Marks:{current.marks}")
                return
            current = current.next
        print("Student not found.")
    
    def display_students(self, sort_by="roll_no", ascending=True):
        students = []
        current = self.head
        while current:
              students.append((current.roll_no, current.name, current.marks))
              current = current.next
    
        if sort_by == "roll_no":
                students.sort(key=lambda x: x[0], reverse=not ascending)
        elif sort_by == "marks":
                students.sort(key=lambda x: x[2], reverse=not ascending)
    
        if not students:
                print(" No records to display.")
                return
                
        print("\n Students Records")
        for s in students:
        	print(f"Roll No:{s[0]},Name: {s[1]},Marks: {s[2]}")
        
def menu():
        system = StudentLinkedList()
        while True:
            print("\n----Student Record Management Menu----")
            print("1.Add student")
            print("2.Delete student")
            print("3.Update student")
            print("4.Search student")
            print("5.Display All students")
            print("6.Exit.")
            
            choice=int(input("Enter Your Choice(1-6): "))
            
            if choice==1:
               roll_no=int(input("Enter the Roll No: "))
               name=input("Enter the Name: ")
               marks=int(input("Enter the Marks: "))
               system.add_student(roll_no,name,marks)
            elif choice==2:
                roll_no=int(input("Enter the Roll No to Delete: "))
                system.delete_student(roll_no)
            elif choice==3:
               roll_no=int(input("Enter Roll No to Update: "))
               name=input("Enter New Name: ")
               marks=int(input("Enter New Marks: "))
               system.update_student(roll_no,name,marks)
            elif choice==4:
                roll_no=int(input("Enter Roll No to Search: "))
                system.search_student(roll_no)
            elif choice==5:
                sort_key = input("Sort by 'roll_no' or 'marks': ").strip()
                order = input("Order 'asc' or 'desc': ").strip()
                ascending = True if order == 'asc' else False    
                system.display_students(sort_by=sort_key,ascending=ascending)
            elif choice==6:
                print("Exit.")
                break
            else:
                print("Invalid Choice.Try Again.")
                
                
menu()
    
    
Output:        
 ----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 1
Enter the Roll No: 02
Enter the Name: Sanskruti
Enter the Marks: 90
Student Record is added.

----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 1
Enter the Roll No: 30
Enter the Name: Manjiri
Enter the Marks: 99
Student Record is added.

----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 1
Enter the Roll No: 23
Enter the Name: shruti
Enter the Marks: 98
Student Record is added.

----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 5
Sort by 'roll_no' or 'marks': roll_no
Order 'asc' or 'desc': asc

 Students Records
Roll No:Manjiri,Name: 30,Marks: 99
Roll No:Sanskruti,Name: 2,Marks: 90
Roll No:shruti,Name: 23,Marks: 98

----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 3
Enter Roll No to Update: 23
Enter New Name: Prachi
Enter New Marks: 89
Student not found.

----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 2
Enter the Roll No to Delete: 23
Student not found.

----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 4
Enter Roll No to Search: 02
Student not found.

----Student Record Management Menu----
1.Add student
2.Delete student
3.Update student
4.Search student
5.Display All students
6.Exit.
Enter Your Choice(1-6): 6
Exit.
           
''' 
            
            
            
            
            
