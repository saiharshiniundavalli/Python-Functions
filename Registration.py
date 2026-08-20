def register(func):
    uns = []
    def inner(us,psd,age):
        nonlocal uns
        if us not in uns:
            sp = ['@', '*', '!', '#', '$', '%', '&', '_', '-', '=', '+', '/']
            if len(psd) >= 8:
                up = list(filter(lambda x: x.isupper(), psd))
                sc = list(filter(lambda x: x in sp, psd))
                dg = list(filter(lambda x: x.isdigit(), psd))

                print(up, sc, dg, sep='\n')

                if up and sc and dg:
                    print("Strong Password")
                    if age >= 18:
                        func(us,psd,age)
                        uns.append(us)
                    else:
                        print("Age must be >= 18")
                else:
                    print("Weak Password")
            else:
                print("password must contain 8 characters")
        else:
            print("User name already exists")
    return inner

@register
def registration(us,psd,age):
    print(f"{us}'s Registration Successful")

registration("cherry","CG4576#@$",19)
registration("cherry","CG4576#@$",19)


import functools

def Dec(func):
    @functools.wraps(func)
    def inner(x,y):
        return func(x,y)
    return inner

@Dec
def ann(x:str,y:str) -> list:
    """Just a doc"""
    print(x+y)
    return [x,y]

print(ann.__name__)
print(ann.__doc__)
print(ann.__annotations__)