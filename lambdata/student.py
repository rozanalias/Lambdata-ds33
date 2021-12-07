'''Classes represtent some entity and today's Class to represent Students'''
# importing
import numpy as np
import pandas as pd
import random 


# class names should be UpperCamelCase

class Student:
    def __init__(self, age, name, gender, cerdits):
        '''Create a parent class'''

        self.age = int(age)
        self.name = name
        self.gender = gender 
        self.cerdits = int(cerdits)

    def status(self):
        '''first attribute'''
        print('processing')
        
    def new_class(self, new_cerdits):
        '''secound attribute'''
        self.cerdits = self.classes + new_cerdits

class BloomTechStudent(Student):
    '''Create a child class'''
    def __init__(self,age, name, gender,cerdits, program):
        super().__init__(age, name, gender, cerdits)
        

        self.program = program

def student_generator(new_student):
    '''generate randomly generate values for your Bloomtech student's attributes'''
    age = (18,61)
    name = ['John', 'Mira', 'Peter', 'Joe', 'Sam', 'Michaela']
    gender = ['male', 'female']
    cerdits = range(1, 81)
    program = ['Full stack software development', 'data science' ,'web developer']
    student_list = []
    for _ in range(new_student):
        rage = random.choice(age)
        rname = random.choice(name)
        rgender = random.choice(gender)
        rcerdits = random.choice(cerdits)
        rprogram = random.choice(program)

        bloomtech_student = BloomTechStudent(rage, rname, rgender,rcerdits, rprogram)

        student_list += [[bloomtech_student.age, bloomtech_student.name, 
        bloomtech_student.gender , bloomtech_student.cerdits , bloomtech_student.program]]

    return list 
        
print(student_generator(30))
    







