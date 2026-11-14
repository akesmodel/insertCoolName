import csv

dictionary = {}  #establishes our dictionary, pulling from source csv
with open('grades.csv','r') as f:
    data = csv.reader(f)
    for row in data:
        if row:
            key = row[0] # first column = key
            values = row[1:] # py list splice = values
            values = [float(item) for item in values]

            dictionary[key] = values #assigns the list of values to each corresponding key

def main(): #runs everything
    good=False
    while (good==False): #Keeps the program running, so the user can make as many changes as they need. Once they're done, the loop stops and the program terminates
        print("Hello! Would you like to") 
        print("a) See your averages for each class?")
        print("b) See your grades for a specific class?")
        print("c) See your GPA?")
        print("d) Add a test score for a class?")
        print("e) Remove a grade?")
        choice=input("(a/b/c/d/e) ")
        if (choice=="a"):
            print_all_averages()
            visualize_grades()
        elif (choice=="b"):
            Subject=input("Which subject do you want to see your grades in? ").lower()
            if (Subject in dictionary.keys()):
                print_grades(Subject)
                print_average(Subject)
            else: #user feedback for the main method
                print("Yikes! Sorry, you're going to have to register that class first!") 
        elif (choice=="c"):
            print("Your GPA is: "+get_GPA())
        elif (choice=="d"):
            print("Your current classes are: ")
            classes = ""
            for key in dictionary.keys():
                print(key)
            Subject=input("Which subject do you want to add a grade for? ").lower()
            grade=float(input("What grade did you get on that test? "))
            add_grade(Subject,grade)
            print("Your new average in "+Subject+" is: "+ (str)(get_average(Subject)))
        else:
            Subject= input("What class would you like to remove a grade from? ").lower()
            grade= input("What grade would you like to remove? ")
            remove_grade(Subject,grade)
        keep_going=input("Would you like to do anything else? (y/n) ")
        if keep_going=="n":
            good=True
    with open('grades.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        # iter thru keys AND values in dataset, write to csv
        for key, value in dictionary.items():
            writer.writerow([key] + value)   
    print("Have a great day!")

#NEW METHODS
def remove_grade(Subject, grade):
    if (Subject in dictionary.keys()):
        if (float(grade) in dictionary.get(Subject)): #float grade because it's a string input, and in because the values are lists
            dictionary[Subject].remove(float(grade)) #we use dictionary[Subject] because dictionary.get(Subject) just returns data but doesn't allow us to access it
        else:
            print("I don't think you ever got that grade, sorry!") #user interaction
    else: #user feedback for the main method
        print("Yikes! Sorry, you're going to have to register that class first!") 
def visualize_grades(): 
    for key in dictionary.keys():
        toPrint="X"
        c= float(get_average(key)) #I don't know if this is redundant because get_average is already a float. It was just being annoying if I didn't.
        d= (int)((c-47.5)/5) #I personally chose to round to the nearest 2.5? If you just want to round everthing down though, it would be (c-50) instead.
        #essentially, we're trying to find how many fives past 50 go into c.
        for i in range(d):
            toPrint+="*"
        print(toPrint)
    

#OLD METHODS, all I changed was a bit of extra user interaction
def add_grade(Subject, grade): #If the subject exists, we add that grade to its values, and if not, we create a new key in dictionary corresponding to that subject
    if (Subject not in dictionary.keys()): #weird troubleshoot to see if subject exists or not.
        dictionary[Subject]= [grade] #if if doesnt exist, we initialize its list to contain the single grade value.
        print("Creating class...") #User interaction for this method
    else:
        dictionary[Subject].append(grade)
def get_average(Subject): #A method that returns the average, a helper method I wrote, because print average doesn't save the average. 
#This gets called on a ton in other methods.
    tests=dictionary.get(Subject)
    #num and sum are variables we create to get a total average, where sum is the total sum of each grade, and num is the total number of tests taken
    num=len(tests)
    sum=0
    for i in range(num):
        sum+=(int)(tests[i])
    sum/=num
    return sum
    #I didn't add user interaction, just since it's a helper method.
def print_average(Subject):
    toRet="Your average in " #user interaction.
    toRet+=Subject
    toRet+=" is "
    toRet+=str(get_average(Subject))
    print(toRet) #prints value in get_average
def print_grades(Subject): #Takes a subject, finds its key, and prints out each corresponding value.
    tests=dictionary.get(Subject)
    toPrint="Grades in "+Subject+": " #User interaction
    for i in range(len(tests)):
        toPrint+= (str)(tests[i])+", "
    print(toPrint)
def print_all_averages(): #Prints out all the value of every get_average.
#Also finds best and worst class by going through each and keeping a running track of which has the highest and lowest average.
    print("Averages for all classes: ")
    best=""
    best_val=0
    worst=""
    worst_val=100
    for key in dictionary:
        print(key+": "+(str)(get_average(key)))
        if (get_average(key)<worst_val):
            worst=key
            worst_val=get_average(key)
        if (get_average(key)>best_val):
            best=key
            best_val=get_average(key)
    print("Your best class is "+best+", and your worst class is "+worst) #user interaction
def get_GPA(): #Calculates the average of each of your averages (using the same sum/num averaging process), and converting that to a letter grade/GPA
    num=len(dictionary)
    sum=0
    for key in dictionary:
        sum+=get_average(key)
    sum/=num
    #Yes I did all of them because yes there IS a highly distinct difference between a B+ and an A- Miss Bono
    if (sum>92.5):
        return "A (4.0)"
    elif (sum>89.5):
        return "A- (3.7)"
    elif (sum>86.5):
        return "B+ (3.3)"
    elif (sum>82.5):
        return "B (3.0)"
    elif (sum>79.5):
        return "B- (2.7)"
    elif (sum>76.5):
        return "C+ (2.3)"
    elif (sum>72.5):
        return "C (2.0)"
    elif (sum>69.5):
        return "C- (1.7)"
    elif (sum>65.0):
        return "D (1.0)"
    else:
        return "F (0.0)"

        


if __name__=="__main__":
    main()