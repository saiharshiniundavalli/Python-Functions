#1 k=lambda a:a**3
# print(k(2))

#2 k=lambda a,b:a if a>b else b
# print(k(5,7))

#3 k=lambda n:'even' if n%2==0 else 'odd'
# print(k(10))

#4 l=[(1,'banana'),(2,'apple'),(3,'cherry')]
# l.sort(key=lambda l:l[1])
# print(l)

#MAP
# without lambda
# numbers=[1,2,3,4,5]
# def double(x):
#     return x*2
# result=list(map(double,numbers))
# print(result)

# with lambda
# k=list(map(lambda x:x*2,numbers))
# print(k)