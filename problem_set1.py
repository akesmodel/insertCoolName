def main():
   blue() 
   blastoff()
   candy_shop()
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
    list.sort
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
    return(1.25*len(all_candies))
    print((1.25*len(all_candies)))


    
    
    print(list[2])
    add = input("Where else would you like to vacation? ")
    list.append(add)
    print(len(list))
    list.remove(list[0])
    print(len(list))


if __name__=="__main__":
    main()