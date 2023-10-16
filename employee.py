"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def hasCommission(self, commission, contractNum):
        self.hasCommission = True
        self.commission = commission
        self.contractNum = contractNum
    
class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    
    def get_pay(self):
        pay = self.salary
        if self.hasCommission and self.contractNum != 0:
            pay += self.commission * self.contractNum
        elif self.hasCommission:
            pay += self.commission
        return pay

    def __str__(self):
        fstring = f"{self.name} works on a monthly salary of {self.salary}"
        if self.hasCommission:
            fstring += " and receives a "
            if self.contractNum != 0:
                fstring += f" commission for {self.contractNum} contract(s) at {self.commission}/contract"
            else:
                fstring += f" bonus commission of {self.commission}"
        fstring += f". Their total pay is {self.getPay()}"

class HourlyEmployee(Employee):
    def __init__(self, name, salary, hours):
        super().__init__(name, salary)
        self.hours = hours
    
    def get_pay(self):
        pay = self.salary * self.hours
        if self.hasCommission and self.contractNum != 0:
            pay += self.commission * self.contractNum
        elif self.hasCommission:
            pay += self.commission
        return pay

    def __str__(self):
        fstring = f"{self.name} works on a contract of {self.hours} at {self.salary}/hour"
        if self.hasCommission:
            fstring += " and receives a "
            if self.contractNum != 0:
                fstring += f" commission for {self.contractNum} contract(s) at {self.commission}/contract"
            else:
                fstring += f" bonus commission of {self.commission}"
        fstring += f". Their total pay is {self.getPay()}"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee("Charlie", 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee("Renee", 3000)
renee.hasCommission(200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee("Jan", 25, 150)
jan.hasCommission(220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee("Robbie", 2000)
jan.hasCommission(1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee("Ariel", 30, 120)
ariel.hasCommission(600, 0)