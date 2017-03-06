#furniture question

class furniture:
    
    def __init__(self,types='A',model='B'):
        self.types=types
        self.model=model

    def getType(self):
        return self.types
    def getModel(self):
        return self.model
    def show(self):
        print(self.types)
        print(self.model)
        
class sofa(furniture):

     def __init__(self,types='z',model='y',seats=4,cost=20000):

         furniture.__init__(self,types,model)

         self.seats=seats
         self.cost=cost

     def getSeats(self):
        return self.seats
    
     def getCost(self):
        return self.cost
    
     def show(self):
        print(self.seats)
        print(self.cost)
        
