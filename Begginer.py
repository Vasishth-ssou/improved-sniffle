#short cut for comment: ctrl + K followed by ctrl + C
#short cut for comment: ctrl + k followed by ctrl + U
'''###s=['Control Engineering','Microprocessor and Application','Disital Signal Processing','Dynamics of Machines','Heat and Mass Transfer','CAD','IDSC']
#s.sort()
s=['CE','MPA','DOM','HMT','DSP','CAD','IDSC']
sk=100
prt=200
for index, subjects in enumerate(s, start=1):
    print(index,subjects)
s=('CE','MPA','DOM','HMT','DSP','CAD','IDSC')
s={'CE','MPA','DOM','HMT','DSP','CAD','IDSC'}'''


###Dictionaries
'''
mechatronics={'CE','MPA','DOM','HMT','DSP','CAD','IDSC'}
b_tech={'school': mechatronics}
admin={'name': 'Vasishth','prn': 1700601093,'Program': b_tech}

print(admin.get('mobile'))
#print(admin.get('mobile', 'not aval'))
#print(admin.get('prn'))
print(admin.get('prn','not aval'))
print(admin['name'])
print(admin)
admin.update({'name':'Vasishth Roy','age':19})
print(admin.get('age') 
#age=admin.pop('age')
#del admin['age']
print(admin)
print(age)
print(admin.keys())
print(admin.items())
for key,value in admin.items():
        print(key,value)
        '''
'''###Comparisons
#Equal: ==
#Not Equal: !=
#Greater Than and Less Than: >  <
#Greater or Equal: >=
#Less or Equal: <=
#Object Identity: is
#if else
i=int(input('1/2/3'))
if i==1:
    print('valueof i is',i)
elif i==2:
    print('value is 2')
elif i==0:
    print('elif can be used as switch case')#elif can be used as switch case
else:
    print('Sorry no. Value')
#and 
#or
#not
usr='admin'
log=False
if usr=='admin' and log:
    print('Access Granted')
else:
    print('Access Denied')
a=[1, 2 , 3]
b=[1, 2, 3]
c=a
print('a:',id(a))
print('b:', id(b))
print('c:',id(c))
print(a is b)
print(a is c)'''


###Loops
'''
##for
nums=[1,2,3,4,5]
for num in nums:
    print(num)
#break will completely break out of a loop
for num in nums:
    if num==3:
        print('Found')
        break
    print(num)
#continue moves onto next iteration of loop
for num in nums:
    if num==3:
        print('Found')
        continue    
    print(num)
    for letr in 'abc':
        print(num,letr)
z=int(input('1)range default\n2)Start from desired no.'))
if z==1:
    for i in range(10):
        print(i)
elif z==2:
    for i in range(1,11):
        print(i)
##while
x=10
while x > 0:
    print(x)
    x -= 1
#for infinite loop
while True:
    print(x)
    x += 1'''


###Functions
'''
# allows us to put code at specific locations    
# this is known as keeping one's code dry
def hello_func(): 
    pass    # pass is added for a function without any value
hello_func()
print(hello_func())
def hello_func():
    print('Hello Function')
hello_func()
def hello_func():
    return 'Hello Function'
print(hello_func())
print(hello_func().upper())
def hello_func(greeting,name='You'):
    return '{}, {}'.format(greeting,name)
print(hello_func('Hello',name='Vasishth'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('Programing','Terminal',name='Vasishth',age=19)
course=['Programing','Terminal']
info={'name':'Vasishth','age':19}
student_info(course,info)
student_info(*course,**info)
#Example Program
#Number of days per month. First value placeholder for indexing purposes
mnth_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """Returns true for leap years and false for non-leap year"""
    return year % 4==0 and (year % 100 != 0 or year % 400 ==0)

def days_in_mnth(year,mnth):
    """returns no.of days in that month in that year"""

    if not 1<= mnth <=12:
        return 'Invalid Month'

    if mnth ==2 and is_leap(year):
        return 29
    return mnth_days[mnth]
print(is_leap(2019))
m=int(input('month'))
y=int(input('year'))
print(days_in_mnth(y,m))'''


###Import Modules
'''
import days_in_month

courses=['control engineering','microprocessor and application','disital signal processing','dynamics of machines','heat and mass transfer','cad','idsc']
a=input('course name:\t')
index=days_in_month.find_index(courses,a)
print(index)
#

import days_in_month as dim #dim is specified name for this  module

courses=['control engineering','microprocessor and application','disital signal processing','dynamics of machines','heat and mass transfer','cad','idsc']
a=input('course name:\t')
index=dim.find_index(courses,a)
print(index)

#
#for importing all modules
from days_in_month import *

courses=['control engineering','microprocessor and application','disital signal processing','dynamics of machines','heat and mass transfer','cad','idsc']
a=input('course name: ')
index=find_index(courses,a)
print(index)
print(test)
cc=int(input('year:'))
ly=is_leap(cc)
da=days_in_mnth(cc,2)
print(da,ly)
''
#
from days_in_month import find_index as fi, test, days_in_mnth as dim

courses=['control engineering','microprocessor and application','disital signal processing','dynamics of machines','heat and mass transfer','cad','idsc']
a=input('course name: ')
index=fi(courses,a)
print(index)
print(test)

da=dim(1999,5)
print(da)

#
import sys
print(sys.path)
sys.path.append('D:\Study\4th Sem\Control Engineering\Project\Elevator\Elevator')
print('new path')
print(sys.path)
from Elevator import door_stat as ds ,floor_stat as fs
print(fs(1,0,1))
# '''






