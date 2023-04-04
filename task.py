#0
#1

#Question 1 write a function that returns a bool type

a= 40
b= 136

print(bool(a==b)) #returns false as a is not equal to b
print(bool(a>b))  #returns false as a is not greater than b
print(bool(a<b))  #returns true as a is greater than b
print(bool(a!=b))  #returns true as a is not equal to b



#Question 2 write a python function that takes 10list and 
#returns true if they have at least one common member 

Colors = ['blue', 'red', 'white', 'champagne', 'orange']
Fruits = ['cherry', 'tangerine','orange', 'apple', 'banana']
Phone = ['apple', 'infinix','orange','samsung', 'tecno']
Drinks = ['vodka', 'orange','champagne', 'whiskey', 'liquor']

common_elements = set(Colors).intersection(Fruits,Phone,Drinks)

def cohort_four():
    if common_elements:
        print('True!', 'The common elements are', common_elements)
    else:
        print('False!', 'There are no common elements')
    
cohort_four()



#Question 3 create a python function that calculates the age of student,
# if the student age is greater than or equal to 18 it should return true else false

current_year = 2023 
average_age = 18 

def age_cal():
    name_of_student = input("enter student name: ")
    age_calculation = int(input("enter student date of birth: "))
    if age_calculation <= 2005 :
        final_age = current_year - age_calculation
        print('True!',name_of_student, "you are", final_age, "years old and qualified")
    else:
        final_age = current_year - age_calculation
        print('False!',name_of_student, "you are", final_age, "years old and disqualified")
age_cal()

