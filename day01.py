
def get_high_salary_employees(employee,minimum_salary):
    return [emp for emp in employee if emp["salary"] < minimum_salary]
employees = [
    {"name": "John", "salary": 50000, "experience": 2},
    {"name": "Alex", "salary": 80000, "experience": 5},
    {"name": "Sam", "salary": 60000, "experience": 3},
    {"name": "David", "salary": 90000, "experience": 7}
]
print(get_high_salary_employees(employees,80000))