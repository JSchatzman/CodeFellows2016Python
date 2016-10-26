
schoolname = "Jordan's School"

#Import TSV data as source of all students, GPAs, grades and teachers
studentdata = [tuple(line.strip().split('\t')) for line in open('studentstsv.txt','r')]

#From studentdata, create set of distinct students and teachers.
studentlist = set((i[0] for i in studentdata[1:]))

teacherlist = set((i[3] for i in studentdata[1:]))

gradelist = set((i[2] for i in studentdata[1:]))

#create list of GPA to later find students average GPA:
gpalist = [int(i[1]) for i in studentdata[1:]]


#Create Intro Report
def createintroreport():
    print ('Welcome to {0}'.format(schoolname))
    print ('-'*50)
    #Use variables created above to generate initial report
    print ('There are {0} unique students that attend this school.'.format(len(studentlist)))
    print ('There are {0} unique teachers that attend this school.'.format(len(teacherlist)))
    print ('On average, students at this school maintain a {0} gpa.'.format(sum(gpalist)/len(gpalist)))
    reportinput = input("If you would like a grade report broken down by grade level, please enter 'grade'. \nIf you would like a grade report broken down by teacher, please enter 'teacher'. \nIf you would like exit, please enter 'exit'")

    print ('-'*50)

#For the secondary reports, we will opt to not use input in the following functions but instead use the global variables we already have
def creategradeeport():
    for i in sorted(gradelist, key = lambda x: int(x) if x.isdigit() else -999):
        grades = [int(y[1]) for y in studentdata[1:] if y[2] == i]
        print ("The average GPA for grade {0} is {1}".format(i, sum(grades)/len(grades)))
        

def createteacherreport():
    for i in sorted(teacherlist):
        grades = [int(y[1]) for y in studentdata[1:] if y[2] == i]


createintroreport()
creategradeeport()
    
