# Problem 1
def calculate_salary(name, salary, sales): 
    employee_name = name   
    final_salary = sales * 0.15 + salary

    print(f"TOTAL = R$ {final_salary:.2f}")

name_input = input()
salary_input = float(input())
sales_input = float(input())

calculate_salary(name_input, salary_input, sales_input)


# Problem 2
def solve_median(A, B, C):
    average = (A * 2 + B * 3 + C * 5) / 10
    print(f"MEDIAN = {average:.1f}")

A = float(input())
B = float(input())
C = float(input())

solve_median(A, B, C)