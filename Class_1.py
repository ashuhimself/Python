class Employee(object):
    raiseamount = 1.08
    num = 0
    def __init__(self,first,last,age,pay) -> None:
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        self.Name = first+" "+last
        Employee.num += 1 
    
    def show(self):
        print(self.Name, self.age, self.pay, self.Name)

    def inc_pay(self):
        self.pay = int(self.pay * Employee.raiseamount)
        
    


        

emp_1 = Employee('Ashutosh','Tiwari',24,1000)
emp_2 = Employee('Ashu','Singh',24,2000)
emp_3 = Employee('Ashu','333',24,2000)

emp_1.raiseamount = 1.9
print(Employee.raiseamount)
print(emp_1.raiseamount)
print(emp_1.__dict__)
print(Employee.num)