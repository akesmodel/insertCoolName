dictionary = {
    "Math": [97, 97, 97, 93],
    "English": [86, 94, 92],
    "History": [74, 83, 79, 65], 
    "Comp Sci": [100,100,100,100], #Please make this happen Miss Bono 🥹 
}
def main():
    add_grade("Latin", 2)
    print(dictionary)
    print_average("English")
    print_grades("Comp Sci")
    print_all_averages()
    print(get_GPA("Math"))
    print(get_GPA("History"))
def add_grade(Subject, grade):
    if (Subject not in dictionary.keys()):
        dictionary[Subject]= [grade]
    else:
        dictionary[Subject].append[grade]
def get_average(Subject):
    tests=dictionary.get(Subject)
    num=len(tests)
    sum=0
    for i in range(num):
        sum+=tests[i]
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
def get_GPA(Subject):
    if (get_average(Subject)>92.5):
        return "A"
    elif (get_average(Subject)>89.5):
        return "A-"
    elif (get_average(Subject)>86.5):
        return "B+"
    elif (get_average(Subject)>82.5):
        return "B"
    elif (get_average(Subject)>79.5):
        return "B-"
    elif (get_average(Subject)>76.5):
        return "C+"
    elif (get_average(Subject)>72.5):
        return "C"
    elif (get_average(Subject)>69.5):
        return "C-"
    elif (get_average(Subject)>65.0):
        return "D"
    else:
        return "F"
        


if __name__=="__main__":
    main()