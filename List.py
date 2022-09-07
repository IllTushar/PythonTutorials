l = [10,5.6,'w']
l[2] = 11  ##List is Mutable..
print(l[2],type(l[2]))
#Neseted Lis
l = [1,2,[3,4]]
print(l[2][1])
#list slicing
l = [2,3,"Hello",[3,4,5]]
# print(l[2])
print(l[0:2])
print(l[1:])
l = [1,2,3,4,5,6]
print(l[0::2])
print(l[-1::-1])
print(l[-1::-2])
#using len keyword
n = len(l)
for i in range(n):
    print(l[i])

#without using len keyword
print("")
w = [1,2,3,4,5]
# w =w[-1::-1]
for p in w:
    print(w[p])