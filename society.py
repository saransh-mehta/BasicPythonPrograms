#society

class Society:
    
    def __init__(self,Sname='Surya Apartment',flat='A Type',Hno=20, memNo=3,income=25000):
        
        self.Sname=Sname
        self.flat=flat
        self.Hno=Hno
        self.memNo=memNo
        self.income=income
    def InputData(self):

        self.Sname=input("enter society name :")
        self.Hno=int(input("enter house no :"))
        self.memNo=int(input("enter member no :"))
        self.income=int(input("enter income :"))
        allocateFlat()
    def allocateFlat(self):

        if (self.income<15000):

            self.flat='C type'
            
        elif (self.income>=20000 and self.income<25000):
            self.flat='B type'
            
        elif (self.income>=25000):
            self.flat='A Type'
        return self.flat

    def showData(self):
        print("Society name :",self.Sname)
        print("\nFlat type :",self.flat)
        print("\nHno :",self.Hno)
        print("\nMember No :",self.memNo)
        print("\nIncome :",self.income)
        
            
        
                      
        
        
