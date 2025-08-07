password=input("Enter your password: ")
n=len(password)

if n<6:
    print("Password is weak")
elif n>=6 and n<10:
    print("Password is moderate")
elif n>10: 
    print("Password is strong")