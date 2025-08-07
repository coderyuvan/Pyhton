chai="Masala chai"
print(chai)
# 0 to 6 index tk string slice ho # jaegi
# 0 is included and 6 is excluded
sliced_str=chai[0:6]
print(sliced_str)



numList="0123456789"
numListSlice=numList[2:5]
print(numListSlice)

# 2 is included 
numlis=numList[2:]
print(numlis)

# 5 is excluded
numlis2=numList[:5]
print(numlis2)

# third paramter will skip number and print only ith number 
numlis3=numList[0:10:2]
print(numlis3)

# same output as numlist3
numlis4=numList[::2]
print(numlis4)

# reverse the string
numlis5=numList[::-1]
print(numlis5)

#- means last se number dega
numlis6=numList[-2]
print(numlis6)



newChai="ginger, mint, herbal, masala"
ls=newChai.split(", ")  # split the string into list of words()
print(ls)


job_type="SDE"
company="ZS ASSOCIATES"
package="15 LPA"

post= "Yuvan is placed at {} with package of {} and his jobe role is {} "
print(post.format(company,package,job_type))


# list to string
list_of_words=["Yuvan","is","placed","at","ZS ASSOCIATES","with package of 15 LPA","and his jobe role is SDE"]
sentence=" ".join(list_of_words)
print(sentence)