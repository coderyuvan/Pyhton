# input age from user
age=int(input("Enter your age: "))

if age<13:
    print("You are a child.")
elif age>=13 and age<20:
    print("You are a teenager.")
elif age>=20 and age<59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# This code categorizes a person based on their age into child, teenager, adult, or