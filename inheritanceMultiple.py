#multiple inheritance
# making parent class Teacher
class teacher():

    #it has following four methods
    def __init__(self,tecId=1,tecName='sunita',subject='python'):
        self.tecId=tecId
        self.tecName=tecName
        self.subject=subject
    def getTecName(self):
        return self.tecName
    def getId(self):
        return self.tecId
    def getSubject(self):
        return self.subject
    def show(self):
        print (self.tecName)
        print (self.tecId)
        print (self.subject)
class student():                  # making another parent class student

    def __init__(self,Id=2,name='geeta'):

        self.Id=Id
        self.name=name
    def getName(self):
        return self.name
    def getId(self):
        return self.Id

#deriving inheritance for class school
#from both teacher and student

class school(teacher,student):

    # it can inherit methods from both, but cant get the object data
    def __init__(self,tecId=3,tecName='babita',subject='hindi',Id=4,name='suresh',schId=6):

        teacher.__init__(self,tecId,tecName,subject)
        student.__init__(self,Id,name)

        self.schId=schId

        def getschlId(self):
            return self.schId
