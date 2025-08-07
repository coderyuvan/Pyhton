str=input("enter the string to be reversed : ")
strr=list(str)
n=len(str)
i=0
j=n-1

while i<j:
    swap=strr[i]
    strr[i]=strr[j]
    strr[j]=swap
    i+=1
    j-=1
rev="".join(strr)
print("Reversed string is:", rev)