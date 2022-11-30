""""
Time Complexity : ??
Space Complexity : O(1)
"""
def calculateTax(salary, brackets):
    taxes = 0
    for x in brackets:
        if x[0] is not None and salary != 0:
            taxable = min(salary, x[0])
            taxes += taxable * x[1]
            salary -= taxable
        else:
            taxes += salary * x[1]

    return taxes


Salary = 45000
Brackets = [
[10000,0.3],
[20000,0.2],
[30000,0.1],
[None, 0.4]
]
print(calculateTax(Salary, Brackets))
