####### objetos a crear -team -stadium -match

class Team:
    
    def __init__(self,id_team,name,fifa_code,group):
        
        self.id_team = id_team
        self.name = name
        self.fifa_code = fifa_code
        self.group = group

class Stadium:

    def __init__(self,id_stadium,location,name,cap,rests):

        self.id_stadium = id_stadium
        self.location = location
        self.name = name
        self.rests = rests
        self.cap = cap

class Match:

    def __init__(self,id_match,home,away,date,id_stadium):

        self.id_match = id_match
        self.home = home
        self.away = away
        self.date = date
        self.id_stadium = id_stadium

        
def partidos(teams,stadiums,matches):
    '''Muestra el menú de búsqueda y regresa la opción seleccionada por el usuario'''
    
    print("-- Búsqueda de partidos --\n\n    1. País\n    2. Estadio\n    3. Fecha\n\n    0. Regresar al menú principal\n")
    
    opc =input("Elija el criterio de búsqueda: ")

    while opc != "1" and opc != "2" and opc != "3" and opc != "0" or len(opc) == 0:
        opc = input("\nValor inválido. Por favor ingrese un valor numérico de 1 a 3: ")

    if opc == "1":
        print("\n")
        for i in teams:
            i = (vars(i))
            print(i["name"],"(",i["id_team"],")")

        opc_t= input("\nIngrese el número (n) del país que desea visualizar: ")

        while opc_t.isnumeric() == False or int(opc_t) < 1 or int(opc_t) > 32 or len(opc_t) == 0:
            opc_t = input("\nValor inválido. Por favor ingrese un valor numérico de 1 a 32: ")
        
        for x in teams:
            x = vars(x)
            if opc_t == x["id_team"]:
                opc_t = x["name"]
                
                for y in matches:
                    y = vars(y)
                    if opc_t == y["home"] or opc_t == y["away"]:
                        for z in stadiums:
                            z = vars(z)
                            if y["id_stadium"] == z["id_stadium"]:
                                
                                print("\n",y["home"],"vs.",y["away"],"- Localizador: (",y["id_match"],")\n\n    Fecha (mm/dd/aaaa) y hora:",y["date"],"\n    Estadio:",z["name"],"\n    Ubicación:",z["location"],"\n")
        print("\n")
        partidos(teams,stadiums,matches)
        
    elif opc == "2":
        print("\n")
        for i in stadiums:
            i = (vars(i))
            print(i["name"],"(",i["id_stadium"],")\n")

        opc_s = input("\nIngrese el número (n) del estadio que desea visualizar: ")

        while opc_s.isnumeric() == False or int(opc_s) < 1 or int(opc_s) > 8 or len(opc_s) == 0:
            opc_s = input("\nValor inválido. Por favor ingrese un valor numérico de 1 a 8: ")
    
        for x in stadiums:
            x = vars(x)
        
            if opc_s == str(x["id_stadium"]):
            
                for y in matches:
                    y = vars(y)
                     
                    if opc_s == str(y["id_stadium"]):
    
                        print("\n",y["home"],"vs.",y["away"],"- Localizador: (",y["id_match"],")\n\n    Fecha (mm/dd/aaaa) y hora:",y["date"],"\n    Estadio:",x["name"],"\n    Ubicación:",x["location"],"\n")

        print("\n")
        partidos(teams,stadiums,matches)
        
    elif opc == "3":
        print("\nNoviembre ( 11 )\nDiciembre ( 12 )")
        mes = input("\nIngrese el mes que desea visualizar: ")

        while mes != "11" and mes != "12" or len(mes) == 0:
            mes = input("\nValor inválido. Por favor ingrese un valor numérico de 11 a 12: ")
        
        dia = input("\nIngrese el día que desea visualizar: ")

        if mes == "11":
            while dia.isnumeric() == False or int(dia) < 20 or int(dia) > 30 or len(dia) == 0:
                dia = input("\nValor inválido. Por favor ingrese un valor numérico de 20 a 30: ")
        elif mes == "12":
            while int(dia) != 1 and int(dia) != 2 or len(dia) == 0:
                dia = input("\nValor inválido. Por favor ingrese un valor numérico de 1 a 2: ")

        opc_f = mes + "/" + dia +"/2022"

        for y in matches:
            y = vars(y)
            
            if opc_f in y["date"]:
                

                for x in stadiums:
                    x = vars(x)

                    if y["id_stadium"] == x["id_stadium"]:
                    
                        print("\n",y["home"],"vs.",y["away"],"- Localizador: (",y["id_match"],")\n\n    Fecha (mm/dd/aaaa) y hora:",y["date"],"\n    Estadio:",x["name"],"\n    Ubicación:",x["location"],"\n")      

        print("\n")
        partidos(teams,stadiums,matches)
        
    elif opc == "0":
        return