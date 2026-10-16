def main(): #makes sure everything runs
   blue() 
   blastoff()
   candy_shop()
   fruit_pricing()
def blue():
    red=3
    purple=red*12 #Pretty standard multiplication here. 
    #Nice how we dont have to add a ; or define type since python is magical
    print(purple)
def blastoff():
    count= int(input("Pick a number to count down from! "))
    for i in range(count):
        print(count-i) #Since indexing starts from zero, this loop prints, count (the user's input), then count-1, count-2, etc until 1 (which is count-(count-1))
    print("Blastoff!")
def candy_shop():
    list = ["Heath Bar", "Sour Patch Watermelon", "Lindor"] #Three objectively very good candies
    list.append("Kitkat") #Adding to the end of our list
    list.insert(1, "Reese's Cups") #Inserts Reeses at index 1
    list.sort() #Alphabeticizes list
    list.remove("Kitkat") #buh bye kitkat
    print(list)
    #Adds candies. This works fine, 
    #the more optimal way to do it is a loop 
    #(like if user were to add 10 candies), 
    #but by the time I realized that I was too lazy to change (and it was 11:46 PM)
    candy1=input("What is your favorite candy? ")
    candy2=input("What is your second favorite candy? ")
    candy3=input("What is your third favorite candy? ")
    all_candies=list #adds stuff in list to all candies
   #individually adding each candy
   #(again loop would have been good here)
    all_candies.append(candy1)
    all_candies.append(candy2)
    all_candies.append(candy3)
    print(str(len(all_candies))) # we have to cast because it only prints strings
    for i in range(len(all_candies)):
        print(all_candies[i])
    print((1.25*len(all_candies))) #If each candy is the same, we can do this
    return(1.25*len(all_candies))

def fruit_pricing():
    groceries ={
        "apple": 0.75,
        "banana": 1.25,
        "orange": 0.80,
        "peach": 2.25,
        "coconut": 2.80,
    }
    groceries["pear"]=1.15
    #using the get method to get the price of a peach, casting to string because print needs strings
    print("The price of a peach is: $" + str(groceries.get("peach")))
    cart=groceries.keys()
    count=len(cart)
    print(cart)
    sum=0.00
    for key in groceries: #using a for each loop, since a index loop doesn't work on unordered dictionary
        if (groceries.get(key))>=1.25:
            print(key)
    print("The total cost of 3 apples, 2 bananas, and 1 coconut is: $" + (str)(3*groceries.get("apple")+2*groceries.get("banana")+groceries.get("coconut")))

    



if __name__=="__main__":
    main()