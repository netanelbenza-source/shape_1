class ID_ERROR(Exception):
    pass

import json
from square import Square
from circle import Circle
from rectangle import Rectangle
import math

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()
    def create_shape(self, shape):
        for dict in self.shapes:
            if dict.get("id") == shape.id:
                raise ID_ERROR("already exists in the system") 
        self.shapes.append(shape.to_dict())
        self.save_to_json()
        print(" Tha shape update successfully ")    
        
    def get_all_shapes(self):
        return self.shapes
        
    def update_shape(self, shape_id, new_data):
        for dict in self.shapes:
            if dict.get("id") == shape_id :
                if dict["type"] == "square" :
                    dict["area"] = new_data["size"] * new_data["size"]
                    dict["perimeter"] = new_data["size"] * 4
                    self.save_to_json()
                    return

                elif dict.get("type") == "circle":
                    dict["area"] = math.pi *  math.pow(new_data["radius"],2)
                    dict["perimeter"] =  2 * math.pi * new_data["radius"]
                    self.save_to_json()
                    return
                
                elif dict.get("type") == "rectangle":
                    if "width" in new_data and "height" in new_data:
                        new_width = new_data["width"]
                        new_height = new_data["height"]
                        dict["area"] = new_width * new_height
                        dict["perimeter"] = 2 * (new_width + new_height)
                        self.save_to_json()
                        return
                    else:
                        raise  ValueError(" For rectangle, you must provide both 'length' and 'width")  
         
        raise ID_ERROR(" Does not exist in the system ")
                          
                    
    def delete_shape(self, shape_id):
        for i,dict in enumerate(self.shapes):
            if dict.get("id") == shape_id:
                    self.shapes.pop(i)
                    self.save_to_json()
                    print("Tha shape delete successfully")
                    return
        
        raise ID_ERROR(" Does not exist in the system ")
           
            
    def save_to_json(self):
        with open("project/shapes.json", "w",encoding="utf-8") as file:
                 json.dump(self.shapes,file,indent=4 ,ensure_ascii=False)
                
    
    
    def load_from_json(self):
        try:
            with open("project/shapes.json", "r",encoding="utf-8") as file:
                load_json = json.load(file)
                self.shapes = load_json
            
        except (FileNotFoundError,json.JSONDecodeError):
                self.shapes = []







def create_shape(choice,inserte):

    match choice:
        case "square":
            while True:
                try:
                    choice_1 = int(input(" please enter ID for the square : ")) 
                    choice_2 = int(input(" please enter side for the square : "))
                    break
                except ValueError :
                     print("error!!! : enter value only with tipe int ")
            s1 = Square(choice_1,"square",choice_2)    
            inserte.create_shape(s1)
            
        case "circle":
            while True:
                try:
                    choice_1 = int(input(" please enter ID for the circle : ")) 
                    choice_2 = int(input(" please enter radius for the circle : "))
                    break
                except ValueError :
                     print("error!!! : enter value only with tipe int ")
            c1 = Circle(choice_2,choice_1,"circle")    
            inserte.create_shape(c1)
             
        case "rectangle":
            while True:
                try:
                    choice_1 = int(input(" please enter ID for the rectangle : ")) 
                    choice_2 = int(input(" please enter width for the rectangle : "))
                    choice_3 = int(input(" please enter height for the rectangle : "))
                    break
                except ValueError :
                     print("error!!! : enter value only with tipe int ")
            r1 = Rectangle(choice_1,"rectangle",choice_2,choice_3)    
            inserte.create_shape(r1)
        case _:
            raise ValueError()    
       

def delete_shape(insert):
    while True:
        try:
            choice = int(input(" please enter ID for the shape to delete :"))
            try:
                insert.delete_shape(choice)
            except ID_ERROR:
                 print(" ID_ERROR : Does not exist in the system ")
            break
        except ValueError:
            print(" error!!! : enter value only with tipe int ")



def update_shape(insert):
    while True:
        try:
            choice = int(input(" please enter ID for the shape to update : "))
            
            found_shape = None
            for s in insert.get_all_shapes():
                if s.get("id") == choice:
                    found_shape = s
                    break


            new_data = {}
            shape_type = found_shape["type"]

            if shape_type == "square":
                new_data["size"] = int(input(" plaese enter size : "))
            elif shape_type == "circle":
                new_data["radius"] = int(input(" please enter radius : "))
            elif shape_type == "rectangle":
                new_data["width"] = int(input (" please enter width : "))
                new_data["height"] = int(input(" please enter height : "))

            try:
                insert.update_shape(choice, new_data)
                print(" The form has been successfully updated in the systemת!")
            except ID_ERROR:
                 print(" ID_ERROR : Does not exist in the system")
            break
        except ValueError:
                print(" error!!! : enter value only with tipe int ")

        



                