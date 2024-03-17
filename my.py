class Employee:
    # Write your code here
    average_age = 0.0
    average_salary = 0.0
    no_employes = 0
    
    def __init__ (self, name, age, salary):
        self.name = name
        self.name = age
        self.salary = salary
        update_average_age(age)
        update_average_salary(salary)
        Employee.no_employes += 1
    
    @classmethod
    def update_average_age(cls, age):
        if no_employes != 0:
            temp_total_age = cls.no_employes * cls.average_age
            cls.average_age = (temp_total_age + age) / (no_employes + 1)
        else:
            cls.average_age = age
    @classmethod 
    def update_average_salary (cls, salary):
        if no_employes != 0:
            temp_total_salary = cls.no_employes * cls.average_salary
            cls.average_salary = (temp_total_salary + salary) / (no_employes + 1)
        else :
            cls.average_salary = salary
    
    
