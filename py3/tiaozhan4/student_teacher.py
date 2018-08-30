#!/usr/bin/env python3
import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self,fenshu):
        
        return self.fenshu


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
     
    def get_grade(self,fenshu):
        ps=0
        fl=0
        for f,s in Counter(fenshu).most_common(4):
            if f =='A':
                ps+=s

            elif f =='B':
                ps+=s
            elif f =='C':
                ps+=s
            elif f =='D':
                fl+=s
        fs=("Pass:{},Fail{}").format(ps,fl)
        
        return fs
class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self,fenshu):
        fs=[]
        for f,s in Counter(fenshu).most_common(4):
            
            fs.append(f+':'+str(s))
        
        return ",".join(fs)
        # return # "{}:{}".format(,)
"""
person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
"""

if __name__=='__main__':
    juese=sys.argv[1]
    teacher1 = Teacher('Prashad', ['C', 'C++'])

    print(teacher1.get_details())
    
    if juese == 'teacher':
        teacher=Teacher("t1","k1")
        fenshu=sys.argv[2]
        print(teacher.get_grade(fenshu))
        print ("teacher")
    elif juese== 'student':
        s=Student("susan","CSE",2009)
        print(s.get_grade(sys.argv[2]))
