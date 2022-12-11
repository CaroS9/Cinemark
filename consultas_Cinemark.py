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

def select_all_usuarios(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario")

    rows = cur.fetchall()
    # print(rows)
    
    for row in rows:
        print(row)
      
def select_un_usuario(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario")           #  da los datos de la 1ra fila de la tabla usuario, NO CAMBIA EL * !!!
       
    row = cur.fetchone()                      # cambia fetchall por FETCHONE !!!
    return row              #

def select_un_usuario_segun_dni(conn,parametro):
   
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usuario WHERE dni={parametro}")
       
    row = cur.fetchone()                      # cambia fetchall por FETCHONE !!!
   
    return row              # Este return vuelve select_one_usuario(conn) una tuple
    
def select_un_usuario_segun_apellido(conn,parametro):
   
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usuario WHERE apellidos={parametro}")
     
    row = cur.fetchone()                      # cambia fetchall por FETCHONE !!!
   
    return row     
def select_dni_apellidos_usuario(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT dni,apellidos FROM usuario")          

    rows = cur.fetchall()                  # OJO AQUI !!    
    # print(rows)
    
    return rows   


def select_usuario_apellidos(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario ORDER BY apellidos ASC")          

    rows = cur.fetchall()                      
    # print(rows)
    for row in rows:
        print(row)
    
    return rows   

def select_all_usuario_by_condition(conn):         #  NOMBRE GENERICO PARA LAS CONSULTAS CONDICIONALES !!!
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE apellidos='Said'")          

    rows = cur.fetchall()                  # OJO AQUI !!    
    # print(rows)
   
    
    return rows

def select_all_titular_macro_(conn):       
   
    cur = conn.cursor()
    cur.execute("SELECT titular FROM tarjeta WHERE banco='Macro'")          

    rows = cur.fetchall()                  # OJO AQUI !!    
    # print(rows)
    for row in rows:
        print(row)
    
    return rows

def select_all_usuarios_apellidos_condicion(conn):       
   
    cur = conn.cursor()
    cur.execute("SELECT apellidos FROM usuario WHERE nombres LIKE'M%'")          

    rows = cur.fetchall()                  # OJO AQUI !!    
    # print(rows)
    for row in rows:
        print(row)
    
    return rows

def select_all_usuarios_apellidos_id_en_lista(conn):       
   
    cur = conn.cursor()
    cur.execute("SELECT apellidos,nombres FROM usuario WHERE id_usuario in (3,4,5,6)")          

    rows = cur.fetchall()                  # OJO AQUI !!    
    # print(rows)
    for row in rows:
        print(row)
    
    return rows

def select_all_usuarios_apellidos_id_en_conjunto(conn):       
    conjunto=(3,4,5,6)
    cur = conn.cursor()
    cur.execute (f"SELECT apellidos,nombres FROM usuario WHERE id_usuario in {conjunto}")          

    rows = cur.fetchall()                  # OJO AQUI !!    
    # print(rows)
    for row in rows:
        print(row)
    
    return rows


def select_descuento(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM descuento ")

    rows = cur.fetchall()              # OJO AQUI !!
    # print(rows)
    
    for row in rows:
        print(row)
    

    return rows

def select_descuento_jueves(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM descuento WHERE dia='Jueves'")

    row = cur.fetchone()              # OJO AQUI !!
    # print(row)   

    return row

def update_descuento(conn,descuento):
   
    
    sql = ''' UPDATE descuento
              SET porcentaje = ?
              WHERE id_descuento= ?'''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    print("Valor actualizado correctamente")


def update_usuario(conn, usuario):
   
    sql = ''' UPDATE usuario
              SET fecha_nac = ?
              WHERE id_usuario = ?'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    print("Valor actualizado correctamente")

def select_usuario_distintos(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM usuario")

    row = cur.fetchall()              # OJO AQUI !!
    # print(row)   

    return row

def select_max_y_min(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT MIN(porcentaje),MAX(porcentaje) FROM descuento")

    row = cur.fetchall()              # OJO AQUI !!
    # print(row)   

    return row

def select_usuario_dni(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario  WHERE dni LIKE '2%' and dni LIKE '%9'")           

    rows = cur.fetchall()              # OJO AQUI !!
    # print(row)   
    #for row in rows:
     #   print(row)

    return rows

def select_fecha_nacimiento(conn,entradadni):
   
    cur = conn.cursor()
    cur.execute(f"SELECT fecha_nac FROM usuario WHERE dni={entradadni}")

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
                
                   #-------SELECT de la tabla usuario ---------
    #    print("1. Consulta de todos los datos de todos los usuario de Cinemark")
    #   select_all_usuarios(conn)
        
    #    print("2. Consulta de los datos del primer usuario")
    #    print(select_un_usuario(conn))
        
    # print("3. Consulta de los datos del usuario a partir de su dni")
    # dni=int(input("Numero de documento? "))
    # print( select_un_usuario_segun_dni(conn,dni))
     
     
    # print("4. Consulta de los datos del usuario a partir de sus apellidos")  
     #apellidos=input("Apellidos? ")
     #print( select_un_usuario_segun_apellido(conn,apellidos))
       
      #  print("El tipo de usuario es: ",(select_one_usuario(conn)[5]))        
        
       #  print("3.Consulta de dni y apellido de usuario")
       # select_dni_apellidos_usuario(conn)
       #print( select_dni_apellidos_usuario(conn))
         
       #print("4.Consulta de todos los registros de los usuarios con apellido 'Said'")
       #select_all_usuario_by_condition(conn)
       #print( select_all_usuario_by_condition(conn))
       
       #print("5.Consulta de todos los registros de los usuarios ordenados alfabeticamente en orden ascendente")
       #select_usuario_apellidos(conn)
       #print (select_usuario_apellidos(conn))
       
      # print("6.los titulares de tarjestas del banco Macro que son usuarios")
       #select_all_titular_macro_(conn)
       
     # print("7.todos los apellidos de los usuarios cuyos  nombres comienzan con M")
     # select_all_usuarios_apellidos_condicion(conn)
     #print(len( select_all_usuarios_apellidos_condicion(conn)))                    #  !!! el largo de la consulta con len()
    #  print("8. Traer apellidos y nombres de usuario cuyos id estan en (3,4,5,6)")
    #  select_all_usuarios_apellidos_id_en_lista(conn)
      
    #print("9. Traer apellidos y nombres de usuario cuyos id estan en {conjunto}")
     #select_all_usuarios_apellidos_id_en_conjunto(conn)
     
    # print("10. Traer todos los descuentos")
    # select_descuento(conn)
    
    # print("11. Traer  descuento jueves")
     #print(select_descuento_jueves(conn)) 
     #id_jueves=select_descuento_jueves(conn)[0]
    # print(len(select_descuento_jueves(conn))) 
    #print(select_descuento_jueves(conn)[0]) 
    
                   #------UPDATE (actualizacion)-------
                   
    # print("12-Actualizacion del descuento  dado su id")
     #id_jueves=select_descuento_jueves(conn)[0]
     #nuevo_descuento=float(input("Introduzca un nuevo descuento entre 0.1 y 0.9: "))
     #update_descuento(conn, (nuevo_descuento, id_jueves))
     
    # !!! print("13. Variante del 12: el usuario elige un numer de (1,7) y el sistema le cambia el dto a ese dia")
    # !!! dias ={1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes", 6:"Sabado", 7:"Domingo"}
    # !!! dia_usuario = int(input("Coloca un numero entre 1 y 7: "))
    # !!!nuevo_descuento=float(input("Introduzca un nuevo descuento entre 0.1 y 0.9: "))
    # !!!update_descuento(conn, (nuevo_descuento, dia_usuario))
     
                   
    #print("14.Actualizacion de la fecha de nacimiento de un usuario dado su id")
    #update_usuario(conn, ("12-3-2005", 7))
    
    #print(15. Devuelve la cantidad de usuarios usando count(*) en la tabla usuario)
    # print(select_usuario_distintos(conn))   
       
    # print("16. Devuelve el MENOR y el MAYOR valor de la tabla descuento")
    #print(select_max_y_min(conn))
    
    #print("17. Devuelve los datos de los usuarios cuyos dni comienzan con 2 y terminan en 9")
    # print(select_usuario_dni(conn))
   #!!!  entradadni=input("Introduzca el dni del usuario que quiere hacer una reserva: ")
    # print(f"Actualizacion de la tabla reserva con previo control de la edad del usuario a traves de dni={entradadni} para corroborar su aptitud para comprar las entradas segun la pelicula que quiere reservar.")
     
    # con este dni voy a la tabla usuario y busco fecha_nac
 #!!!   nacido=(select_fecha_nacimiento(conn,entradadni))         # viene como tupla
     
    # con esta fecha_nac corro edadActual
    
 
"""  def edadActual(nacido):
        #Esta funcion calcula la edad de una persona (en anios). Solo es necesario como parametro la fecha de nacimiento en formato: dd-mm-aaaa (lo toma de select_fecha_nacimiento(conn,entradadni))
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
   # print("La edad del usuario es: ",edadActual(nacido), " anios")
    
    #if edadActua
    
    
    nombre_peli=input("Introduzca el nombre de la pelicula de la que quiere hacer reservas (entre comillas simples o dobles): ")
   # print(select_clasificacion(conn,nombre_peli))
    id_clasificador=(select_clasificacion(conn,nombre_peli))[-1] # la tupla la convierto en string
    apto_para=(select_clasificador(conn,id_clasificador))[-1]
   # print("La pelicula: ",nombre_peli," es para ",apto_para)
    if apto_para!="ATP":
        apto_para=int(apto_para[1:3])         # al string le saco el > y lo hago int
        if edad<=apto_para:
       # if edadActual(nacido)<=apto_para:
            print("Disculpe, no tiene edad para reservar esa pelicula")
            print("La pelicula: ",nombre_peli," es para mayores de ",apto_para)
        else:
            print("Continue con su reserva, tiene la edad permitida")
            
    #else:
     #   print("Continue con su reserva")
    #print(apto_para)
    #print(type(select_clasificacion(conn,nombre_peli)))
    #print(select_clasificador(conn,id_clasificacion))"""
    
    
if __name__ == '__main__':
    main()
