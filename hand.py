#just doing a basic select movment curently, prob gonna use json
from ClearScreen import clearScr,back
import time
from framework import Tools


prompt = "Computer ~# "
frameworkName = ['Tools',
                 'Machine',]



    
def begin():
    clearScr(False)
    beginBase = 0

    for i in frameworkName:
        beginBase += 1
        beginArrayBase = "{"+str(beginBase)+"} -"
        print(beginArrayBase, i)
    print("{99} - Exit")
    match input(prompt):
        case "1":
            clearScr()
            Tools.ToolIndex()
        case "2":
            #TODO
            """need to link this to somthing"""
        
        case "99":
              print("goodbye")
              return
        case "":
              print("just \'\'")
        case _:
              clearScr(True, True)
              
              

 

#start()
begin()