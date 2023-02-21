class Patient:
    def __init__(self,id,name,disease,treatment=''):
        self.PatientID = id
        self.PatientName = name
        self.disease = disease
        self.treatment = treatment

    def settreatment(self,treatment):
        self.treatment = treatment
        print('Treatment Type:',self.treatment)
      
    def Chart(self):
        print('Patient ID:',self.PatientID)
        print('Patiend Name:',self.PatientName)
        print('Patient Disease:',self.disease)

class Doctor:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print('Doctor ID:',self.id)
        print('Doctor Name:',self.name)

    def treat(self,treatment):
        Patient.settreatment(self,treatment)
        

patient = Patient('1','Ahmed Nizai','heary disease')
doc = Doctor('23','Dr.Khurram Naveed')
doc.treat('Surgery')
patient.Chart()
doc.display()




##
print('\n\n')
class Bird:
    def __init__(self,name,color,gender='m'or'f'):
        self._name = name
        self._color = color
        self._gender = gender
    def SetName(self,name):
        self._name = name
    def GetName(self):
        return self._name
    def SetColor(self,color):
        self._color = color
    def GetColor(self):
        print(self._color)
    def SetGender(self,gender):
        self._gender = gender
    def GetGender(self):
        print(self._gender)
    def Display(self):
        print(f'Name: {self._name}\nColor: {self._color}\nGender: {self._gender}')

class Cage:
    def __init__(self,cno=0,csize=0,list_of_birds=[]):
        self._cno = cno
        self._csize = csize
        self._lob = list_of_birds

    def addbird(self,birb):
        self._lob.append(birb)
    
    def deletebird(self,borb):
        self._lob.remove(borb)

    def DisplayCage(self):
        print(f'Cage Number: {self._cno}\nCage Size: {self._csize}\nBirds in cage: {self._lob}')

b1 = Bird('Sparrow','Brown','f')
b2 = Bird('Eagle','White','m')
b3 = Bird('Usama','Gray','m')
b4 = Bird('Alina','Blue','f')

c1 = Cage(1,5,[b1.GetName(),b2.GetName(),b3.GetName()])
c1.DisplayCage()
c1.addbird(b4.GetName())
c1.deletebird(b2.GetName())
c1.DisplayCage()
b1.Display()

##
print('\n\n')
class student:
	def __init__(self,id=0,name=""):
		self.id=id
		self.name=name
	def Display(self):
		print(self.id,self.name)
class course:
	student_list=[]
	def __init__(self,student,course=""):
		self.student_obj=student
		self.course=course
		#self.student_list=[]
	def courseName(self):
		return self.course
	def addStudent(self):
		course.student_list.append(self.student_obj)
	def dropStudent(self):
		course.student_list.remove(self.student_obj)
		print("Removed:",end="")
		self.student_obj.Display()
		print()
	def displayStudents(self):
		for student in course.student_list:
			student.Display()
	def course_Strength(self):
		return len(self.student_list)
course_obj=course(student(101,"Programming"),"Class")
course_obj.addStudent()
course_obj=course(student(102,"Math"),"Class")
course_obj.addStudent()
course_obj=course(student(103,"Science"),"Class")
course_obj.addStudent()
course_obj.displayStudents()
print("Total students in ",course_obj.courseName(),"are:",course_obj.course_Strength())
print()
course_obj.dropStudent()
course_obj.displayStudents()
print("Total students in ",course_obj.courseName(),"are:",course_obj.course_Strength())