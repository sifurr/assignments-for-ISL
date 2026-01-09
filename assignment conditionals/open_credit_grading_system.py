print("--- Open Credit Grading System ---")
print("Available Departments: CSE, EEE, Civil, English, BBA")

dept = input("Enter Department Name: ")

total_earned_points = 0.0
total_credits = 0.0

if dept == "CSE":
    print("\n--- Department: CSE ---")
    
    # Subject 1
    print("Subject: Structured Programming")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00
    
    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 2
    print("\nSubject: Data Structures")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00
    
    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 3
    print("\nSubject: Algorithms")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00
    
    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

elif dept == "EEE":
    print("\n--- Department: EEE ---")
    
    # Subject 1
    print("Subject: Electrical Circuits")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00
    
    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 2
    print("\nSubject: Electronics I")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00
    
    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 3
    print("\nSubject: Signals and Systems")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00
    
    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

elif dept == "Civil":
    print("\n--- Department: Civil Engineering ---")
    
    # Subject 1
    print("Subject: Engineering Mechanics")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 2
    print("\nSubject: Surveying")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 3
    print("\nSubject: Structural Analysis")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

elif dept == "English":
    print("\n--- Department: English ---")
    
    # Subject 1
    print("Subject: Intro to Poetry")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 2
    print("\nSubject: Victorian Literature")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 3
    print("\nSubject: Modern Drama")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

elif dept == "BBA":
    print("\n--- Department: BBA ---")
    
    # Subject 1
    print("Subject: Principles of Accounting")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 2
    print("\nSubject: Marketing Management")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

    # Subject 3
    print("\nSubject: Business Mathematics")
    cr = float(input("Enter Credits for this course: "))
    ct = float(input("Enter Class Test (20): "))
    mid = float(input("Enter Mid Term (30): "))
    final = float(input("Enter Final Term (50): "))
    total_marks = ct + mid + final
    
    if total_marks >= 80: gp = 4.00
    elif total_marks >= 75: gp = 3.75
    elif total_marks >= 70: gp = 3.50
    elif total_marks >= 65: gp = 3.25
    elif total_marks >= 60: gp = 3.00
    elif total_marks >= 55: gp = 2.75
    elif total_marks >= 50: gp = 2.50
    elif total_marks >= 40: gp = 2.00
    else: gp = 0.00

    total_earned_points = total_earned_points + (gp * cr)
    total_credits = total_credits + cr

else:
    print("Invalid Department Name")

# Final Calculation
if total_credits > 0:
    cgpa = total_earned_points / total_credits
    print("\n--------------------------------")
    print("Department:", dept)
    print("Total Credits Attempted:", total_credits)
    print(f"Your Estimated CGPA is: {cgpa:.2f}")
    print("--------------------------------")