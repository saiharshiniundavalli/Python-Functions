# count=len
# l=[1,2,3,4,5,6,7,8,]
# print(count(l))

def run_twice(func,value):
    return func(func(value))
def add(x):
    return x+1
print(run_twice(add,5))