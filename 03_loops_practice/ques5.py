n=int(input("Enter a number: "))

if(n==0):
    print("Factorial of 0 is 1")

fact=1
i=1
while i<=n:
    fact = fact * i
    i+= 1

    
print("Factorial of", n, "is", fact)