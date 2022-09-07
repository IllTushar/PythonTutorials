# a = "Hello"
# b = "World"
# print(a+b)
w = "Tushar Gupta"
print(w[-1::-1])
print(w[0::2])
print(w[0:4:1])

#Stirng Iterantion
n = len(w)
print(n)#include space
## Print String
for i in range(n):
    print(w[i])
#Print Reverse String
print("")
for i in range(n-1,-1,-1):
    print(w[i])

#Reverse string without range
print("")
w = w[-1::-1]
for i in w:
    print(w[i])