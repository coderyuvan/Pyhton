fruit=input("enter the name of fruit : ")
color=input("enter the color : ")

if color=='green':
    sol= "{} is unripe"
    print(sol.format(fruit))
elif color=='yellow':
    sol= "{} is ripe"
    print(sol.format(fruit))
elif color=='brown':
    sol= "{} is overripe"
    print(sol.format(fruit))