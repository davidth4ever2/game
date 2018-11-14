import time
import random

class Encounter:

    def __init__(self):

        self.COLORTOP            = 255
        self.DEGREETOP           = 360
        self.MINUTETOP           = 60
        self.SECONDTOP           = 60
        
        self.latitude            = [ random.randint(0,self.DEGREETOP)    ,random.randint(0,self.MINUTETOP   )  ,random.randint(0,self.SECONDTOP   )]
        self.longitude           = [ random.randint(0,self.DEGREETOP)    ,random.randint(0,self.MINUTETOP   )  ,random.randint(0,self.SECONDTOP   )]
        self.appearance          = [ random.randint(0,self.COLORTOP)     ,random.randint(0,self.COLORTOP    )  ,random.randint(0,self.COLORTOP    )]
        self.cost               = 0
    
class Environment:
    
    def __init__(self):

        self.TIMEUNIT = 1


class Person(Encounter):

    def __init__(self):

        self.START_UTILITY          = 10000
        self.PROCESSORTOP           = 10
        self.appearanceProcessor    = [ random.randint(1,self.PROCESSORTOP) ,random.randint(1,self.PROCESSORTOP)  ,random.randint(1,self.PROCESSORTOP)]
        self.positionProcessor      = [ random.randint(1,self.PROCESSORTOP) ,random.randint(1,self.PROCESSORTOP)  ,random.randint(1,self.PROCESSORTOP)]
        self.encounter              = Encounter()
        self.utility                = self.START_UTILITY
        self.perceivedCost          = 0 

    def perception(self):

            random.randint(0,1)

    def test(self):

        startTime = time.time()
            
        for component in self.encounter.latitude:
            
            self.perceivedCost = self.perceivedCost + self.perception()
            time.sleep(self.perception()  + 1)
            print(str(component))
        


p = Person()
p.test()


        





