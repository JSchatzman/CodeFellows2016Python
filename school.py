
import sys
import random

schoolname = "Jordan's School"

#Import TSV data as source of all students, GPAs, grades and teachers
studentdata = [tuple(line.strip().split('\t')) for line in open('studentstsv.txt','r')]

#From studentdata, create set of distinct students and teachers.
studentlist = set((i[0] for i in studentdata[1:]))

teacherlist = set((i[3] for i in studentdata[1:]))

gradelist = set((i[2] for i in studentdata[1:]))

#create list of GPA to later find students average GPA:
gpalist = [int(i[1]) for i in studentdata[1:]]




#Check for Empty School
def emptycheck():
    if not studentlist or not teacherlist:
        if not studentlist:
            print ('This school has no students!')
        if not teacherlist:
            print ('This school has no teachers!')
        print ('The program will now exit')
        sys.exit()

#Create Intro Report
def createintroreport():
    """print student count, teacher count, and average gpa"""
    print ('Welcome to {0}'.format(schoolname))
    print ('-'*50)
    #Use variables created above to generate initial report
    print ('There are {0} unique students that attend this school.'.format(len(studentlist)))
    print ('There are {0} unique teachers that attend this school.'.format(len(teacherlist)))
    print ('On average, students at this school maintain a {0} gpa.'.format(sum(gpalist)/len(gpalist)))
    print ('-'*50)


def creategradeeport():
    """create report showing average gpa for each grade"""
    print ('  Grade ---------- Average GPA')    
    for i in sorted(gradelist, key = lambda x: int(x) if x.isdigit() else -999):
        grades = [int(y[1]) for y in studentdata[1:] if y[2] == i]
        print ('    {0}{1}{2}'.format(i, ' '*(18-len(i)), str(sum(grades)/len(grades))[0:5]))
    print ('-----------------------------------------------------------------------------')
        

def createteacherreport():
    """create report showing average gpa for each grade and teacher"""  
    teachermap = []
    for i in studentdata[1:]:
        if [i[2],i[3]] not in teachermap:
            teachermap.append([i[2],i[3]])
    teachermap.sort(key = lambda x: (int(x[0]) if x[0].isdigit() else -999, x[1]))
    print ('  Grade ---------- Teacher ------------ Average GPA')
    print ('--------------------------------------------------') 
    for y in sorted(teachermap, key = lambda x: (int(x[0]) if x[0].isdigit() else -999, x[1])):
        grades = [int(i[1]) for i in studentdata[1:] if i[2] == y[0] and i[3] == y[1]]
        teachernamelength = len(y[1])
        grandenamelength = len(y[0])
        print ('    {0}{1}{2}{3}{4}'.format(y[0], ' '*(15-grandenamelength) , y[1], ' '*(24-teachernamelength), str(sum(grades)/len(grades))[0:5]))


def addstudent():
    studentname = input('Please enter new student''s name \n')
    studentgpa = input('Please enter new student''s GPA as a number between 0 and 100')
    while not studentgpa.isdigit() or (float(studentgpa) >= 100 or float(studentgpa) <= 0):
        studentgpa = input('You have entered an invalid GPA, Please enter a number between 0 and 100 \n')
    for i in teacherlist:
        print (i)   
    teachername = input('Please enter new student''s teacher.  The list of teachers is shown below.')
    while teachername not in teacherlist:
        teachername = input('Please enter an existing teacher''s name.')
    
        
        

def userprompt():
    """this function will be called as part of the module to intake user input and cal other functions"""
    inputquestion = 'If you would like a grade report broken down by grade level, please enter ''grade''. \n'
    inputquestion += 'If you would like a grade report broken down by teacher, please enter ''teacher''. \n'
    inputquestion += 'If you would like exit, please enter ''exit''. \n'
    reportinput = input(inputquestion)
    if reportinput == 'grade':
        createteacherreport()
    elif reportinput == 'teacher':
        createteacherreport()
    elif reportinput == 'exit':
        sys.exit()
    else:
        print ('Please enter a valid input as instructed')
        userprompt()

    
        


if __name__ == '__main__':
    addstudent()
    #emptycheck()
    #createintroreport()
    #userprompt()


#creategradeeport()
#createteacherreport()
