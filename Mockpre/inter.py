# new_li =[1,2,3,4,5,6,7,8,1,2]
# set_ = set(new_li)
# print(set_)
#
# d ={}
# for ele in new_li:
#     if ele not in d:
#         d[ele] = 1
#     else:
#         d[ele] += 1
# print(d)
# for key,value in d.items():
#     if value ==1 :
#         print(key)

from abc import abstractmethod

class company:
    def __init__(self,name,dep,project):
        self.name = name
        self.dep = dep
        self.__project = project

    def display_info(self):
        return {f"{self.name} is working in {self.dep}"}

    def get_project(self):
        return {f"{self.__project}"}

    def add_emp(self):
        pass

class details(company):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id =  emp_id

    def add_emp(self,name):
        super
        print(f"{self.name} is working in sony")


    def display_info(self):
        print(f"{self.name} has  employee id has {self.emp_id}")








