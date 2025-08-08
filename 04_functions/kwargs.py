def print_kwarsgs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_kwarsgs(name="yuvan")
print_kwarsgs(name="yuvan",power="nalla")
print_kwarsgs(name="yuvan",power="nalla",placement="unplaced")