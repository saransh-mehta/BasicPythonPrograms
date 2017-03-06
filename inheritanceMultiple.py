#multiple inheritance

class teacher():

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
class student():

    def __init__(self,Id=2,name='geeta'):

        self.Id=Id
        self.name=name
    def getName(self):
        return self.name
    def getId(self):
        return self.Id

class school(teacher,student):

    def __init__(self,tecId=3,tecName='babita',subject='hindi',Id=4,name='suresh',schId=6):

        teacher.__init__(self,tecId,tecName,subject)
        student.__init__(self,Id,name)

        self.schId=schId

        def getschlId(self):
            return self.schId
