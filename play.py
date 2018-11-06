import time
import random
# This is a test commit


def language_symbols():
    return  ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(language_symbols())

class Individual:

    latitude      = []
    longitude     = []
    appearance    = []
    storage       = 0
    other         = 0
    encounterCost = 0

    

    appearanceProcessor = [0,0,0]
    positionProcessor   = [0,0,0]

    
    class other():
        
        latitude      = []
        longitude     = []
        appearance    = []
        storage       = 0

        def __init__(self, o_individual):

            self.latitude        = o_individual.latitude 
            self.longitude       = o_individual.longitude
            self.appearance      = o_individual.appearance
            self.storage         = o_individual.storage
            
    def encounterCost(self, o_individual):

        count = 0
        totalCost   = 0

        for i in  self.latitude:
            
            #print('latitude:' + str(i) + " - " + str(self.other(o_individual).latitude[count]))
            totalCost    = (totalCost) + abs(i - self.other(o_individual).latitude[count])
            count = count + 1;

        count = 0
        
        for o in  self.longitude:
            
            
            #print('longitude:' + str(o) + "- " + str(self.other(o_individual).longitude[count]))
            totalCost    = totalCost + abs(o - self.other(o_individual).longitude[count])            
            count = count + 1;



        count  = 0
        
        for p in  self.appearance:
            
            #print('appearance:' + str(p) + "- " + str(self.other(o_individual).appearance[count]))
            totalCost    = totalCost + abs(p - self.other(o_individual).appearance[count])            
            count = count + 1;



        return (totalCost)

    def storage():

            return random.int(1000,10000)


    def __init__(self):

        self.latitude    = [ random.randint(0,360), random.randint(0,60),  random.randint(0,60)]

        self.longitude   = [ random.randint(0,360), random.randint(0,60),  random.randint(0,60)]

        self.appearance  = [ random.randint(0,255),random.randint(0,255),random.randint(0,255)]

        self.storage     =  random.randint(1000,10000)

        self.appearanceProcessor = [random.randint(1,10),random.randint(1,10),random.randint(1,10)]
        self.positionProcessor   = [random.randint(1,10),random.randint(1,10),random.randint(1,10)]

"""
This beginning the encounter , each individual is given a few thing durning instaniation
  1. they are given a latitude
  2. they are given a longitude
  3. they are given an appearance
  4. they are given an appearanceProcessor
  5. they are given a  positionProcessor
  6. they are given language symbols but that has not been added yet to the processing framework
  
"""

david_i = Individual()

sandra_i = Individual()

"""
individual creation ( Birth/Instaniatition)
"""


# print('david  latitude   --> ' + str(david_i.latitude))
# print('david  longitude  --> ' + str(david_i.longitude))
# print('david  appearance --> ' + str(david_i.appearance))
# testout = david_i.other(sandra_i)


 
"""
initial cost of encounter
"""

print('david  meet sandra --> ' + str(sandra_i.encounterCost(david_i)))
print('sandra meet david --> '  + str(david_i.encounterCost(sandra_i)))

# print('sandra  latitude  --> ' + str(sandra_i.latitude))
# print('sandra  longitude --> ' + str(sandra_i.longitude))
# print('sandra  appearence--> ' + str(sandra_i.appearance))


print('sandras initial self')

print('total work expected for latitude[0]' + str(sandra_i.latitude[0]))
print('total work expected for latitude[1]' + str(sandra_i.latitude[1]))
print('total work expected for latitude[2]' + str(sandra_i.latitude[2]))
      
print('total work expected for longitude[0]' + str(sandra_i.longitude[0]))
print('total work expected for longitude[1]' + str(sandra_i.longitude[1]))
print('total work expected for longitude[2]' + str(sandra_i.longitude[2]))


print('total work expected for appearance[0]' + str(sandra_i.appearance[0]))
print('total work expected for appearance[1]' + str(sandra_i.appearance[1]))
print('total work expected for appearance[2]' + str(sandra_i.appearance[2]))


print('davids initial self')

print('total work expected for latitude[0]' + str(david_i.latitude[0]))
print('total work expected for latitude[1]' + str(david_i.latitude[1]))
print('total work expected for latitude[2]' + str(david_i.latitude[2]))
      
print('total work expected for longitude[0]' + str(david_i.longitude[0]))
print('total work expected for longitude[1]' + str(david_i.longitude[1]))
print('total work expected for longitude[2]' + str(david_i.longitude[2]))


