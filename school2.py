
import sys
import random

schoolname = "Jordan's School"

#Import TSV data as source of all students, GPAs, grades and teachers
studentdata = [tuple(line.strip().split('\t')) for line in open('studentstsv.txt','r')]

#From studentdata, create set of distinct students and teachers.
studentlist = set((i[0] for i in studentdata[1:]))

teacherlist = set((i[3] for i in studentdata[1:]))

gradelist = set((i[2] for i in studentdata[1:]))

#Create dictionary with teachers as keys and values as student count as value
teacherstudentcount = {}
for i in teacherlist:
    teacherstudentcount[i] = len([x for x in studentdata[1:] if i == x[3]])

#Create dictionary with grades as keys and values as student count
gradestudentcount = {}
for i in gradelist:
    gradestudentcount[i] = len([x for x in studentdata[1:] if i == x[2]])

#Create nested array that maps teachers to their grades
teachermap = []
for i in studentdata[1:]:
    if [i[2],i[3]] not in teachermap:
        teachermap.append([i[2],i[3]])
teachermap.sort(key = lambda x: (int(x[0]) if x[0].isdigit() else -999, x[1]))



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
    gpalist = [int(i[1]) for i in studentdata[1:]]
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
    print ('  Grade ---------- Teacher ------------ Average GPA')
    print ('--------------------------------------------------') 
    for y in sorted(teachermap, key = lambda x: (int(x[0]) if x[0].isdigit() else -999, x[1])):
        grades = [int(i[1]) for i in studentdata[1:] if i[2] == y[0] and i[3] == y[1]]
        teachernamelength = len(y[1])
        grandenamelength = len(y[0])
        print ('    {0}{1}{2}{3}{4}'.format(y[0], ' '*(15-grandenamelength) , y[1], ' '*(24-teachernamelength), str(sum(grades)/len(grades))[0:5]))


def addstudent():
    """this function adds a new student to studentdata if a valid GPA and available teacher is chosen"""
    studentname = raw_input('Please enter new student''s name \n')
    for i in teacherlist:
        print (i)   
    teachername = raw_input('Please enter new student''s teacher.  The list of teachers is shown above.')
    while teachername not in teacherlist:
        teachername = raw_input('Please enter an existing teacher''s name.')
    studentcount = len([i for i in studentdata if i[3] == teachername])
    teachergrade = set([i[2] for i in studentdata if i[3] == teachername]).pop()
    gpa = random.randint(0,100)
    if studentcount < 10:
        studentdata.append([studentname, gpa, teachergrade, teachername])
        teacherstudentcount[teachername] += 1
        gradestudentcount[teachergrade] += 1
        print ("All done, {0} has been assigned to Mr/Mrs. {1}'s class with a GPA of {2}.").format(studentname, teachername, gpa)
    else:
        alternateteacher = set([i[3] for i in studentdata if i[3] != teachername and i[2] == teachergrade])
        if alternateteacher:
            alternateteacher = alternateteacher.pop()
            studentdata.append([studentname, gpa, teachergrade, alternateteacher])
            teacherstudentcount[alternateteacher] += 1
            gradestudentcount[teachergrade] += 1
            print ("There are no spots available in Mr/Mrs. {0}'s class.  The new student has been assigned to Mr./Mrs. {1} class with a gpa of {2}".format(teachername, alternateteacher, gpa))
        else:
            print ("We're sorry, there are no spots available for the new student in his/her grade. {0} will not be able to attend this school".format(studentname))

def addteacher():
    newteacher = raw_input("Please enter new teacher's name. \n")
    teacherlist.extend(newteacher)
    gradefinder = lambda x: str(x) if x > 0 else 'K'
    teachermap.append([gradefinder(random.randint(0,12)), newteacher])

def rollcall():
    print ('  Grade  -----------  StudentName')
    for i in sorted(studentdata[1:], key = lambda x: (int(x[2]) if x[2].isdigit() else -999, x[0])):
        gradelength = len(i[2])
        print ('   {0}{1}{2}').format(i[2], ' '*(17-gradelength), i[0])
        
           
def userprompt():
    """this function will be called as part of the module to intake user input and cal other functions"""
    inputquestion = 'If you would like a grade report broken down by grade level, please enter ''grade''.'
    inputquestion += 'If you would like a grade report broken down by teacher, please enter ''teacher''. \n'
    inputquestion += 'If you would like exit, please enter ''exit''. \n'
    reportinput = raw_input(inputquestion)
    if reportinput == 'grade':
        createteacherreport()
    elif reportinput == 'teacher':
        createteacherreport()
    elif reportinput == 'exit':
        confirmexit = raw_input("Are you sure you want to exist, please enter 'Yes' or 'No \n")
        while confirmexit != 'Yes' and confirmexit != 'No':
            confirmexit = raw_input("Please enter 'Yes' or 'No \n")
        if confirmexit == 'Yes':
            sys.exit()
        elif confirmexit == 'No':
            userprompt()
    else:
        print ('Please enter a valid input as instructed')
        userprompt()

    
if __name__ == '__main__':
    print sys.argv
    if 'roll_call' in sys.argv:
        emptycheck()    
        rollcall()
        sys.exit()
    emptycheck()    
    createintroreport()
    userprompt()
    #print (teacherstudentcount)
    #addstudent()
    #emptycheck()
    #createintroreport()
    #userprompt()


#creategradeeport()
#createteacherreport()
