import shape ,rectangle,square,circle,shape_manager

def get_manu():
    print("    ____MENU_____    ")
    print("")
    print(" To add shape enter 1 : ")
    print(" To show all shape enter 2 : ")
    print(" To update shape enter 3 : ")
    print(" To delete shape enter 4 : ")
    print(" To Exit enter 5 : ")

def your_choice():
    return input(" please enter your choice : ")  






def main():
    manjer = shape_manager.ShapeManager()
    while True:
        get_manu()
        choice = your_choice()
        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _ :
                print("Enter an existing value in the menu")

main()