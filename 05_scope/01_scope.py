# x=100

# def func1():
#     x=10
#     def func2():
#          print(x)

#     return func2
# res=func1()
# res()  




def func1(x):
    def func2(y):
        return x**y
    return func2

rest=func1(2)(3) # This will calculate 2 raised to the power of 3
print(rest)  # Output: 8
res=func1(3)
print(res(4))  # This will calculate 3 raised to the power of 4

