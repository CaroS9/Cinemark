import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """creando la conexion a Cinemark.db"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)

    return conn


def create_usuario(conn, usuario):
    
    sql = ''' INSERT INTO usuario(dni,apellidos,nombres,fecha_nac,tipo_usuario,email,contrasenia)
              VALUES(?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    return cur.lastrowid

def create_sala(conn, sala):
   

    sql = ''' INSERT INTO sala(nombre,formato,capacidad)
              VALUES(?,?,?)'''
                    
    cur = conn.cursor()
    cur.execute(sql, sala)
    conn.commit()
    return cur.lastrowid

def create_butaca(conn, butaca):
    
    sql = ''' INSERT INTO butaca(fila, numero, reserva, id_sala)
              VALUES(?,?,?,?) '''
              
    cur = conn.cursor()
    cur.execute(sql, butaca)
    conn.commit()
    return cur.lastrowid

def create_tarjeta(conn, tarjeta):
   

    sql = ''' INSERT INTO tarjeta(numero,banco,titular,fecha_cad,cod_seg,id_usuario)
              VALUES(?,?,?,?,?,?)'''
                    
    cur = conn.cursor()
    cur.execute(sql, tarjeta)
    conn.commit()
    return cur.lastrowid

def create_descuento(conn, descuento):
   

    sql = ''' INSERT INTO descuento(dia,porcentaje)
              VALUES(?,?)'''
                    
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    return cur.lastrowid

def create_tipopelicula(conn, tipopelicula):
   
    sql = ''' INSERT INTO tipopelicula(formato, idioma, subtitulada)
            VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tipopelicula)
    conn.commit()
    return cur.lastrowid

def create_clasificacion(conn, clasificacion):
   
    sql = ''' INSERT INTO clasificacion(clasificador, descripcion)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, clasificacion)
    conn.commit()
    return cur.lastrowid

def create_genero(conn, genero):
   
    sql = ''' INSERT INTO genero(tipo_genero)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, genero)
    conn.commit()
    return cur.lastrowid


def create_pelicula(conn, pelicula):
   
    sql = ''' INSERT INTO pelicula(nombre, director,reparto,pais,anio_estreno, sinopsis, duracion,id_genero, id_clasificacion,id_tp)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pelicula)
    conn.commit()
    return cur.lastrowid

def create_sesion(conn, sesion):
   
    sql = ''' INSERT INTO sesion(fecha, hora, id_sala, id_pelicula)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, sesion)
    conn.commit()
    return cur.lastrowid

def create_reserva(conn, reserva):
  
    sql = ''' INSERT INTO reserva(precio, fecha, id_usuario, id_sesion, id_butaca, id_descuento,id_tarjeta)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, reserva)
    conn.commit()
    return cur.lastrowid



def insert_data(database):

    usuarios=[
        [26521489,"Saal","Nilda","16-12-2005","Administrador","saaa@gmail.com","Mbn89976"],
        [27821489,"Said","Marta Alicia","6-11-2008","Cliente","maaa@gmail.com","SSn89976"],
        [34521489,"Martinez","Juan","3-2-2005","Administrador","maraa@gmail.com","mpn88976"],
        [44521489,"Perez Santillan","Juan Jose","15-5-2005","Cliente","jujo@gmail.com","jUjo9976"],
        [33521489,"Wallpa","Ilda Jorgelina","23-12-2000","Cliente","jorw@gmail.com","Mbn15976"],
        [32521489,"Martin","Jorge Alberto","7-7-1995","Cliente","jja@gmail.com","JJa69976"],
        [26678489,"Said","Jose Luis","12-3-21970","Cliente","jjsh@Hotmail.com","55JSh976"],
        [33321489,"Esteban","Maria Luisa","12-12-2000","Cliente","lmes@hotmail.com","MlEh9976"],
        [16521499,"Jorge","Alberto Jose","5-5-1967","Cliente","jaaa@gmail.com","6785jBte"],
        [35465768,"Saal","Juan","16-12-1998","Cliente","saju@gmail.com","mNbV4569"]
    ]
    
    salas=[
      ["sala_1","2D",10],
      ["sala_2","4D",10],
      ["sala_3","4D",10],
      ["sala_super","3D",10],
      ["sala_premium","4D",5]
    ]    
        
    butacas = [
        # sala_1
        ["A", 1, "Si", 1],
        ["A", 2, "Si", 1],
        ["A", 3, "No", 1],
        ["A", 4, "No", 1],
        ["A", 5, "No", 1],
        ["B", 1, "No", 1],
        ["B", 2, "No", 1],
        ["B", 3, "No", 1],
        ["B", 4, "No", 1],
        ["B", 5, "No", 1],
        # sala_2
        ["A", 1, "Si", 2],
        ["A", 2, "Si", 2],
        ["A", 3, "Si", 2],
        ["A", 4, "Si", 2],
        ["A", 5, "No", 2],
        ["B", 1, "No", 2],
        ["B", 2, "No", 2],
        ["B", 3, "No", 2],
        ["B", 4, "No", 2],
        ["B", 5, "No", 2],
        # sala_3
        ["A", 1, "No", 3],
        ["A", 2, "No", 3],
        ["A", 3, "Si", 3],
        ["A", 4, "No", 3],
        ["A", 5, "No", 3],
        ["B", 1, "No", 3],
        ["B", 2, "No", 3],
        ["B", 3, "No", 3],
        ["B", 4, "No", 3],
        ["B", 5, "No", 3],
        # sala_super
        ["A", 1, "No", 4],
        ["A", 2, "No", 4],
        ["A", 3, "Si", 4],
        ["A", 4, "No", 4],
        ["A", 5, "No", 4],
        ["B", 1, "No", 4],
        ["B", 2, "Si", 4],
        ["B", 3, "No", 4],
        ["B", 4, "No", 4],
        ["B", 5, "No", 4],
        # sala_premium
        ["A", 1, "Si", 5],
        ["A", 2, "Si", 5],
        ["A", 3, "Si", 5],
        ["A", 4, "Si", 5],
        ["A", 5, "Si", 5]
        
    ]

    tarjetas=[
       [9876543488870099,"Macro","ALBERTO J JORGE","20-12-25",456,16521499],
       [1234543488870099,"Nacion","ALBERTO J JORGE","2-12-24",100,16521499],
       [9988588488809099,"Noroeste","NILDA SAAL","20-10-23",432,26521489],
       [8888543488870099,"Macro","JOSE LUIS SAID","26-12-25",456,26678489],
       [9777743488870099,"Macro","MARTA A SAID","20-10-25",356,27821489],
       [1212143488870099,"Nacion","JORGE A MARTIN","22-12-24",366,32521489],
       [5556543488870099,"Macro","MARIA LUISA ESTEBAN","20-12-25",444,33321499],
       [7777543488870099,"Nacion","MARIA LUISA ESTEBAN","20-7-26",458,33321499],
       [9876555570070099,"Macro","JUAN MARTINEZ","15-12-25",946,34521489],
       [3333543488870099,"Santander","JUAN SAAL","20-11-25",456,35465768],
       [9876543488870022,"Macro","JUAN J PEREZ S","10-12-25",116,44521489],
       [9877743488870099,"Nacion","JUAN J PEREZ S","4-12-27",956,16521499],
       [6543212345678987,"Huala","ILDA J WALLPA","10-10-26",121,23156478]
    ]
    
    descuentos=[
       ["Lunes",0.25],
       ["Martes",0.5],
       ["Miercoles",0.25],
       ["Jueves",0.50],
       ["Viernes",0],
       ["Sabado",0],
       ["Domingo",0]
    ]
    
    tipopeliculas = [
        ['2D', "Ingles", "Si"],
        ['2D', "Ingles", "Si"],
        ["2D", "Ingles", "No"],
        ['3D', "Español", "No"],
        ["3D", "Ingles", "Si"],
        ["3D", "Ingles", "No"],
        ["4D", "Español", "No"],
        ["4D", "Ingles", "No"],
        ["4D", "Ingles", "Si"]
    ]
    
    clasificaciones= [
        [">18", "Violencia,drogas y sexo"],
        [">16", "Violencia moderada y sexo"],
        [">13", "Violencia leve"],
        ["ATP",  "Para la familia"]
    ]
    
    generos=[
             ["Accion"],
             ["Ciencia ficcion"],
             ["Drama historico"],
             ["Comedia y sexo"],
             ["Romantica"],
          #   ["Amor y drama"]
             ["Policial"],
             ["Terror"],
             ["Dibujos animados"]
                    
    ]
    
    peliculas=[
        ["El Padrino", "Francis Ford Coppola","Marlon Brando y Al Pacino","EEUU",1972,"La historia, ambientada desde 1945 a 1955, cuenta las crónicas de la familia Corleone liderada por Vito Corleone (Brando), enfocándose en el personaje de Michael Corleone (Pacino), y su transformación de un reacio joven ajeno a los asuntos familiares a un implacable jefe de la mafia ítalo-estadounidense.",175,1,1,1],
        ["Contacto", "Robert Zemeckis", "Jodie Foster, Letan Matthew, McConaughey y David Morse","EEUU",1997,"La protagonista del film, la Dra. Eleanor Arroway, una científica del SETI que encuentra pruebas fehacientes de vida extraterrestre es elegida para tomar contacto por primera vez.",150, 2,4,1],
        ["Everest", "Baltasar Kormákur", "Jason Clarke, Josh Brolin, John Hawkes, Robin Wright y Michael Kelly","EEUU",2015,"Narra la tragedia ocurrida en el monte Everest el 10 de mayo de 1996, en la que ocho alpinistas fallecieron debido a una tormenta.",121,3,3,1],
        ["Historia de amor", "Artur Hiller", "Ali MacGraw y Ryan O'Neal","EEUU",1970, "Oliver Barret IV es un gran deportista y estudiante que proviene de una familia acomodada.La vida de Oliver cambia cuando conoce a Jennifer Cavilleri, una extrovertida e interesante estudiante de música. En contra de la voluntad del padre de Oliver, los dos deciden casarse. La pareja enfrenta serios problemas económicos y con el apoyo de Jenny quien trabaja como maestra en una escuela privada, Oliver logra cursar la carrera de leyes.Cuando deciden tener un bebé, consultan a un especialista, quien después de practicarle varias pruebas a Jenny le informa a Oliver que su esposa está gravemente enferma y desahuciada.",99,5,4,1],
        ["La lista de Schindler","Steven Spielberg","Liam Neeson, Ralph Fiennes y Ben Kingsley","EEUU",1993,"En Cracovia, durante la Segunda Guerra Mundial, las tropas alemanas de ocupación han forzado a los judíos polacos a vivir recluidos en un gueto. El empresario Oskar Schindler (Liam Neeson), de etnia alemana y miembro del Partido Nazi, tomo todo el dinero que tenía y destinarlo a salvar esas vidas de los prisioneros judios",195,3,1,1]
    ]
    
    sesiones= [
        ["01-12-2022", "12:00", 1, 1],
        ["01-12-2022", "15:00", 1, 1],
        ["01-01-2022", "18:00", 1, 1],
        ["01-01-2022", "21:00", 1, 5],
        ["01-12-2022", "12:00", 2, 2],
        ["01-12-2022", "15:00", 2, 2],
        ["01-01-2022", "18:00", 2, 2],
        ["01-01-2022", "21:00", 2, 5],
        ["01-12-2022", "12:00", 3, 3],
        ["01-12-2022", "15:00", 3, 3],
        ["01-01-2022", "18:00", 3, 3],
        ["01-01-2022", "21:00", 3, 5],
        ["01-12-2022", "12:00", 4, 4],
        ["01-12-2022", "15:00", 4, 4],
        ["01-01-2022", "18:00", 4, 4],
        ["01-01-2022", "21:00", 4, 5]
        
    ]
    # precio, fecha, id_sesion, id_butaca, id_usuario,id_descuento, id_tarjeta
    reservas = [
        [500, "01-01-2022", 1, 1, 9, 1, 1],
        [500, "01-01-2022", 1, 2, 9, 1, 1],
        [500, "01-01-2022", 2, 1, 2, 1, 5],
        [500, "01-01-2022", 2, 2, 2, 1, 5],
        [500, "01-01-2022", 3, 1, 10, 1, 10],
        [500, "01-01-2022", 3, 2, 10, 1, 10],
        [500, "01-01-2022", 4, 1, 5, 1, 13],
        [500, "01-01-2022", 4, 2, 5, 1, 13],
        [500, "01-01-2022", 5, 3, 5, 1, 13],
        [500, "01-01-2022", 5, 4, 5, 1, 13]
       
    ]
    
   # create a database connection
    conn = create_connection(database)
    with conn:
      
        # create a new usuario
        for usuario in usuarios:
            create_usuario(conn, usuario)
            
         # create a new sala
        for sala in salas:
            create_sala(conn, sala)
            
        
        # create a new butaca
        for butaca in butacas:
            create_butaca(conn, butaca)

        # create a new tarjeta
        for tarjeta in tarjetas:
            create_tarjeta(conn, tarjeta)
            
         # create a new descuento
        for descuento in descuentos:
            create_descuento(conn, descuento)

         # create a new tipopelicula
        for tipopelicula in tipopeliculas:
            create_tipopelicula(conn, tipopelicula)
        
        # create a new clasificacion
        for clasificacion in clasificaciones:
            create_clasificacion(conn, clasificacion)        

          # create a new genero
        for genero in generos:
            create_genero(conn, genero)   
                   
          # create a new pelicula
        for pelicula in peliculas:
            create_pelicula(conn, pelicula)

        # create a new sesion
        for sesion in sesiones:
            create_sesion(conn, sesion)

        # create a new reserva
        for reserva in reservas:
            create_reserva(conn, reserva)

        

        print("Insercion realizada !")   

if __name__ == '__main__':
         #main()
   insert_data("Cinemark.db")
    