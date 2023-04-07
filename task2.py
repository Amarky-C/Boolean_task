#Question 2 write a python function that takes 10list and 
#returns true if they have at least one common member 

Colors = ['blue', 'hisense', 'white', 'champagne', 'orange']
Fruits = ['cherry', 'tangerine','orange', 'apple', 'hisense']
Phone = ['hisense', 'infinix','orange','samsung', 'tecno']
Drinks = ['vodka', 'orange','champagne', 'hisense', 'liquor']
Laptop = ['samsung', 'apple','hisense', 'orange', 'hp']
Makeup = ['mascara','orange','eyeliner', 'hisense','blush']
Coffee = ['black', 'nescafe','orange', 'tetley','hisense']
Software = ['python', 'orange', 'html', 'hisense', 'javascript']
Tablet = ['hisense', 'android', 'xiaomi', 'orange', 'infinix']
Conditioner = ['thermocool', 'orange', 'scanfrost', 'hisense']


common_elements = set(Colors).intersection(Fruits,Phone,Drinks)

def cohort_four():
    if common_elements:
        print('True!', 'The common elements are', common_elements)
    else:
        print('False!', 'There are no common elements')
    
cohort_four()
