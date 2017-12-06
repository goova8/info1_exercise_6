from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        assert isinstance(title, Module)
        
        obj = title
        self.modules.append(obj)
        self.grades[obj] = title.get_grade()

    def get_list_modules(self):
        print("Modules of Student {}:".format(self.name))
        for element in self.modules:
            print("\t{}".format(element.title))

    def get_grades(self):
        print("Grades of Student {}:".format(self.name))
        for title, grade in self.grades.items():
            print("\t{}: {}".format(title.title, grade))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
