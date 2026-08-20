# class A:
#     def __init__(self,start,end):
#         self.start=start
#         self.end=end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start<=self.end:
#             self.start+=1
#             return self.start-1
#         else:
#             raise StopIteration
# a1=A(1,3)
# k=iter(a1)
# print(k,a1,sep='\n')
# for i in a1:
#     print(i)
from operator import index


# class list_iter:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             i=self.index
#             self.index+=1
#             return self.l[i]
#         else:
#             raise StopIteration
# l=list_iter([1,2,4,909,78,53,65])
# for i in l:
#     print(i)

# class Even:
#     def __init__(self, l):
#         self.l = l
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index < len(self.l):
#             i = self.index
#             self.index += 1
#             if self.l[i] % 2 == 0:
#                 return self.l[i]
#         raise StopIteration
# l = Even([1, 2, 4, 909, 78, 53, 65])
# for i in l:
#     print(i)

# class Vowels:
#     def __init__(self,s):
#         self.s=s
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index < len(self.s):
#             index = self.index
#             self.index += 1
#             if self.s[index] in "aeiou":
#                 return self.s[index]
#         raise StopIteration
# v1=Vowels("Just Kidding")
# it=iter(v1)
# print(next(it))

# 1.	Create an custom iterator that prints numbers from 1 to N, where N is given by the user.

# class number:
#     def __init__(self,n):
#         self.n=n
#         self.total=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.total<=self.n:
#             a=self.total
#             self.total+=1
#             return a
#         raise StopIteration
# x=number(30)
# # for i in x:
# #     print(i)
# print(next(x))
# print(next(x))
# print(next(x))

# 2.	Create an custom iterator that prints numbers from N to 1.

# class number:
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>=1:
#             a=self.n
#             self.n-=1
#             return a
#         raise StopIteration
# x=number(30)
# for i in x:
#     print(i)

# 3.	Create an custom iterator that prints the first N even numbers.
# class number:
#     def __init__(self,n):
#         self.n=n
#         self.count=0
#         self.num=2
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>self.count:
#             a=self.num
#             self.num+=2
#             self.count+=1
#             return a
#         raise StopIteration
# x=number(30)
# for i in x:
#     print(i)

# 4.	Create an custom iterator that prints the first N odd numbers.
# class number:
#     def __init__(self,n):
#         self.n=n
#         self.count=0
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>self.count:
#             a=self.num
#             self.num+=2
#             self.count+=1
#             return a
#         raise StopIteration
# x=number(30)
# for i in x:
#   print(i)