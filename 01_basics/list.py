# case1 : both variables refer to the same list  object && change in one variable reflects in the other
# list is mutable
print("This is first case printing")
l1=[1,2,3,4]
l2=l1
print(l1)
l1[0]=100
print(l2)


# case2 : both variables refer to the differnt list object && change in one variable do not reflects in the other
print("This is second case printing")
p1=[7,8,9]
p2=p1
p2=[7,8,9]
p1[0]=1000
print(p1)
print(p2)


#case 3: jb slicing kri h to aapne ek copy bnaya h and usko refer kra h
print("This is third case printing")
k1=[1,2,3,4]
k2=k1[:]
k2[0]=1000
print(k1)
print(k2)