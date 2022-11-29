import itertools as it
from functions import random_code

#clases cliente y ticket


class Client:

    def __init__(self,name,id_client,age,match,vip):

        self.name = name
        self.id_client = id_client
        self.age = age
        self.match = match
        self.vip = vip

def maps(filas,columnas):
    mapa = []
    for y in range(filas):
        y_mapa = []
        for x in range(columnas):
            y_mapa.append(False)

        mapa.append(y_mapa)
    return mapa

def show_map(mapa):

    print("* "*(len(mapa[1])-1) + " ESTADIO " + " *" * (len(mapa[1])-1))
    print("\n")

    nums = "   "

    for i,x in enumerate(mapa[1]):
        if i > 8:
            nums += str(i+1)+ " |"
        else:
            nums +=" " + str(i+1) + " |"

    print(nums)

    for i,x in enumerate(mapa):

        if i > 8:
            aux = str(i+1)
        else:
            aux = str(i+1) + " "

        for y in x:
            if y == True:
                aux += "| X "
            else:
                aux += "|   "

        print("   "+"-"*len(mapa[1]*4))
        print(aux)
    
   

def show_ticket(vip,id_client):
    '''Recibe el valor vip y el id del cliente, muestra la factura de dicho cliente'''
    print("\nMonto a pagar:")

    if vip == "1":
        cost = 120.00
        print("\nSubtotal: $",cost)
    elif vip == "2":
        cost = 50.00
        print("\nSubtotal: $",cost)

    if isvamp(int(id_client)) == True:
        discount = cost*0.15
        print("¡Ha obtenido un descuento de 15%!\nDescuento: -",discount)
    else:
        discount = 0.00
        print("Descuento: - $",discount)

    iva = (cost-discount)*0.16
    print("16% - IVA: $",iva)

    print("Total: $",(cost-discount)+iva)


def vamp(num_str):
    '''recibe un entero que debe cumplir los requisitos para tener posibilidad de ser vampiro, regresa True si es vampiro y False si no lo es'''
    num_iter = it.permutations(num_str, len(num_str))
    for num_list in num_iter:
        v = ''.join(num_list)
        x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
        if x[-1] == '0' and y[-1] == '0':
            continue
        if int(x) * int(y) == int(num_str):
            return True
    return False

def isvamp(m_int):
    '''recibe un entero cualquiera, retorna True si es vampiro y False si no lo es'''
    n_str = str(m_int)
    
    if len(n_str) % 2 == 1:
        return False
    
    x = vamp(n_str)
   
    if not x:
        return False
    
    return True

def pick_seat(clientes,matches,stadiums,mapas,codes):

    if len(mapas) == 0:
        mapas=[0,0,0,0,0,0,0,0]
    
    for x in clientes:##shows map and registers the seat they want to take
        x = vars(x)
        for y in matches:
            y = vars(y)
            if x["match"] == y["id_match"]:
            
                for z in stadiums:
                    z = vars(z)
                    if y["id_stadium"] == z["id_stadium"]:

                        if mapas[(z["id_stadium"]) - 1] == 0:
                            mapas[(z["id_stadium"]) - 1] = maps(z["cap"][0],z["cap"][1])
                            
                        mapa = mapas[(z["id_stadium"]) - 1]
                        
                        show_map(mapa)
    
                        fila = input("\nSeleccione la fila en la que desea estar: ")
                        while int(fila) > z["cap"][0] or int(fila) < 1:
                            fila = input("\nValor fuera de rango. Ingrese un valor válido: ")
                            
                        columna = input("\nSeleccione la columna en la que desea estar: ")
                        while int(columna) > z["cap"][1] or int(columna) < 1:
                            columna = input("\nValor fuera de rango. Ingrese un valor válido: ")
                        
                        while mapa[int(fila)-1][int(columna)-1] == True:

                            a = mapa[int(fila)-1][int(columna)-1]

                            show_map(mapa)
                            print("\nEste asiento está ocupado. Por favor escoja otro asiento: ")
                            
                            
                            fila = input("\nSeleccione la fila en la que desea estar: ")
                            while int(fila) > z["cap"][0] or int(fila) < 1:
                                fila = input("\nValor fuera de rango. Ingrese un valor válido: ")

                            columna = input("\nSeleccione la columna en la que desea estar: ")
                            while int(columna) > z["cap"][1] or int(columna) < 1:
                                columna = input("\nValor fuera de rango. Ingrese un valor válido: ")
                            b = mapa[int(fila)-1][int(columna)-1]
                                
                            if a != b:
                                break

                        print("\nAsiento: ",int(fila),"-",int(columna),"\n")
                        show_ticket(x["vip"],x["id_client"])
                    
                        buy = input("\n¿Desea adquirir esta entrada?\n\n    1. Sí\n    2. No\n\nIngrese el número correspondiente a su respuesta: ")
                    
                        while buy != "1" and buy != "2":
                            buy = input("\nValor inválido. Ingrese un numero del 1 al 2: ")
                    
                        if buy == "1":

                            mapa[int(fila)-1][int(columna)-1] = True
                            mapas[(z["id_stadium"]) - 1] = mapa
                            code = random_code(8)
                            codes.append(code)
                            print("\n\nPago procesado exitosamente\n¡Gracias por su compra!\n")
                            print("Fecha:",y["date"],"\nEstadio:",z["name"],"\nUbicación:",z["location"],"\nAsiento: ",int(fila),"-",int(columna))
                            if x["vip"] == "1":
                                print("\nTipo: VIP")
                            elif x["vip"] == "2":
                                print("\nTipo: general")
                                  
                            print("\nLocalizador: ",code,"\n\nDEBE PRESENTAR EL LOCALIZADOR EN LA ENTRADA DEL ESTADIO.\n")
                            
                            return mapas,codes

                        elif buy == "2":
                            return mapas,codes
                            
