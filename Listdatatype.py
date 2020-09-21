a = ["indore",["rajwada","2",3],["delhi",["raipur",1]]]
print(a[0][1])
print(a[1][2])
print(a[1:2])
print(a[1:])
print(a[1][0:1])
a = [2,3,4,5,6]
a[0]=1
print(a)
a[1:3]=[1,1,1]
print(a)
a.append(7)
print(a)
a.extend([8,9,10])
print(a)
print(a+[11,12])
print(a)
print([a]*3)
a.insert(3,9)
print(a)
a = [2,5,9,10,11]
a[2:]=[3,4,5]
print(a)
a = [1,2,3,4,5,6,7,8,3,0]
print(a.index(8))
print(a.count(1))
a.sort()
print(a)
a.reverse()
print(a)
a = [4 ** x for x in range(11)]
print(a)