print('total work expected for appearance[0]' + str(david_i.appearance[0]))
print('total work expected for appearance[1]' + str(david_i.appearance[1]))
print('total work expected for appearance[2]' + str(david_i.appearance[2]))


# print('===========================================')



totalDiff = []

for i in range(0,3):

#        print(david_i.latitude[i])
#        print(sandra_i.latitude[i])
#        print('--------------------')

    totalDiff.append([david_i.latitude  [i] -  sandra_i.latitude[i],
                     david_i.longitude [i]  -  sandra_i.longitude[i],
                     david_i.appearance[i]  -  sandra_i.appearance[i]])
    
#        print('******************************************************')
#        print('******************************************************')
#        print('******************************************************')
#        
#    print('===========================================')
#
#    print('david actual  ' + str(david_i.latitude))
#
#    print('work for sandra' + str(totalDiff))


totalDiff = []

for i in range(0,(len(sandra_i.latitude))):

 #       print(sandra_i.latitude[i])
 #       print(david_i.latitude[i])
 #       print('--------------------')

    totalDiff.append([sandra_i.latitude  [i] -  david_i.latitude[i],
                         sandra_i.longitude [i] -  david_i.longitude[i],
                         sandra_i.appearance[i] -  david_i.appearance[i]])
        
#      print('******************************************************')
#      print('******************************************************')
#      print('******************************************************')
#      print('sandra actual  ' + str(sandra_i.latitude))    

    print('work for david ' + str(totalDiff))


#  print('sandra '  + str(sandra_i.appearanceProcessor))
#  print('david   ' + str(david_i.appearanceProcessor))

#  print('sandra '  + str(sandra_i.positionProcessor))
#  print('david   ' + str(david_i.positionProcessor))

#  print('processing sandra perception " ******************************************************')

#  print('processing latitude')


process_start     = 0
process_end       = 0
sleepTime         = 0

# this is where the work begins

for i in range(0,3):

    print(i)

    sleepTime = float(sandra_i.positionProcessor[i])

#       print('p=' + str(sleepTime))

    me          = david_i.latitude[i]
    sleepTime   = 1 #int(david_i.positionProcessor[i])
    them        = sandra_i.latitude[i]
    display =  '*'
    
#      print(str(david_i.latitude))
#      print('processing latitude difference '  + str(sandra_i.latitude[i] ) + ' - ' +  str(david_i.latitude[i]) )

    while(me != them):

        if(me > them):

            # print('processing latitude >' + str(sleepTime))
            me = me - 1
            # print('going to sleep ' + time.ctime())
            time.sleep(sleepTime)
            # print('awake '  + str(me) + '-->' + str(them))
            display = display + "*"
            
            # print(str(sandra_i.latitude) )
            # print(str(david_i.latitude) )
            # print('latitude position' + str(i))
            # print('sandra' + str(sandra_i.latitude[i])  +  "_____" + str(me) )
            # print('david'  + str( david_i.latitude[i])  +  "_____" + str(me) )
            
        if(me <  them):

            # print('processing latitude advance' + str(sleepTime))
            me = me + 1
            # print('going to sleep ' + time.ctime())
            time.sleep(sleepTime)
            # print('awake '  + str(me) + '-->' +  str(them))
            # print(str(sandra_i.latitude))
            # print(str(david_i.latitude))

            display = display + "*"
            # print('latitude position' + str(i))
            # print('sandra' + str(sandra_i.latitude[i])  +  "_____" + str(me) )
            # print('david' + str( david_i.latitude[i])  +  "_____" + str(me) )

        if(i==0):
            
            print(str(sandra_i.latitude))
            print(str(david_i.latitude))
            print(str(time.time()))
            print(str(me))
            print(david_i.latitude[1])
            print(david_i.latitude[2])
            
        if(i==1):
            
            print(str(sandra_i.latitude))
            print(str(david_i.latitude))
            print(str(time.time()))
            print(david_i.latitude[0])
            print(str(me))
            print(david_i.latitude[2])
            
        if(i==2):

            print(str(sandra_i.latitude))
            print(str(david_i.latitude))
            print(str(time.time()))
            print(david_i.latitude[1])
            print(david_i.latitude[2])
            print(str(me))
            
            
# print('processing longitude >')

process_start     = 0
process_end       = 0
sleepTime         = 0

