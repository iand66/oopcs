from __future__ import annotations

class Employee:

    num_emps = 0
    raise_amt = 1.05

    def __init__(self, first, last, title, pay) -> None:
        self.first = first
        self.last = last
        self.title = title
        self.pay = pay
        #self.email = first + "." + last + '@company.com'

        Employee.num_emps += 1

    def __repr__(self) -> str:
        return (f"{self.first} {self.last} {self.title} {self.pay} {self.email}")

    def __str__(self) -> str:
        return (f"{self.first} {self.last} {self.title}")

    @property
    def email(self) -> str:
        return (f"{self.first}.{self.last}@company.com")
    
    @property
    def fullname(self) -> str:
        return (f"{self.first} {self.last}")

    @fullname.setter
    def fullname(self, name) -> None:
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self) -> None:
        self.first = None
        self.last = None

    def pay_rise(self) -> None:
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amt) -> None:
        cls.raise_amt = amt

    @classmethod
    def from_string(cls, employee) -> Employee:
        first, last, title, pay = employee.split('-')
        return cls(first, last, title, float(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() >= 5:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, title, pay, skills:list) -> None:
        super().__init__(first, last, title, pay)
        #Employee.__init__(self, first, last, title, pay)
        self.skills = skills

    def __repr__(self) -> str:
        return (f"{self.first} {self.last} {self.title} {self.pay} {self.email} {self.skills}")

    def __str__(self) -> str:
        return (f"{self.first} {self.last} {self.title}")

class Manager(Employee):

    def __init__(self, first, last, title, pay, employees:list) -> None:
        super().__init__(first, last, title, pay)
        self.employees = employees

    def __repr__(self) -> str:
        return (f"{self.first} {self.last} {self.title} {self.pay} {self.email} {self.employees}")

    def __str__(self) -> str:
        return (f"{self.first} {self.last} {self.title}")

    def add_employee(self, employee) -> None:
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee) -> None:
        if employee in self.employees:
            self.employees.remove(employee)
    
    def list_employees(self) -> None:
        for e in self.employees:
            print(f"{self.fullname()} supervises {e.fullname()}")
 
e1 = Employee.from_string('Ian-Davies-Senior Consultant-100000')
d1 = Developer('Pedro','Davies','Backend Specialist',80000,['SQL','Python'])
m1 = Manager('Jeanette','Davies','Managing Director',250000,[])

e1.fullname = 'Zorba Magnificat'
print(e1.first)
print(e1.email)
print(e1.fullname)

del e1.fullname
print(e1.fullname)
