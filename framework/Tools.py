from ClearScreen import clearScr, back
def ToolIndex():

    import hand
    clearScr()
    
    match input("Input popper number(80 max), press return to go back: "):
        
        case "1": 
            print("hammer")
            clearScr(True, False)
            ToolIndex()

        case "2": 
            print("not avalible yet")
        case "3": 
            print("not avalible yet")
       
        case "":
            print("going back")
            hand.begin()
        case _:
            clearScr(True, True)
            ToolIndex()
