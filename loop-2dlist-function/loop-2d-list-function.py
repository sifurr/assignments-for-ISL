#task 1
all_grades = [
[88, 92, 70], # Student 0 
 [45, 80, 77], # Student 1 (Has a 45!) 
 [99, 100, 95] # Student 2
]

def check_failing(grades_grid):
    index = 0
    for student_scores in grades_grid:
        for score in student_scores:
            if score < 50:                
                print(f"Student [{index}] failed a subject!")
        index += 1

check_failing(all_grades)


#Task 2
monitor = [
[0, 0, 0], 
 [0, 0, 0], 
[0, 0, 0]
]

def activate_row(screen, row_index):
    if row_index >= 0 and row_index < len(screen):
        screen[row_index] =  [one + 1 for one in screen[row_index]] 
        print(screen)
    else:
        print("Row index out of range")   

activate_row(monitor, 1)

