# Student Scores, Gift Recommender, & Book Discount

This repository contains a Python module implementing five utility functions for:

1. **Gift Recommendation** based on preference and budget  
2. **Student Score Calculation** (weighted average of PAs and exams)  
3. **Letter Grade Assignment** from a numeric score  
4. **Discount Eligibility** based on age, military status, major, and GPA  
5. **Book Price Calculation** with an optional discount  

A simple test harness (`tester2.py`) is provided to verify your implementations.

---

## ⚙️ Prerequisites

- Python 3.6 or newer

---

## 📥 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/Student-Scores-Gift-Recommender-Discount.git
cd Student-Scores-Gift-Recommender-Discount
```

## How to Use

from achu4_211_PA2 import (
    gift_recommender,
    calculate_student_score,
    calculate_letter_grade,
    is_discount_applicable,
    book_price
)

## 1. Gift Recommender
print(gift_recommender('electronics', 150))
→ "headphone"

## 2. Student Score Calculation
(40% PAs, 30% midterm, 30% final; special rules if an exam = 0)
score = calculate_student_score(PA=85, mid_term_exam=90, final_exam=95)
print(score)
→ 90.5

## 3. Letter Grade
print(calculate_letter_grade(90.5))
→ "A"

## 4. Discount Eligibility
(applies if age ≥ 60, or is_military=True, or (major=="CS" and GPA≥3.7))
print(is_discount_applicable(age=65, is_military=False, major='ENG', gpa=3.5))
→ True

## 5. Book Price Calculation
(base price by category, minus discount if eligible)
print(book_price(age=65, is_military=False, major='ENG', gpa=3.5, book_category='fiction'))
→ 24.0  (30 × (1 – 0.20))

## Run Test Cases

**Test with Tester**

python3 tester2.py achu4_211_PA2.py

**Test a specific function**

python3 tester2.py achu4_211_PA2.py gift_recommender calculate_student_score

