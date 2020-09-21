a = [1,2,3,4,5,6,7,8,9,10,20,"Banana"]
b = [11,12,13,14,15,16,17,18,19,20]
for i in a:
    if i != 20:
       continue
    print(i)
for i in range(1,20,2):
    print(i)
else:
    print("you Won");
a = [1,2,3,4,5,6,7,8,9,10,20,"Banana"]
b = [11,12,13,14,15,16,17,18,19,20]
for x in a:
    for y in b:
        print(y,x)
