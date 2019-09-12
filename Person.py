import random
import time
import json
""" The experience of light is what gives each Person state """
class Light:

    def __init__(self):

        self.COLORTOP            = 999
        self.DEGREETOP           = 999
        self.MINUTETOP           = 99
        self.SECONDTOP           = 60
        self.PROCESSORTOP        = 10

        self.appearanceProcessor = [ random.randint(1,self.PROCESSORTOP) ,random.randint(1,self.PROCESSORTOP)  ,random.randint(1,self.PROCESSORTOP)]
        self.positionProcessor   = [ random.randint(1,self.PROCESSORTOP) ,random.randint(1,self.PROCESSORTOP)  ,random.randint(1,self.PROCESSORTOP)]
        
        
        self.eternity            = 0
        
        self.latitude            = [ random.randint(0,self.DEGREETOP)    ,random.randint(0,self.MINUTETOP   )  ,random.randint(0,self.SECONDTOP   )]
        self.longitude           = [ random.randint(0,self.DEGREETOP)    ,random.randint(0,self.MINUTETOP   )  ,random.randint(0,self.SECONDTOP   )]
        self.appearance          = [ random.randint(0,self.COLORTOP)     ,random.randint(0,self.COLORTOP    )  ,random.randint(0,self.COLORTOP    )]
        
        self.acknowledgement     = [ self.latitude ,self.longitude , self.appearance, self.appearanceProcessor, self.positionProcessor]

"""A Person inherits State from the light beset at the time of his birth """

class Memory:

    def __init__(self):

        self.sequence            = 0
        self.time                = float(1/100)
        self.state               = []
        self.CHANNEL             = 1/100
        
class Person(Light):

    def __init__(self):

        self.light    = Light()
        self.memories = list()
                
    def perception(self):

        return random.randint(0,1)

def test():
            
    david = Person()
    v_count = 0
    encounter = dict()
    encounter["start"]       = str(time.time())
    encounter["certificate"] = str(david.light.acknowledgement)
    waitTime = 0    
    #print(str(david.light.acknowledgement))
   # time.sleep(david.light.acknowledgement[4][0])
    
    for i in range(0,len(david.light.acknowledgement)):

        m_sequenece = 0

        if(i<=2):

            for j in range(0,len(david.light.acknowledgement[i])):

                currentValue = david.light.acknowledgement[i][j]

                while( currentValue > 0 ):

                    memory          = Memory() 
                    memory.sequence = m_sequenece
                    memory.time     = time.time()
                    memory.state    = david.light.acknowledgement
                    david.memories.append(memory)
                    m_sequenece  = m_sequenece + 1
                    currentValue = currentValue - 1 
                    david.light.acknowledgement[i][j] = currentValue
                    print(str(david.light.acknowledgement))
            
               #waitTime = david.light.acknowledgement[(len(david.light.acknowledgement)-1)][j]
                
        elif(i == 3 ):

            for j in range(0,len(david.light.acknowledgement[i])):
                currentValue = david.light.acknowledgement[i][j]
                while( currentValue > 0 ):

                    memory          = Memory() 
                    memory.sequence = m_sequenece
                    memory.time     = time.time()
                    memory.state    = david.light.acknowledgement
                    david.memories.append(memory)
                    currentValue = currentValue - 1 
                    david.light.acknowledgement[i][j] = currentValue
      #              print(str(david.light.acknowledgement))
            
        else:

            continue


    encounter["end"]      = str(time.time())
    encounter["elapsed"]  = float(encounter["end"]) - float(encounter["start"])
    encounter["person"]   = json.dumps((david))
    print(str(encounter))

    


    # individual = dict()
    # individual["start"]          = time.time()
    # individual["encounterStart"] = encounter["start"]

    # m_count  = 0
    # m_sequenece = 0

    


    # for i in range(0,len(david.light.acknowledgement)):

    #     if(i<2):

    #         for j in range(0,len(david.light.acknowledgement[i])):

    #             currentValue = david.light.acknowledgement[i][j] + david.perception()
                
                
    #             while(currentValue > 0):

    #                 memory          = Memory() 
    #                 memory.sequence = m_sequenece
    #                 memory.time     = time.time()
    #                 memory.state    = david.light.acknowledgement
                    
    #                 david.memories.append(memory)

    #                 david.light.acknowledgement[i][j] =  currentValue
    #                 waitTime = float(1) / float(david.light.acknowledgement[(len(david.light.acknowledgement)-1)][j])
    #                 time.sleep(waitTime)
    #                 m_sequenece  = m_sequenece + 1
    #                 currentValue = currentValue - 1
                    
    #     elif(i == 3 ):

    #         for j in range(0,len(david.light.acknowledgement[i])):


    #             currentValue = david.light.acknowledgement[i][j] + david.perception()


    #             while(currentValue > 0):

    #                 memory          = Memory() 
    #                 memory.sequence = m_sequenece
    #                 memory.time     = time.time()
    #                 memory.state    = david.light.acknowledgement
                    
    #                 david.memories.append(memory)

    #                 david.light.acknowledgement[i][j] =  currentValue
    #                 waitTime = float(1) / float(david.light.acknowledgement[(len(david.light.acknowledgement)-2)][j])
    #                 time.sleep(waitTime)
    #                 m_sequenece  = m_sequenece + 1
    #                 currentValue = currentValue - 1
    #     else:

    #         continue
individual = dict()
    # individual["start"]          = time.time()
    # individual["encounterStart"] = encounter["start"]

    # m_count  = 0
    # m_sequenece = 0

    


    # for i in range(0,len(david.light.acknowledgement)):

    #     if(i<2):

    #         for j in range(0,len(david.light.acknowledgement[i])):

    #             currentValue = david.light.acknowledgement[i][j] + david.perception()
                
                
    #             while(currentValue > 0):

    #                 memory          = Memory() 
    #                 memory.sequence = m_sequenece
    #                 memory.time     = time.time()
    #                 memory.state    = david.light.acknowledgement
                    
    #                 david.memories.append(memory)

    #                 david.light.acknowledgement[i][j] =  currentValue
    #                 waitTime = float(1) / float(david.light.acknowledgement[(len(david.light.acknowledgement)-1)][j])
    #                 time.sleep(waitTime)
    #                 m_sequenece  = m_sequenece + 1
    #                 currentValue = currentValue - 1
                    
    #     elif(i == 3 ):

    #         for j in range(0,len(david.light.acknowledgement[i])):


    #             currentValue = david.light.acknowledgement[i][j] + david.perception()


    #             while(currentValue > 0):

    #                 memory          = Memory() 
    #                 memory.sequence = m_sequenece
    #                 memory.time     = time.time()
    #                 memory.state    = david.light.acknowledgement
                    
    #                 david.memories.append(memory)

    #                 david.light.acknowledgement[i][j] =  currentValue
    #                 waitTime = float(1) / float(david.light.acknowledgement[(len(david.light.acknowledgement)-2)][j])
    #                 time.sleep(waitTime)
    #                 m_sequenece  = m_sequenece + 1
    #                 currentValue = currentValue - 1
    #     else:

    #         continue


    # individual["end"]          = time.time()
    # individual["elapsed"]      = float(individual["end"]) - float(individual["start"])
    # individual["memories"]       = david.memories

    # print("individual output " + str(individual))
    # print(' total iterations ' + str(v_count))


    # individual["end"]          = time.time()
    # individual["elapsed"]      = float(individual["end"]) - float(individual["start"])
    # individual["memories"]       = david.memories

    # print("individual output " + str(individual))
    # print(' total iterations ' + str(v_count))

    
   


test()



        





