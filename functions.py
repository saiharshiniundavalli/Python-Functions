# #def details():
#     name=input("Enter Your Name:")
#     age=int(input("Enter Your Age:"))
#     native=input("Enter Your Native Place:")
#     course=input("Enter Your Course:")
#     print(f"Name:{name}\n Age:{age}\n Native:{native}\n Course:{course}")
# while True:
#     op=int(input("Enter '1' to continue and '2' to exit"))
#     if op==1:
#         details()
#     else:
#         break

# create a function called tree with parameters monkey-count, fruit-type,fruit-count. this function should
# calculate the time taken by total monkey's to completely eat the fruits and print the details

# def tree(monkey_count,fruit_type,fruit_count):
#     monkey_count=int(input("Enter Number of Monkeys:"))
#     fruit_type=input("Enter Fruit Type:")
#     fruit_count=int(input("Enter Number of Fruits:"))
#     d={"mango":2,"apple":3,"orange":1.5}
#     t=d[fruit_type.lower()]
#     time_taken=int(fruit_count/monkey_cou`nt)*t
#     print(time_taken)
# tree(   5,"mango",10)

#Function Examples section:1
#1. def say_hello():
#     print("Welcome to Python!")
# say_hello()

#2 def add(a,b):
#     sum=a+b
#     print(sum)
# add(10,15)

#4 def area_of_rectangle(length,width):
#     print(length*width)
# area_of_rectangle(6,4)

#Function Examples section:2
#1 def multiply(a,b,c):
#     print(a*b*c)
# multiply(2,3,4)

#2 def describe_pet(animal,name):
#     print(f"My {animal} is named {name}")
# describe_pet("dog","lokey")

# def power(base,exponent):
#     print(base**exponent)
# power(2,3)

#5 def full_name(first,middle,last):
#     print(f"My name is {first} {middle} {last}")
# full_name("Undavalli","Sai","Harshini")

#Function Examples section:3
#1 def intro(name,city,hobby):
#     print(f"hi!,I am {name},i'm from {city} and my hobbies are {hobby}")
# intro("Harshini","Razole","Music")

#2 def subtract(a,b):
#     return(a-b)
# print(subtract(3,10))
# print(subtract(10,3))

#4 def bio(first_name,last_name,age):
#     print(f"{first_name} {last_name} {age}")
# bio("Harshini","Undavalli",20)

#Function Examples section:4
#1 def send_email(to, subject, body):
#     print(f"{to}\n {subject}\n {body}\n")
# send_email(body="Please find the report attached.",to="alice@example.com",subject="Monthly Report")

#2 def create_profile(username,email,age):
#     print(f"My usename is {username} , email id is {email} and my age is {age}")
# create_profile(age=21,username="Meghana",email="kalepumeghana@gmail.com")

#3 def greet(name,age):
#     print(name,age)
# greet("Meghana",21)
# #greet(name="Meghana",21)//error

#4 def book_ticket(name,city,destination,ticket):
#     print(f"My name is {name} from {city} to reach {destination} i want {ticket} tickets")
# book_ticket(city="srikakulam",ticket=2,destination="hyderabad",name="meghana")

#Function Examples section:5
#1 def power(base,exponent=2):
#     return base**exponent
# print(power(5))
# print(power(5,3))

#2 def connect(host,port=3306,protocol='TCP'):
#     print(f"{host} {port} {protocol}")
# connect("localhost")
# connect("localhost",3350)
# connect("localhost",3790,"HCL")

#4 def discount_price(price,discount=10):
#     print(price-(price*discount/100))
# discount_price(100)

#Function Examples section:6
# 1 def multiply_all(*args):
#     product = 1
#     for num in args:
#         product *= num
#     return product
# print(multiply_all(2, 3, 4))  # 24

# 2 def display_tags(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
# display_tags(name="Sai", age=20, city="Hyderabad")

# 3 def describe_person(name, *hobbies):
#     print("Name:", name)
#     print("Hobbies:", hobbies)
# describe_person("Sai", "Reading", "Coding", "Music")








