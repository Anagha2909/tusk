"""
1.Create a function and add this 
2.Try using list indexing 

"""
fcart=0
vcart=0
chcart=0
icart=0
fruits =['apple', 'banana', 'mango']
vegetables =["tomato","carrot","onion"]
chocolates =["five star",'chocobar','milkybar']
icecream =['vanilla','strawberry','kulfi']
x=int(input('Enter what you choice'))
if (x==0):
    print(fruits)
    n=int(input("enter which fruit you want"))
    m=int(input("Enter the quantity"))
    if(n==0):
        print(fruits[0]) #this is called indexing and try changing it for a print statements
        fcart=m*100
    elif(n==1):
        print("banana")
        facrt=m*60
    elif(n==2):
        print("mango")
        fcart=m*200
    else:
        print("error")
        fcart=0
elif(x==1):
    print(vegetables)
    n=int(input("eneter the vegetable you want"))
    m=int(input("enter the quantity"))
    if(n==0):
        print("tomato")
        vcart=m*40
    elif(n==1):
        print("carrot")
        vcart=m*50
    elif(n==2):
        print("onion")
        vcart=m*90
    else:
        print("error")
        vcart=0
elif(x==2):
    print(chocolates)
    n=int(input("Enter the chocolate you want"))
    m=int(input("enter the quantity you want"))
    if(n==0):
        print("five stars")
        chcart=m*10
    elif(n==1):
        print("chocobar")
        chcart=m*15
    elif(n==2):
        print("milkybar")
        chcart=m*12
    else:
        print("error")
        chcart=0
elif(x==3):
    print(icecream)
    n=int(input("enter which ice cream you want"))
    m=int(input("enter the quantity of ice cream you want"))
    if(n==0):
        print("Vanilla")
        icart=m*100
    elif(n==1):
        print("strawberry")
        icart=m*110
    elif(n==2):
        print("kulfill")
        icart=m*115
    else:
        print("error")
        icart=0
else:
    print("error")

bill=fcart+vcart+chcart+icart
print("Total amount is : ")
print(bill)
