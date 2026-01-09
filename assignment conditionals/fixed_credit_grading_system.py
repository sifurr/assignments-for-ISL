print("--- Fixed Credit Grading System ---")
print("Available Departments: CSE, EEE, Civil, English, BBA")

dept = input("Enter Department Name: ")

total_earned_points = 0.0
total_credits = 0.0

if dept == "CSE":
    print("\n--- Department: CSE ---")
    
    # Subject 1
    print("Subject: Structured Programming (Cr: 3.0)")
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
    
    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 2
    print("\nSubject: Data Structures (Cr: 3.0)")
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
    
    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 3
    print("\nSubject: Algorithms (Cr: 4.0)")
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
    
    total_earned_points = total_earned_points + (gp * 4.0)
    total_credits = total_credits + 4.0

elif dept == "EEE":
    print("\n--- Department: EEE ---")
    
    # Subject 1
    print("Subject: Electrical Circuits (Cr: 3.0)")
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
    
    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 2
    print("\nSubject: Electronics I (Cr: 3.0)")
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
    
    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 3
    print("\nSubject: Signals and Systems (Cr: 4.0)")
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
    
    total_earned_points = total_earned_points + (gp * 4.0)
    total_credits = total_credits + 4.0

elif dept == "Civil":
    print("\n--- Department: Civil Engineering ---")
    
    # Subject 1
    print("Subject: Engineering Mechanics (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 2
    print("\nSubject: Surveying (Cr: 4.0)")
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

    total_earned_points = total_earned_points + (gp * 4.0)
    total_credits = total_credits + 4.0

    # Subject 3
    print("\nSubject: Structural Analysis (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

elif dept == "English":
    print("\n--- Department: English ---")
    
    # Subject 1
    print("Subject: Intro to Poetry (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 2
    print("\nSubject: Victorian Literature (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 3
    print("\nSubject: Modern Drama (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

elif dept == "BBA":
    print("\n--- Department: BBA ---")
    
    # Subject 1
    print("Subject: Principles of Accounting (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 2
    print("\nSubject: Marketing Management (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

    # Subject 3
    print("\nSubject: Business Mathematics (Cr: 3.0)")
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

    total_earned_points = total_earned_points + (gp * 3.0)
    total_credits = total_credits + 3.0

else:
    print("Invalid Department Name")

# Final Calculation
if total_credits > 0:
    cgpa = total_earned_points / total_credits
    print("\n--------------------------------")
    print("Department:", dept)
    print("Total Credits Attempted:", total_credits)
    print(f"Your Estimated CGPA is: {cgpa:.2f}")
    print("-------------------------------")