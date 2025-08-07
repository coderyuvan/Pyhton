myList={
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
}

print(myList)

print(myList["courses"])

myList["age"] = 31
print(myList["age"])

print(myList)


for name in myList:
    print(name, ":", myList[name])


if "age" is not  30:
    print("Age is present in the dictionary.")
else:
    print("Age is not present in the dictionary.")

myList.pop("courses")
print(myList)