def client_menu(teams,stadiums,matches):
    '''shows user data menu, returns registered data as an object class client'''
    print("\n-- Ingreso de datos --\n\n")

    name = input("    Ingrese su nombre completo: ")

    while name.replace(' ','').isalpha() == False or len(name) == 0:
        print("\nIngreso inválido. Su nombre solo puede contener letras.\n")
        name = input("    Ingrese su nombre completo: ")
    
    id_cliente = input("\n    Ingrese su cédula de identidad: ")

    while id_cliente.isnumeric() == False or len(id_cliente) == 0:
            print("\nIngreso inválido. Su cédula solo puede contener números.\n")
            id_cliente = input("    Ingrese su cédula de identidad: ")
    
    age = input("\n    Ingrese su edad en números: ")

    while age.isnumeric() == False or len(age) == 0 or int(age) < 14 or int(age) > 110:
        print("\nIngreso inválido. Su edad solo puede contener números desde el 14 hasta el 110 .\n")
        age = input("    Ingrese su edad: ")
    
    print("\n\n-- Información de los partidos --")
        
    for y in matches:
            y = vars(y)
            
            for x in stadiums:
                x = vars(x)

                if y["id_stadium"] == x["id_stadium"]:
                    print("\n",y["home"],"vs.",y["away"],"- Localizador: (",y["id_match"],")\n\n    Fecha (mm/dd/aaaa) y hora:",y["date"],"\n    Estadio:",x["name"],"\n    Ubicación:",x["location"],"\n")
                        
    id_match = input("\n    Ingrese el localizador del partido para el cuál desea adquirir un ticket: ")

    while id_match.isnumeric() == False or int(id_match) < 1 or int(id_match) > 48 or len(id_match) == 0:
            print("\nIngreso inválido. El localizador solo puede contener números entre del 1 al 48.\n")
            id_match = input("    Ingrese el localizador del partido para el cuál desea adquirir un ticket: ")

    vip = input("\n- Entradas disponibles -\n\n        1. VIP ($120)\n        2. General ($50)\n\n    Ingrese el número correspondiente al tipo de entrada que desea adquirir: ")

    while vip != "1" and vip != "2":
            print("\nIngreso inválido. El tipo de entrada solo puede ser un número del 1 al 2.\n")
            vip = input("    Ingrese el número correspondiente al tipo de entrada que desea adquirir: ")

    cl = Client(name,id_cliente,age,id_match,vip)

    return cl

def entradas(clientes,teams,stadiums,matches,mapas,codes):

    clientes.append(client_menu(teams,stadiums,matches))
    print("\n")

    mapas,codes = pick_seat(clientes,matches,stadiums,mapas,codes)

    return mapas,codes
