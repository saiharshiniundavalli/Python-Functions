# 1.	Write a generator that yields numbers from 1 to N.

# def fun(x):
#     for i in range(1,x+1):
#         yield i
# gen=fun(25)
# for j in gen:
#     print(j)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Write a generator that yields numbers from 1 to N.

# def fun(n):
#     for i in range(1,n+1):
#         if (i%2==0):
#             yield i
# gen=fun(25)
# for j in gen:
#     print(j)

# 3.	Write a generator that yields each character of a string.

# def fun(x):
#     for i in x:
#         yield i
# st=fun("Harshini")
# for i in st:
#     print(i)

# 4.	Write a generator that yields characters of a string in reverse order.

# def fun(x):
#     a=len(x)-1
#     for i in range(a,-1,-1):
#         yield x[i]
# st=fun("Harshini")
# for i in st:
#     print(i)

# 5.	Write a generator that yields only vowels from a string

# def fun(x):
#     a=len(x)
#     for i in range(0,a):
#         if x[i] in "AEIOUaeiou":
#             yield x[i]
# st=fun("Mokshajna")
# for i in st:
#     print(i)

# 6.	Write a generator that yields only digits present in a string.

# def fun(x):
#     a=len(x)
#     for i in range(0,a):
        # if x[i].isdigit():  or if x[i] in "0123456789":
#             yield x[i]
# st=fun("Mokshajna1234@345")
# for i in st:
#     print(i)

# 7.	Write a generator that yields the square of each element in a list.

# def fun(x):
#     for i in (x):
#         yield i*i
# l=fun([1,3,5,7,9])
# for i in l:
#     print(i)

# 8.	Write a generator that yields digits from an integer one by one.

# def fun(x):
#     for i in str(x):
#         yield int(i)
# l=fun(12345678)
# for i in l:
#     print(i)

# 9.	Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6

def fun(x):
    total=0
    for i in x:
        total=total+i
        yield total

l=fun([1,2,3])
for i in l:
    print(i)