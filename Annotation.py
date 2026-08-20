def adding(x:str,y:str) -> str:
    return x+y

# list, tuple, str, dict, int, float, bool

print(adding("asd","asd"))
print(adding.__annotations__)

def add(x,y):
    return x+y
print(add.__name__)
print(add)

a = add
print(add(10,20))
print(a(10,20))