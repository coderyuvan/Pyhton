def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
for num in even_generator(8):
    print(num)

# yeild memory m function ko rkhta and also state ko bhi rkhta h ki itna kaam ho chuka hai and aap is state p ho