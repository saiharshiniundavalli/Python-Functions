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

#def fun(name='guest',age):
#  print(name,age)
#fun(guest,25)
def fun(age,name='Harshini'):
    print(name,age)
fun(21,"Harshini")

#4 def discount_price(price,discount=10):
#     print(price-(price*discount/100))
# discount_price(100)