###Classes
'''
class employee:
    no_of_emp=0 # no. of employee
    raise_amount=1.04 #raise_amount is a class variable which represents yearly increase in classes
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.'+ last + '@company.com'
        employee.no_of_emp +=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    @classmethod ##classmethod
    def set_raise_amt(cls,amt): #cls=class; amt=amount
        cls.raise_amount = amt 
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay= emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_weekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
        

#Use of Class
emp_1=employee('Titan','Ackerman',5000000)
emp_2=employee('Pride', 'Sin',9990100)
"""
#Below is a method without class. This makes it the code longer hence we use classes

emp_1= employee()
emp_2=employee()
print(emp_1)
print(emp_2)
emp_1.first= 'Test1'
emp_1.last='User2'
emp_1.email='test1user2@company.com'
emp_1.pay=100000
emp_2.first= 'Test2'
emp_2.last='User1'
emp_2.email='test2user1@company.com'
emp_2.pay=200000
"""
"""
print(emp_1.email)
print(emp_2.email)
#to print full name 
#method 1
print('{} {}'.format(emp_1.first,emp_1.last))
#method 2: check class above
print(emp_2.fullname())
#method 3
print(employee.fullname(emp_1))
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
#print(employee.raise_amount)
#print(emp_1.__dict__)
#print(employee.__dict__)
##now if you want to change class variable then outside class then:
#employee.raise_amount=1.05
emp_1.raise_amount=1.05
emp_1.apply_raise() #you have to apply raise every time you  change in this method
print(emp_1.pay)
print(emp_1.__dict__) #now you'll see raise amount in emp_1         
#print(employee.raise_amount)
print(employee.no_of_emp)"""
##class method
employee.set_raise_amt(1.05)
print(employee.raise_amount)
print(emp_2.raise_amount)
print(emp_1.raise_amount)
#
emp_str_1='Erza-Scarlet-712123'
emp_str_2='Grey-Fullbuster-601000'
emp_str_3='Natsu-Dragoneel-641000'
new_emp_1=employee.from_string(emp_str_1)
#Below commented method takes some effort  
#first, last, pay= emp_str_3.split('-')
#new_emp_3=employee(first,last,pay)
print(new_emp_1.email,'\n',new_emp_1.pay)  
##static method
import datetime
my_date=datetime.date(2019, 5, 27)
print(employee.is_weekday(my_date))
'''


# '''
###OS Module - Use Underlying OS Functions

import os 
print(dir(os))      # shows all attributes and methods we can access 

# print current directory 
a = os.getcwd()
print(a)

# #  Change directory
os.chdir('C:/Users/cstt/Desktop/steps') ##Note##  Address is different for different PC 
print(os.getcwd())

os.chdir('C:/Users/cstt/Desktop/python')  

# check all files present in specified directory 
# syntax os.listdir('location or leave blank for current one')
b = os.listdir()
print(b) # it is saved in form of list 

# creating and removing directories
# there are two ways to create and delete directories:
# 1) os.mkdir() / os.rmdir()    # won't create/delete intermediate level directory 
# Eg:
os.mkdir('py_test') # os.mkdir('Python-testDir/testProgram_dir')  # it is not able to create intermediate directory   # preferd to create single level dir
print(os.listdir())
os.rmdir('py_test') # os.rmdir('Python-testDir/testProgram_dir')  # it is not able to delete intermediate directory   # preferd to create single level dir

# 2) os.makedirs() / os.removedirs()     # will create/delete intermediate level directory 
os.makedirs('Python-testDir/testProgram_dir')     # preferd to create multiple level dir
print(os.listdir())
os.removedirs('Python-testDir/testProgram_dir')   # preferd to delete multiple level dir
print(os.listdir())
 ## Renaming File
#  syntax os.rename('current file name in dir','custom name of file you want')
# os.rename('hello cc.py','codeChef.py')
print(os.listdir())

## get info about file/directory
print(os.stat('codeChef.py'))
print(os.stat('codeChef.py').st_size)
print(os.stat('codeChef.py').st_mtime) # modified time # to view in actuall datetime  or human readable format do following
from datetime import datetime
mod_time = os.stat('codeChef.py').st_mtime
print(datetime.fromtimestamp(mod_time))
 
 ## Traversing directory tree
 ##SYNTAX## os.walk('file location')
for dirpath, dirname, filename in os.walk('C:/Users/cstt/Desktop/python'):
    print('Path:',dirpath)
    print('Directories:',dirname)
    print('File Name:',filename)

##WARNING## Code is not working or not understood yet
# print(os.environ.get('HOME'))

# join file to pariticular path
file_path = os.path.join(os.getcwd(), 'test1.txt')
print(file_path)

# print()
answ=input('More Info on os.path? \ny/n')
if answ == 'y':
    print(help(os.path))
elif answ == 'n':
    pass
# show basename of path
print(os.path.basename('C:/temp/css.exe'))
# directory name of path
print(os.path.dirname('C:/temp/css.exe'))
# both directory and basename
print(os.path.split('C:/temp/css.exe'))
# check if path exist or not
print(os.path.exists('C:/temp/css.exe'))
# check if the basefile is directory or not
print(os.path.isdir('C:/temp/css.exe'))
# check if the basefile is file or not
print(os.path.isfile('C:/temp/css.exe'))
# split file path and extension
print(os.path.splitext('C:/temp/css.exe'))
# split drive
print(os.path.splitdrive('C:/temp/css.exe'))
