# a=10000**10000
# print(a)  #Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

# ____________________str___________________
# class Emp:
#     def __init__(self,n,sal,e):
#         self.name=n
#         self.salary=sal
#         self.exp=e
#     def __str__(self):
#         return f"Name:{self.name}"
# e1=Emp("Harshini",500000,2)
# print(e1)  #Name:Harshini

# class Theater:
#     def __init__(self,m,t):
#         self.movie=m
#         self.tickets=t
#         self.tickets_booked=0
#     def book_ticket(self,n):
#         if n<=self.tickets-self.tickets_booked:
#             self.tickets_booked+=n
#             print(f"{n} ticket(s) booked successfully.")
#         else:
#             print("Not enough tickets available.")
#     def __str__(self):
#         return f"Movie: {self.movie}\nTotal Tickets: {self.tickets}\nTickets Booked: {self.tickets_booked}\nTickets Available: {self.tickets-self.tickets_booked}"
# t1=Theater("Coolie",100)
# print(t1)
# t1.book_ticket(25)
# print("\nAfter Booking:")
# print(t1)

# _______________________repr_______________________________
# class Inventory:
#     def __init__(self):
#         self.items=[]
#     def __add__(self,items:list):
#         self.items.extend(items)
#     def __str__(self):
#         return f"items:{self.items}\n Total:{len(self.items)}"
#     def __repr__(self):
#         return f"{len(self.items)}"
# i1=Inventory()
# i2=Inventory()
# i3=Inventory()
# i1.__add__(["milk","cake"])
# i2.__add__(["Stand","Thumpsup","Rice"])
# i3.__add__(["Rice","Dry Fruits","Diet Coke","Fruits"])
# print(i1)

# class Student:
#     def __init__(self, name, sec, m, p, c):
#         self.name = name
#         self.section = sec
#         self.maths = m
#         self.physics = p
#         self.chemistry = c
#     def total_marks(self):
#         return self.maths + self.physics + self.chemistry
#     @staticmethod
#     def grade(k):
#         if k > 290:
#             return 'A'
#         elif k >= 280:
#             return 'B'
#         elif k >= 270:
#             return 'C'
#         elif k >= 260:
#             return 'D'
#         elif k >= 250:
#             return 'E'
#         else:
#             return 'F'
#     def __str__(self):
#         return f"Name: {self.name} Total: {self.total_marks()} Grade: {self.grade(self.total_marks())}"
#     def __repr__(self):
#         return f"{self.name}: {self.grade(self.total_marks())}"
# s1 = Student("Sai", "A", 98, 97, 99)
# print(s1)
# print(repr(s1))

# class Bank:
#     def __init__(self,name,acc,pin):
#         self.name=name
#         self.account=acc
#         self.pin=pin
#         self.balance=0
#     def valid_pin(self):
#         p=int(input("enter your pin:"))
#         return p==self.pin
#     def deposit(self):
#         m=int(input("Enter deposit money:"))
#         if m>=0:
#             self.balance +=m
#         else:
#             print("Invalid Money")
#     def withdraw(self):
#         if self.valid_pin():
#             m=int(input("Enter the withdraw money:"))
#             if 0<=m<=self.balance:
#                 print("Withdraw Successfully")
#                 self.balance -=m
#             else:
#                 print("Invalid/Insufficient Money")
#         else:
#             print("Wrong Pin")
#     def change_pin(self):
#         if self.valid_pin():
#             p=int(input("Enter new pin:"))
#             self.pin==p
#             print("Pin changed Successfully")
#         else:
#             print("Wrong Pin")
#     def __str__(self):
#         if self.valid_pin():
#             return f"Name:{self.name}\n Account No:{self.account}\n Balance:{self.balance}"
#         else:
#             return "Wrong Pin"
#     def __repr__(self):
#         return self.name
# b = Bank("Sai", 1234567890, 1234)
#
# b.deposit()
# b.withdraw()
# b.change_pin()
# print(b)
# print(repr(b))

#____________________________add,sub___________________

class Bank():
    def __init__(self,acc,pin):
        self.accno=acc
        self.pin=pin
        self.bal=0
    def valid_pin(self):
        p=int(input("Enter your pin:"))
        return p==self.pin
    def __add__(self, other):
        if other>=0:
            self.bal+=other
            return "Deposited Successfully"
        else:
            return "Invalid Money"
    def __sub__(self, other):
        if self.valid_pin():
            if 0<=other<=self.bal:
                self.bal-=other
                return "Withdraw Successfully"
            else:
                return "Insufficient Money"
        else:
            return "Invalid Pin"
b1=Bank(17889,1234)
b1+5000
b1-2000

# ___________________________hash_____________________
# class Student:
#     def __init__(self,i,n,m):
#         self.Id=i
#         self.name=n
#         self.marks=m
#     def __gt__(self, other):
#         return self.marks>other.marks
#     def __lt__(self, other):
#         return self.marks<other.marks
#     def __eq__(self, other):
#         return self.marks==other.marks
#     def __hash__(self):
#         return hash(self.Id)
    
