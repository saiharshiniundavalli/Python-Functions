# def multiply_all(*args):
#     a=1
#     for i in args:
#         a=a*i
#     return a
# print(multiply_all(1,2,3,4,5))

# def display_tags(**kwargs):
#     print(kwargs)
# display_tags(name="Harshini",age=21,city="Razole",brach="cse")

# def describe_person(name,*hobbies):
#     print(f"My name is {name}")
#     print(f"My hobbies are {hobbies}")
# describe_person("Harshini","watching movies","listening music")

# def f(*args):
#     print(type(args))
# f(4,5,6)

def mixed(a,b,*args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)
mixed(1,2,3,4,5,x=12)