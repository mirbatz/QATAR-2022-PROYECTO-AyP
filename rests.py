
class Product:

    def __init__(self,id_stadium,id_rest,name_rest,type,name,specs,price_iva):

        self.id_stadium = id_stadium
        self.id_rest = id_rest
        self.name_rest = name_rest
        self.type = type
        self.name = name
        self.specs = specs
        self.price_iva = price_iva

def show_rests(products,stadiums):

    print("-- Búsqueda de productos --\n\n    1. Según el nombre del producto\n    2. Según el tipo de producto\n    3. Ségun el precio del producto\n\n    0. Regresar al menú principal")

    opc = input("\nElije una opción: ")

    while opc.isnumeric() == False or int(opc) not in range(4):
        opc = input("\nOpción inválida. Por favor elija una opción contenida en el menú: ")

    print("\n")
    
    if opc == "1":

        print_prods = []
    
        for x in products:
            x = vars(x)
            for key,value in x.items():
                if key == "name":
                    if value not in print_prods:
                        print_prods.append(value)
        print("-- Búsqueda por nombre de producto --\n")
    
        for y in print_prods:
            print("    ",y,"(",print_prods.index(y)+1,")")
            
        aux = int(input("\nIngrese el número correspondiente al producto que desea buscar, o ingrese 0 para regresar al menú de búsqueda: "))
        while aux not in range(9):
            aux = int(input("\nIngreso inválido. Ingrese un valor contenido en la lista: "))
        if aux == 0:
            print("\n")
            show_rests(products,stadiums)    
        producto = print_prods[aux-1]
    
        for x in products:
            x = vars(x)
    
            for key,value in x.items():
                if key == "name":
                    if producto == value:
                        print("\n--",x["name"],"--")
                        if x["type"] == "beverages":
                            if x["specs"] == "alcoholic":
                                print("Tipo: bebida alcohólica")
                            elif x["specs"] == "non-alcoholic":
                                print("Tipo: bebida no alcohólica")
                        elif x["type"] == "food":
                            if x["specs"] == "package":
                                print("Tipo: comida empacada")
                            elif x["specs"] == "plate":
                                print("Tipo: comida preparada")
                        print("Precio: $",x["price_iva"],)
                        for z in stadiums:
                            z = vars(z)
    
                            if x["id_stadium"] == z["id_stadium"]:
                                print("Encuéntrala en el restaurante  ~",x["name_rest"],"~  en el",z["name"])
        print("\n")
        show_rests(products,stadiums)                          

    elif opc == "2":
        print("-- Búsqueda por tipo de producto --\n\n    1. Bebida\n    2. Comida\n\n    0. Regresar al menú de búsqueda")

        aux = input("\nElije una opción contenida en la lista: ")

        while aux != "1" and aux != "2" and aux != "0":
            aux = input("\nOpción inválida. Por favor elija una opción contenida en la lista: ")

        for x in products:
            x = vars(x)
            for key,value in x.items():

                if aux == "1":
                    if value == "beverages":
                        print("\n--",x["name"],"--")
                        
                        if x["specs"] == "alcoholic":
                            print("Tipo: bebida alcohólica")
                        elif x["specs"] == "non-alcoholic":
                            print("Tipo: bebida no alcohólica")
                        print("Precio: $",x["price_iva"],)
                        for z in stadiums:
                            z = vars(z)
        
                            if x["id_stadium"] == z["id_stadium"]:
                                print("Encuéntrala en el restaurante  ~",x["name_rest"],"~  en el",z["name"]) 
                    
                elif aux == "2":    
                    if value == "food":
                        print("\n--",x["name"],"--")
                        
                        if x["specs"] == "package":
                            print("Tipo: comida empacada")
                        elif x["specs"] == "plate":
                            print("Tipo: comida preparada")
                        print("Precio: $",x["price_iva"],)
                        for z in stadiums:
                            z = vars(z)
        
                            if x["id_stadium"] == z["id_stadium"]:
                                print("Encuéntrala en el restaurante  ~",x["name_rest"],"~  en el",z["name"])  
                
                elif aux == "0":
                    print("\n")
                    show_rests(products,stadiums)    
        print("\n")
        show_rests(products,stadiums)  
        
    elif opc == "3":
        print("-- Búsqueda por rango de precio --\n")
        min = int(input("Ingrese el límite inferior del precio: "))

        while str(min).isnumeric() == False or min < 0.0:
            min = int(input("Ingreso inválido. Por favor ingrese un valor numérico mayor a 0.00: "))

        if min > 40.6:
            print("\nNo hay productos disponibles en este rango de precios\n")
            show_rests(products,stadiums)

        max = int(input("Ingrese el límite superior del precio: "))

        while str(max).isnumeric() == False or max < 0.0:
            max = int(input("Ingreso inválido. Por favor ingrese un valor numérico mayor a 0.00: "))

        if max < 4.64:
            print("\nNo hay productos disponibles en este rango de precios\n")
            show_rests(products,stadiums)

        for x in products:
            x = vars(x)
        
            for key,value in x.items():
                
                    if key == "price_iva":
                        
                        if value > min and value < max:
                            
                            print("\n--",x["name"],"--")
                            if x["type"] == "beverages":
                                if x["specs"] == "alcoholic":
                                    print("Tipo: bebida alcohólica")
                                elif x["specs"] == "non-alcoholic":
                                    print("Tipo: bebida no alcohólica")
                            elif x["type"] == "food":
                                if x["specs"] == "package":
                                    print("Tipo: comida empacada")
                                elif x["specs"] == "plate":
                                    print("Tipo: comida preparada")
                            print("Precio: $",x["price_iva"],)
                            for z in stadiums:
                                z = vars(z)
        
                                if x["id_stadium"] == z["id_stadium"]:
                                    print("Encuéntrala en el restaurante  ~",x["name_rest"],"~  en el",z["name"])
        print("\n")
        show_rests(products,stadiums)                   
        
    elif opc == "0":
        return
            