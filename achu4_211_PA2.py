'''
Honor Code Statement
---------------------------------------------------------------------------------
Name: Amanda Chu
Assignment: PA 2
Due Date: 09/25/2023
---------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
---------------------------------------------------------------------------------
Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions.
You can write in N/A if you don’t have any comments/assumptions.
---------------------------------------------------------------------------------
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
        10       20         30        40        50        60        70        80
---------------------------------------------------------------------------------
'''
#-------------------------------------------------------
# Task1

def gift_recommender (preference, budget):
    # The body of your function goes here
    #for each preference it checks for the amount the user enters 
    #and print out the corresponding item
    if preference == "electronics": 
        if budget <= 100:
            return "gaming earbuds"
        elif 100 < budget <= 200:
            return "headphone"
        elif budget > 200:
            return "smart watch"
    if preference == "clothing":
        if budget <= 25:
            return "tops"
        elif 25 < budget <= 50:
            return "jackets"
        elif 50 < budget <= 100:
            return "shoes"
        elif budget > 100:
            return "suits"
    if preference == "jewelry":
        if budget < 500:
            return "ring"
        elif 500 <= budget < 1000:
            return "necklace"
        elif budget >= 1000:
            return "bracelet"
    else:
        return "decorative gifts!"
    return gift_recommender (preference, budget)

#-------------------------------------------------------
# Task 2
def calculate_student_score (PA, mid_term_exam, final_exam):
    # The body of your function goes here
    #the equation to calculate the student score
    student_score = (PA * 0.4) + (mid_term_exam * 0.3) + (final_exam * 0.3)
    #when the final exam score is 0, the student scores is automatically 0 
    if final_exam == 0:
        student_score = 0
    #final exam score replaces midterm score
    elif mid_term_exam == 0:
        student_score = (PA * 0.4) + (final_exam * 0.6)
    #Calculates student scores with PA assignment and the two exam scores
    else:
        student_score = (PA * 0.4) + (mid_term_exam * 0.3) + (final_exam * 0.3)
    return float(student_score)

def calculate_letter_grade (score):
    # The body of your function goes here
    #checks for student scores, and displays which letter grade they have 
    if 90 < score <= 100:
        return "A"
    elif 80 < score <= 90:
        return "B"
    elif 70 < score <= 80:
        return "C"
    elif 60 <= score <= 70:
        return "D"
    elif score < 60:
        return "F"
    return calculate_letter_grade (score) 
#-------------------------------------------------------    
# Task 3

def is_discount_applicable (age, is_military, major, gpa):
    # The body of your function goes here
    #the statement returns true if the person is either in military or 60 years or older
    if is_military or age >= 60:
        return True
    #the person has to be majoring in CS and has a GPA of 3.7 or more to be eligible
    if major == "CS" and gpa >= 3.7: 
        return True
    else:
        return False

'''This function needs to call the 'is_discount_applicable' function 
in its body to calculate the final book price.'''
def book_price(age, is_military, major, gpa, book_category):
    # The body of your function goes here
    #checks for the price according to book category 
    #discount adder
    discount = 0
    
    if book_category == "science" or book_category == "fiction":
        price = 30
    elif book_category == "novel" or book_category == "horror":
        price = 20
    elif book_category == "mystery":
        price = 10
    elif book_category == "comic":
        price = 15
    else:
        price = 0
    
    #takes the previous function to check if the person is eligible
    #check the amount of discount according to book category  
    if is_discount_applicable(age, is_military, major, gpa):
        if book_category == "fiction" or book_category == "comic":
            discount = 20 
        elif book_category == "novel":
            discount = 40
        # calculate the total price 
        price = price * (1 - (discount / 100))
    return price
