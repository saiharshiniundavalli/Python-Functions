def validation(func):
    def inner(*args):
        # print(args)
        # l = []
        # for i in args:
        #     if isinstance(i,int):
        #         l.append(i)
        # l = tuple(l)

        l = tuple(filter(lambda x: isinstance(x,int),args))
        return func(*l)

    return inner

@validation
def just(*args):
    print(f"args: {args}")
    return sum(args)

# print(just(1,2,3,'66',[45],123,'78'))

def password_validator(func):
    def inner(psd:str):
        sp = ['@','*','!','#','$','%','&','_','-','=','+','/']
        if len(psd)>=8:
            up = list(filter(lambda x: x.isupper(),psd))
            sc = list(filter(lambda x:x in sp, psd))
            dg = list(filter(lambda x: x.isdigit(),psd))

            print(up,sc,dg,sep='\n')

            if up and sc and dg:
                print("Strong Password")
                func(psd)
            else:
                print("Weak Password")
        else:
            print("password must contain 8 characters")
    return inner

@password_validator
def password(ps):
    print(f"password {ps} is accepted")


password("23456fghbnkH")
password("765FHGDk#$")