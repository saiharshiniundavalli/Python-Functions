#Shallow copy
m=[1,2,3,[4,5]]
l=m.copy()
m[3].append(25)
print(m)
print(l)

#Deep Copy
from copy import deepcopy
m=[1,2,3,[4,5]]
l=deepcopy(m)
m[3].append(25)
print(m)
print(l)
