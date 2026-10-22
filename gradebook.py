dictionary = {
    "Math": [97, 97, 97, 93],
    "English": [86, 94, 92],
    "History": [74, 83, 79, 65], 
    "Comp Sci": [100,100,100,100], #Please make this happen Miss Bono 🥹 
}
def main():
    good=False
    while (good==False):
        print("Hello! Would you like to") 
        print("a) See your averages for each class?")
        print("b) See your grades for a specific class?")
        print("c) See your GPA?")
        print("d) Add a test score for a class?")
        choice=input("(a/b/c/d) ")
        if (choice=="a"):
            print_all_averages()
        elif (choice=="b"):
            Subject=input("Which subject do you want to see your grades in?")
            print_grades(Subject)
        elif (choice=="c"):
            print("Your GPA is: "+get_GPA())
        else:
            Subject=input("Which subject do you want to add a grade for? ")
            grade=input("What grade did you get on that test? ")
            add_grade(Subject,grade)
            print("Your new average in "+Subject+" is: "+ (str)(get_average(Subject)))
        keep_going=input("Would you like to anything else? (y/n) ")
        if keep_going=="n":
            good=True
    print("Have a great day!")
def add_grade(Subject, grade):
    if (Subject not in dictionary.keys()):
        dictionary[Subject]= [grade]
    else:
        dictionary[Subject].append(grade)
def get_average(Subject):
    tests=dictionary.get(Subject)
    num=len(tests)
    sum=0
    for i in range(num):
        sum+=(int)(tests[i])
    sum/=num
    return sum
def print_average(Subject):
    print(get_average(Subject))
def print_grades(Subject):
    tests=dictionary.get(Subject)
    toPrint="Grades in "+Subject+": "
    for i in range(len(tests)):
        toPrint+= (str)(tests[i])+", "
    print(toPrint)
def print_all_averages():
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
    print("Your best class is "+best+", and your worst class is "+worst)
def get_GPA():
    num=len(dictionary)
    sum=0
    for key in dictionary:
        sum+=get_average(key)
    sum/=num
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