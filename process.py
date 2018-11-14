import json
import random
import time

class person:

    def __init__(self):

        self.id             = 0 
        self.action         = {}
        self.actions        = [] # array of actions 
        self.memories       = [] # spiritual
        self.features       = [] # material
        
        """ array included in birth certificate
        0 latitude   - degree, minutes, seconds
        1 longitude  - degree, minutes, seconds
        2 appearance - red   , green  , blue
        """
        self.birth   = dict([ ('certificate', [
                                                 [ random.randint(0,360), random.randint(0,60) ,  random.randint(0,60) ],
                                                 [ random.randint(0,360), random.randint(0,60) ,  random.randint(0,60) ],
                                                 [ random.randint(0,255), random.randint(0,255),  random.randint(0,255)]
                                              ]),
                              ('date',str(time.time()))])
        
    class memory:

        def __init__(self):

            
            self.start   = 0
            self.end     = 0
            self.cost    = 0

def test(inputfielname):

    biglist = []
    f = open( str(inputfielname) ,"w")
    
    x = person()
    m = x.memory()
    m.start = time.time()
    
    
    print("starting @ " + str(m.start))
    print(str(x.birth["certificate"]))

    class memoryTemplate:

        def __init__(self):

            self.timestamp = 0
            self.content   = ''

    startTime = time.time()
            
    for features in (x.birth["certificate"]):

        for feature in range(0,len(features)):        

                # to do  add processores to each item in the certificate array /
                temp = (features[feature])

                while(temp > 0):

                    writeOut = ""

                    temp = temp -1
                    features[feature] = temp

                    # This is where the sleeping starts
                    
                    time.sleep(.10)

                    
                    memoryframe           = memoryTemplate()
                    memoryframe.timestamp = time.time()
                    memoryframe.content   = x.birth["certificate"]

                    memory = dict(
                           Memorytype             = "foundational",
                           startTimeStamp         = startTime,
                           currentFrameTimeStamp  = str(memoryframe.timestamp),
                           content                = memoryframe.content)

                    print("memory")
                    biglist.append(str((json.dumps(memory))))
                    print(writeOut)
                    f.write(writeOut)
                    f.flush()

            
                

                # log what happened
                 
                # print('feature value ' + str(features) + " completed at " + str(time.time())) 
                # f.write('feature value ' + str(features) + " completed at " + str(time.time()))

                #wait
                
         
    f.write(json.dumps(biglist))
    f.close()

    
test("memory.json")

import json
from pprint import pprint

with open('memory.json') as f:
    data = json.load(f)

pprint(data)
        
