# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         return self.marks>40
# s1=Student("Harshini",35)
# print(f"{s1.name}:{"Passed" if s1.is_passed() else "Failed"}")
# s2=Student("Manisha",80)
# print(f"{s2.name}:{"Passed" if s2.is_passed() else "Failed"}")
from hmac import new


class Employee:
    company_name="TechCorp" #Class Variable
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("Harshini")
e2=Employee("Meghana")
print(e1.name,"-",e1.company_name)
print(e2.name,"-",e2.company_name)
Employee.change_company("MNC")
print(e1.name,"-",e1.company_name)
print(e2.name,"-",e2.company_name)