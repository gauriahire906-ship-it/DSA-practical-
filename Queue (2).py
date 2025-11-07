''' GROUP B-ASSIGNMENT NO 02
STATEMENT:Implement a real-time event processing system using a Queue data structure. The system
should support the following features:
• Add an Event: When a new event occurs, it should be added to the event queue.
• Process the Next Event: The system should process and remove the event that has
been in the queue the longest.
• Display Pending Events: Show all the events currently waiting to be processed.
• Cancel an Event: An event can be canceled if it has not been processed.

NAME: PRACHI VINOD BALAK 
ROLL NO :14


from collections import deque;
class Q_deque:
    def __init__(self):
        self.q = deque()
    def add_event(self,event):
        self.q.append(event)
        print(f"Event '{event}' added")
    def process_event(self):
        if self.q:
            event = self.q.popleft()
            print(f"Event is processed {event}")
        else :
            print(f"Event {event} is already processed ")
    def cancel_event(self,event):
        if event in self.q:
            self.q.remove(event)
            print(f"Event '{event}' is remove")
            print(self.q)
        else:
            print(f"Event '{event}' is canceled")
    def display(self):
            print(f"Event is display'{self.q}'")
     


    def menu(self):

        while True:
            print("===menu===")
            print("1. added event:")
            print("2. process event:")
            print("3. cancel event:")
            print("4. display event:")
            print("5. Exist:")
            choice = int(input("Enter a number:"))
            if (choice == 1):
                event = input("Enter a event:")
                self.add_event(event)
            elif (choice == 2):
                self.process_event()
            elif (choice == 3):
                event=input("enter event to be delete:-")
                self.cancel_event(event)
            elif (choice == 4):
                self.display()
            elif (choice ==5):
                print("Exit")
                break;

            
obj = Q_deque()
obj.menu()


OUTPUT:
===menu===
1. added event:
2. process event:
3. cancel event:
4. display event:
5. Exist:
Enter a number:1
Enter a event:E1
Event 'E1' added
===menu===
1. added event:
2. process event:
3. cancel event:
4. display event:
5. Exist:
Enter a number:1
Enter a event:E2
Event 'E2' added
===menu===
1. added event:
2. process event:
3. cancel event:
4. display event:
5. Exist:
Enter a number:1
Enter a event:E3
Event 'E3' added
===menu===
1. added event:
2. process event:
3. cancel event:
4. display event:
5. Exist:
Enter a number:2
Event is processed E1
===menu===
1. added event:
2. process event:
3. cancel event:
4. display event:
5. Exist:
Enter a number:4
Event is display'deque(['E2', 'E3'])'
===menu===
1. added event:
2. process event:
3. cancel event:
4. display event:
5. Exist:
Enter a number:3
enter event to be delete:-E1
Event 'E1' is canceled
===menu===
1. added event:
2. process event:
3. cancel event:
4. display event:
5. Exist:
Enter a number:5
Exit
'''



