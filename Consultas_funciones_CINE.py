import sqlite3
from sqlite3 import Error
from datetime import date

def create_connection(db_file):
  
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_fecha_nacimiento(conn,entrada):
   
    cur = conn.cursor()
    cur.execute(f"SELECT fecha_nac FROM usuario WHERE contrasenia={entrada}")

    row = cur.fetchone()              # OJO AQUI !!
    # print(row)   

    return row

def select_clasificacion(conn,nombre_peli):
    
    cur = conn.cursor()
    cur.execute(f"SELECT id_clasificacion FROM pelicula WHERE nombre={nombre_peli}")

    row = cur.fetchone()              # OJO AQUI !!
    # print(row)   

    return row

def select_clasificador(conn,id_clasificador):
    
    cur = conn.cursor()
    cur.execute(f"SELECT clasificador FROM clasificacion WHERE id_clasificacion={id_clasificador}")

    row = cur.fetchone()                  # OJO AQUI !!
    # print(row)   

    return row


def main():
    database = r"Cinemark.db"

    # create a database connection
    conn = create_connection(database)

    with conn:
                
                  
     entrada=input("Introduzca la contraseña del usuario que quiere hacer una reserva: ")
    # con esta contraseña voy a la tabla usuario y busco fecha_nac
     nacido=select_fecha_nacimiento(conn,entrada)        # viene como tupla
     
    # con esta fecha_nac corro edadActual
    
     def edadActual(nacido):
        #Esta funcion calcula la edad de una persona (en anios). Solo es necesario como parametro la fecha de nacimiento en formato: dd-mm-aaaa (lo toma de select_fecha_nacimiento(conn,entrada))
        hoy=date.today()   # ojo: aaaa-mm-dd !!
        anio_hoy=hoy.year
        mes_hoy=hoy.month
        dia_hoy=hoy.day
        nacido= ''.join(nacido)  #convierte la tupla en string dd-mm-aaaa
        nacimiento=nacido.split('-')  # convierte el string nacido en una lista de ['dd','mm','aaaa']
        dia_nac=nacimiento[0]  
        dia_nac=int(dia_nac)     # casteo
        mes_nac=nacimiento[1]
        mes_nac=int(mes_nac)     # casteo
        anio_nac=nacimiento[2]
        anio_nac=int(anio_nac)   # casteo
        if mes_hoy>mes_nac:
            anios=anio_hoy-anio_nac
        elif mes_hoy==mes_nac and dia_hoy>=dia_nac: 
            anios=anio_hoy-anio_nac               
        else:
            anios=anio_hoy-anio_nac-1
        
        return anios
    
    edad=edadActual(nacido)
    if edad>18:
        pass
    else:
        print("La edad del usuario es: ",edad, " anios")
      
    nombre_peli=input("Introduzca el nombre de la pelicula de la que quiere hacer reservas (entre comillas simples o dobles): ")
   
    id_clasificador=(select_clasificacion(conn,nombre_peli))[-1] # la tupla la convierto en string
    apto_para=(select_clasificador(conn,id_clasificador))[-1]

    if apto_para!="ATP":
        apto_para=int(apto_para[1:3])         # al string le saco el > y lo hago int
        if edad<=apto_para:
       
            print("Disculpe, no tiene edad para reservar esa pelicula")
            print("La pelicula: ",nombre_peli," es para mayores de ",apto_para)
        else:
            print("Continue con su reserva, tiene la edad permitida")
            
        
if __name__ == '__main__':
    main()
