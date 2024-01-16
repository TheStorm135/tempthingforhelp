import os
back = "Invalid option, Press return to go back."
def clearScr(buttonBack = bool, valid=bool):
    if buttonBack == True and valid == True:
        input(back)
        os.system('clear')
    elif buttonBack == True and valid == False:
        input("Press return to go back")
        os.system('clear')
    else:
        os.system('clear')

# if empty just clear
# if false also just clear
# if True true invalid option
#if true false then press return
        
