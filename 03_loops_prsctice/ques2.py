n=int(input("enter the number : "))
sum=0

for i in range(0,n):
    if i%2==0:
        sum+=i

print("sum of even numbers upto",n ,"is : ",sum)