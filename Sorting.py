'''
GROUP:-A PRACTICAL NO..2
PROBLEM STATEMENT:--> In a company, Employee salaries
 are stored in a list as floating-point numbers. Write a python program that sorts the employee salaries in ascending order using the following two algorithms: 
Selection Sort: Sort the salaries using the selection sort algorithm.
Bubble sort: Sort the salaries using the bubble sort algorithm.
After sorting the salaries, the program should display the top five highest salaries in the company.
-----------------------------------------------------------------------------------------
Name:- Deore Om Yashwant
Roll No.:- 29
Batch:- SEA-2
'''
def menu():
    print("==============menu==============")
    print("1.bubble sort")
    print("2.selection sort")
    print("3.Exit")

def bubble_sort(salary):
    
    n = len(salary)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(salary[j] > salary[j+1]):
                    salary[j],salary[j+1] = salary[j+1],salary[j]
    print("Sorted List :",salary)
    print("Top 5 Salaries :",salary[-1:-6:-1])
  
def selection_sort(salary):
  
    n = len(salary)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(salary[i] > salary[j]):
                    temp = salary[i]
                    salary[i] = salary[j]
                    salary[j] = temp
    print("Sorted Salary :", salary)
    

def salary_input():
    size = int(input("Enter number of Employees :"))
    salary = [ ]
    print("Enter salary in Decimal :")
    for i in range (0,size):
        salary.append(float(input()))
    print("Unsorted salary :",salary)
    return salary,size
  
    
while True:
    menu()
    choice = int(input("Enter your choice :"))

    if (choice == 1):
        print("bubble sort")
        salary,size=salary_input()
        sort=bubble_sort(salary)
        print(sort)
    if (choice == 2):
        print("selection sort")
        salary,size=salary_input()
        sort=selection_sort(salary)
        print(sort)
    if (choice == 3):
        print("<<<<Exit>>>>")
        break


'''
-----------------OUTPUT-----------------
==============menu==============
1.bubble sort
2.selection sort
3.Exit
Enter your choice :1
bubble sort
Enter number of Employees :7
Enter salary in Decimal :
123
45
23242
68690
565.67
34345
3434.56
Unsorted salary : [123.0, 45.0, 23242.0, 68690.0, 565.67, 34345.0, 3434.56]
Sorted List : [45.0, 123.0, 565.67, 3434.56, 23242.0, 34345.0, 68690.0]
Top 5 Salaries : [68690.0, 34345.0, 23242.0, 3434.56, 565.67]
==============menu==============
1.bubble sort
2.selection sort
3.Exit
Enter your choice :2 
selection sort
Enter number of Employees :7   
Enter salary in Decimal :
123
34
676
45455.45
4545.56
56
38934
Unsorted salary : [123.0, 34.0, 676.0, 45455.45, 4545.56, 56.0, 38934.0]
Sorted Salary : [34.0, 56.0, 123.0, 676.0, 4545.56, 38934.0, 45455.45]
==============menu==============
1.bubble sort
2.selection sort
3.Exit
Enter your choice :3   
<<<<Exit>>>>
'''