from functions import getapi
from partidos import Team
from partidos import Stadium
from partidos import Match
from rests import Product
from partidos import partidos
from entradas import entradas
from asistencia import asistencia
from rests import show_rests

#### obtención de data de la API
data_teams = getapi("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json")

data_stadiums = getapi("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json")

data_matches = getapi("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json")
####
#### creación de objetos Team, Stadium y Match, los cuales se organizan en listas

teams = []
stadiums = []
matches = []
clients = []
mapas=[0,0,0,0,0,0,0,0]
codes = []
products = []

for x in data_teams:
   
    for key, value in x.items():
        
        if key == "name":
            name = value
        elif key == "group":
            group = value
        elif key == "fifa_code":
            code = value
        elif key == "id":
            id_team = value

    t = Team(id_team,name,code,group)
    teams.append(t)

for y in data_stadiums:

    for key, value in y.items():
        
        if key == "id":
            id_stadium = value
        elif key == "name":
            name = value
        elif key == "capacity":
            cap = value
        elif key == "location":
            location = value
        elif key == "restaurants":
            rests = value
            
            for z in rests:
                for r_key,r_value in z.items():
                    if r_key == "name":
                        r_name = r_value
                    if r_key == "products":
                        for a in r_value:
                            for p_key,p_value in a.items():
                                if p_key == "name":
                                    if p_value == "Beer":
                                        p_name = "Cerveza"
                                    elif p_value == "Water":
                                        p_name = "Agua"
                                    elif p_value == "Hamburger":
                                        p_name = "Hamburguesa"
                                    elif p_value == "Fish and Chips":
                                        p_name = "Pescado con papas fritas"
                                    elif p_value == "Steak":
                                        p_name = "Filete"
                                    else:
                                        p_name = p_value
                                        
                                elif p_key == "quantity":
                                    p_quantity = p_value
                                elif p_key == "price":
                                    p_price = round((p_value*1.16),2)
                                elif p_key == "type":
                                    p_type = p_value
                                elif p_key == "adicional":
                                    p_specs = p_value

                            p = Product(id_stadium,rests.index(z),r_name,p_type,p_name,p_specs,p_price)
                            products.append(p)
        
    s = Stadium(id_stadium,location,name,cap,rests)
    stadiums.append(s)


for z in data_matches:

    for key, value in z.items():

        if key == "home_team":
            home = value
        elif key == "away_team":
            away = value
        elif key == "date":
            date = value
        elif key == "stadium_id":
            id_stadium = value
        elif key == "id":
            id_match = value

    for x in teams:
        
        if x.name == home:#referencia al objeto Team correspondiente#
            for y in stadiums:#referencia al objeto Stadium correspondiente#
                if y.id_stadium == id_stadium:
                    m = Match(id_match,x.name,away,date,y.id_stadium)
                    
        elif x.name == away:
            for y in stadiums:
                if y.id_stadium == id_stadium:
                    m = Match(id_match,home,x.name,date,y.id_stadium)

    matches.append(m)

def main():
    
    print("---- QATAR 2022 ----\n\n    1. Buscar información de los partidos\n    2. Comprar entradas\n    3. Validar código de entrada\n    4. Buscar información de productos\n    5. Venta de productos\n    6. Visualizar estadísticas\n")
    menu = input("Ingrese la opción que desee: ")

    while menu.isnumeric() == False or int(menu) not in range(1,7):
        menu = input("\nOpción inválida. Por favor ingrese una opción contenida en el menú: ")

    print("\n")
    
    if menu == "1":
        partidos(teams,stadiums,matches)
    elif menu == "2":
        entradas(clients,teams,stadiums,matches,mapas,codes)
    elif menu == "3":
        asistencia(codes)
    elif menu == "4":
        show_rests(products,stadiums)
    elif menu == "5":
        pass
    elif menu == "6":
        pass

    exit = input("\n¿Desea regresar al menú principal?\n\n    1. Sí\n    2. No (finalizar programa)\n\nIngrese una opción: ")

    while exit != "1" and exit != "2":
        exit = input("\nOpción inválida. Por favor ingrese una opción contenida en la lista: ")
    print("\n")
    if exit == "1":
        main()
    elif exit == "2":
        exit = input("\n¿Está seguro de que desea finalizar el programa?\n\n    1. Sí\n    2. No\n\nIngrese una opción: ")
        while exit != "1" and exit != "2":
            exit = input("\nOpción inválida. Por favor ingrese una opción contenida en la lista: ")

        if exit == "1":
            return
        elif exit == "2":
            print("\n")
            main()

main()
