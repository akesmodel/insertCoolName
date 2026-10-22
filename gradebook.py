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
def add_grade(Subject, grade):
    if (Subject not in dictionary.keys()):
        dictionary[Subject]= [grade]
    else:
        dictionary[Subject].append[grade]
def print_average(Subject):
    tests=dictionary.get(Subject)
    num=len(tests)
    sum=0
    for i in range(num):
        sum+=tests[i]
    sum/=num
    print(sum)
def print_grades(Subject):
    tests=dictionary.get(Subject)
    toPrint="Grades in "+Subject+": "
    for i in range(len(tests)):
        toPrint+= (str)(tests[i])+", "
    print(toPrint)

if __name__=="__main__":
    main()