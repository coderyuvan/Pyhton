age=int(input("enter your age :"))
day=input("Enter the day :")

if(day== 'wednesday'):
    if age>=18:
        print('As today is wednesday and ur adult so u will get discount and Price of ticket for u is $10')
    else :
         print('As today is wednesday and ur child so u will get discount and Price of ticket for u is $6')
else :
    if age>=18:
        print('As today is not wednesday and ur adult so Price of ticket for u is $12')
    else :
         print('As today is not wednesday and ur child so  Price of ticket for u is $8')          

