#inheritance implementation

class father():
    def __init__(self,name='saransh',age=54):
        self.name=name
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        self.age=age

class son(father):

    def __init__(self,name,age,rollNo=34,marks=86):

        father.__init__(self,name,age)

        self.rollNo=rollNo
        self.marks=marks

    def getRoll(self):
         return self.rollNo
    def getMarks(self):
         return self.marks