for i in range(0,3):

    sleepTime = int(sandra_i.positionProcessor[i])

    # print('processing longitude >' + str(sleepTime))

    me          = david_i.longitude[i]
    sleepTime   = 1 #int(david_i.positionProcessor[i])
    them        = sandra_i.longitude[i]
    
    # print('processing longitude difference >'  + str(sandra_i.longitude[i] ) + ' - ' +  str(david_i.longitude[i]) )



    while(me != them):

        if(me > them):

      #      print('processing longitude > retreat' + str(sleepTime))
            me = me - 1
      #      print('processing longitude going to sleep ---' + time.ctime())
            time.sleep(sleepTime)
      #      print('awake' + str(me) + '-->' + str(them))

            # print('longitude position' + str(i))
            # print(str(sandra_i.longitude) )
            # print(str(david_i.longitude) )
            # print('sandra' + str(sandra_i.longitude[i])  +  "_____" + str(me) )
            # print('david' + str( david_i.longitude[i])  +  "_____" + str(me) )
  


        if(me < them):


       #     print('processing longitude > advance' + str(sleepTime))
            me = me + 1
       #     print('going to sleep +++' + time.ctime())
            time.sleep(sleepTime)
        #    print(str(me) + '-->' +  str(them))

        #    print('longitude position' + str(i))
        #    print(str(sandra_i.longitude) )
        #    print(str(david_i.longitude) )
        #    print('sandra' + str(sandra_i.longitude[i])  +  "_____" + str(me) )
        #    print('david' + str( david_i.longitude[i])  +  "_____" + str(me) )

        if(i==0):
            
            print(str(sandra_i.longitude))
            print(str(david_i.longitude))
            print(str(time.time()))
            print(str(me))
            print(david_i.longitude[1])
            print(david_i.longitude[2])
            
        if(i==1):

            print(str(sandra_i.longitude))
            print(str(david_i.longitude))
            print(str(time.time()))
            print(david_i.longitude[0])
            print(str(me))
            print(david_i.longitude[2])
            
        if(i==2):

            print(str(sandra_i.longitude))
            print(str(david_i.longitude))
            print(str(time.time()))
            print(david_i.longitude[1])
            print(david_i.longitude[2])
            print(str(me))
         
# print('processing appeareance')
    

process_start     = 0
process_end       = 0
sleepTime         = 0

for i in range(0,3):

    sleepTime = float(sandra_i.positionProcessor[i])
    # print('i' + str(i))
    # print('p=' + str(sleepTime))
    # print('david  appearance --> ' + str(david_i.appearance))
    me          = david_i.appearance[i]
    # print(str(david_i))
    sleepTime   = 1 # int(david_i.positionProcessor[i])
    them        = sandra_i.appearance[i]
    
    #  print('different --> appeareance'  + str(sandra_i.appearance[i] ) + ' - ' +  str(david_i.appearance[i]) )

              
    while(me != them):
        
        if(me > them):

       #      print('appearance retreat' + str(sleepTime))
            me = me - 1
            time.sleep(sleepTime)
       #      print(str(me) + '-->' + str(them))

            # print('appearance position' + str(i))
            # print(str(sandra_i.appearance))
            # print(str(david_i.appearance))
            # print('sandra' + str(sandra_i.appearance[i])  +  "_____" + str(me) )
            # print('david' + str( david_i.appearance[i])   +  "_____" + str(me) )
            
                      
        if(me < them):

       #      print('appearance advance' + str(sleepTime))
            me = me + 1
            time.sleep(sleepTime)

       #      print(str(me) + '-->' +  str(them))

            # print(str(sandra_i.appearance) )
            # print(str(david_i.appearance) )
            
            # print('appearance position' + str(i))
            # print('sandra'  + str(sandra_i.appearance[i])  +  "_____" + str(me) )
            # print('david'   + str(david_i.appearance[i] )  +  "_____" + str(me) )
            
        

        if(i==0):
            print(str(sandra_i.appearance))
            print(str(david_i.appearance))
            print(str(time.time()))
            print(str(me))
            print(david_i.appearance[1])
            print(david_i.appearance[2])
            
        if(i==1):

            print(str(sandra_i.appearance))
            print(str(david_i.appearance))
            print(str(time.time()))
            print(david_i.appearance[0])
            print(str(me))
            print(david_i.appearance[2])
            
        if(i==2):

            print(str(sandra_i.appearance))
            print(str(david_i.appearance))
            print(str(time.time()))
            print(david_i.appearance[1])
            print(david_i.appearance[2])
            print(str(me))
           
            
            



