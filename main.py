import shape ,rectangle,square,circle,shape_manager

def get_manu() -> None :
    print("    ____MENU_____    ")
    print("")
    print(" To add shape enter 1 : ")
    print(" To show all shape enter 2 : ")
    print(" To update shape enter 3 : ")
    print(" To delete shape enter 4 : ")
    print(" To Exit enter 5 : ")

def your_choice() -> None :

    return input(" please enter your choice : ")  

def menu_of_shapes() -> None :

    print(" To crate square enter square : ")
    print(" To crate circle enter circle : ")
    print(" To crate rectangle enter rectangle : ")

def loading_create_shape(choice,inserte):
     try:
        shape_manager.create_shape(choice,inserte)
     except ValueError:
         print(" error!!! : The shape name is incorrect" )
                                      


# def loading_delete_shape(insert):
#     shape_manager.delete_shape(insert)



def main():
    manajer = shape_manager.ShapeManager()
    while True:
        get_manu()
        choice = your_choice()
        match choice:
            case "1":
                menu_of_shapes()
                choice = your_choice().lower()
                loading_create_shape(choice,manajer)
            
            case "2":
                # print(manajer.get_all_shapes())
                pass
            
            case "3":
                pass
            
            case "4":
                loading_delete_shape(manajer)
            
            case "5":
                break
            
            case _ :
                print("Enter an existing value in the menu")

main()