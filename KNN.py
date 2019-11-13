import numpy as np
from math import sqrt
class_a = np.array([[1,2],[2,3],[4,5]])
class_b = np.array([[78,90],[90,67],[77,88]])
print("Enter the data points")
c = int(input())
d = int(input())
dist = 0
list_a = []
list_b = []
for i in range(0,len(class_a)):
    j=0
    a = sqrt((class_a[i,j]-c)**2 + (class_a[i,j+1]-d)**2)
    list_a.append(a)
    b = sqrt((class_b[i,j]-c)**2 + (class_b[i,j+1]-d)**2)
    list_b.append(b)
print(list_a)
print(list_b)
list_c = list_a
list_c.extend(list_b)
list_c.sort()
print(list_c)
print("Enter the value of k")
k = int(input())
a1 = 0
b1 = 0
for m in range(0,k-1):
    for n in range(0,len(list_a)-1):
        if(list_a[n] == list_c[m]):
            a1 = a1 + 1
    for p in range(0,len(list_b)-1):
        if(list_b[p] == list_c[m]):
            b1 = b1 + 1

if(a1>b1):
    print("The point belongs to Cluster1")
elif(b1>a1):
    print("The point belongs to Cluster2")
