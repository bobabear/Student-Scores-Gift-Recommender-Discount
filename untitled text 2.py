def gift_recommender (preference, budget):
    # The body of your function goes here
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
        else budget >= 1000:
            return "bracelet"
    if preference == "not listed above":
        return "decorative gifts!"
    return gift_recommender (preference, budget)

#-------------------------------------------------------
# Task 2
def calculate_student_score (PA, mid_term_exam, final_exam):
    # The body of your function goes here
    student_score = float((PA * 0.4) + (mid_term_exam * 0.3) + (final_exam * 0.3))
    return student_score

def calculate_letter_grade (score):
    # The body of your function goes here
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
    is_military == True 
    if age >= 60 and is_military and major == "CS" and gpa >= 3.7:
        return True
    else: 
        return False

'''This function needs to call the 'is_discount_applicable' function 
in its body to calculate the final book price.'''
def book_price (age, is_military, major, gpa, book_category):
    # The body of your function goes here
    discount = 0
    
    if book_category == "science" or "fiction":
        price = 30
        discount += 20
    if book_category == "novel" or "horror":
        price = 20
        if book_category == "novel":
            discount += 40
    elif book_category == "mystery":
        price = 10
    elif book_category == "comic":
        price = 15
    else:
        price = 0
        
    total_cost = 1 - (discount / 100) 
    return book_price (age, is_military, major, gpa, book_category)



