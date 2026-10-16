def main():
   blue() 
   blastoff()
   candy_shop()
   fruit_pricing()
def blue():
    red=3
    purple=red*12
    print(purple)
def blastoff():
    count= int(input("Pick a number to count down from! "))
    for i in range(count):
        print(count-i)
    print("Blastoff!")
def candy_shop():
    list = ["Heath Bar", "Sour Patch Watermelon", "Lindor"]
    list.append("Kitkat")
    list.insert(1, "Reese's Cups")
    list.sort()
    list.remove("Kitkat")
    print(list)
    user_candies=[]
    candy1=input("What is your favorite candy? ")
    candy2=input("What is your second favorite candy? ")
    candy3=input("What is your third favorite candy? ")
    all_candies=list
    all_candies.append(candy1)
    all_candies.append(candy2)
    all_candies.append(candy3)
    print(len(all_candies))
    for i in range(len(all_candies)):
        print(all_candies[i])
    print((1.25*len(all_candies)))
    return(1.25*len(all_candies))


    
    
    print(list[2])
    add = input("Where else would you like to vacation? ")
    list.append(add)
    print(len(list))
    list.remove(list[0])
    print(len(list))

def fruit_pricing():
    groceries ={
        "apple": 0.75,
        "banana": 1.25,
        "orange": 0.80,
        "peach": 2.25,
        "coconut": 2.80,
    }
    groceries["pear"]=1.15
    print(groceries)
    print("The price of a peach is: $" + str(groceries.get("peach")))
    cart=groceries.keys()
    count=len(cart)
    print(cart)
    sum=0.00
    for key in groceries:
        if (groceries.get(key))>=1.25:
            print(key)
    print("The total cost of 3 apples, 2 bananas, and 1 coconut is: $" + (str)(3*groceries.get("apple")+2*groceries.get("banana")+groceries.get("coconut")))

    



if __name__=="__main__":
    main()