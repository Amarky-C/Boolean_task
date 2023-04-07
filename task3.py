#Question 3 create a python function that calculates the age of student,
# if the student age is greater than or equal to 18 it should return true else false

current_year = 2023 
average_age = 18 

def age_cal():
    name_of_student = input("enter student name: ")
    print('Welcome!',name_of_student, 'to my age calculation app!')
    age_calculation = int(input("enter student date of birth: "))
    if age_calculation <= 2005 :
        final_age = current_year - age_calculation
        print('True!',name_of_student, "you are", final_age, "years old and qualified")
    else:
        final_age = current_year - age_calculation
        print('False!',name_of_student, "you are", final_age, "years old and disqualified")
age_cal()