 
class Employee:

    num_of_emps = 0
    raise_amount = 1.04 #class variable; shared information among all instances

    def __init__(self, first, last, pay):   
        self.first = first #instance variable; unique to each instance
        self.last = last
        self.pay = pay 

        Employee.num_of_emps += 1 #increments the num of employees each time a new instance is created

    def __repr__(self): #readable for another dev, used for debugging 
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    @property #this acts like a getter
    def email(self): #property decorator allows us to define a method but still access it like an attribute
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self): #normal method
        return '{} {}'.format(self.first, self.last)  

    @fullname.setter #creates a setter for fullname 'attribute'
    def fullname(self, name):
        first, last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod #example of a class method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod #we're doing to use this method as an alternative constructor/__init__
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) 
        #this statement will allow the parent class to handle first, last, and pay
        # this statement will do the same thing
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees 
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
   # def print_emps(self):
   #     for emp in self.employees:
   #        print('-->', emp.fullname())

        
        


emp_1 = Employee('Brie', 'Molinari', 50000) #no need to pass the instance, it's passed automatically
emp_2 = Employee('Test', 'User', 60000)

dev_1 = Developer('James', 'Smith-Allen', 75000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Developer)) #this statement will tell us if something is an instance of a class
print(issubclass(Manager, Employee))

print(mgr_1.email)
#mgr_1.print_emps()
mgr_1.add_emp(emp_1)
mgr_1.remove_emp(dev_1)


print(emp_1.email)
print(emp_2.email)

print (help(Developer)) #this will print information about the class

print(emp_1.pay)
print(emp_1.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)


print(emp_1.__dict__) #prints the namespace of this instance, will not include class variables
print(Employee.__dict__) #will include only class variables

#emp_1.raise_amount = 1.05 you can still access and change this variable for a specific instance

Employee.set_raise_amount(1.06) #ex of calling a class method
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1) #ex of calling a class method as alt constructor/__inti__
print(new_emp_1.email)
print(new_emp_1.pay)

repr(emp_1)

emp_1.fullname = 'Joe Smith'




