from os import replace
import accessBDD
import pandas

def CrearModelo():
    eliminarTablas()
    creartablas()
    cargartemporal()
    cargarmodelo()

def eliminarTablas():
    with open("scripts/deletetables.sql", 'r') as creaciontablas:
        query = creaciontablas.read()
        conexionCarga = accessBDD
        conexionCarga.ejecutarArchivo(query)

    strdesc = "se eliminaron las tablas del modelo"
    return [{"msg": True, "descripcion": strdesc}]

def creartablas():
    with open("scripts/tablas.sql", 'r') as creaciontablas:

        query = creaciontablas.read()
        conexionCarga = accessBDD
        conexionCarga.ejecutarArchivo(query)

    strdesc = "se crearon las tablas"
    return [{"msg": True, "descripcion": strdesc}]

def cargartemporal():
    df = pandas.read_csv('C:\Users\Sergio Felipe\Documents\USAC\Seminario2\Lab\songs_normalize.csv', delimiter=";", encoding='latin-1', dtype="string")
    print(df.index)
    val = 0
    for index, row in df.iterrows():
        val += 1
        query = getQuery(row, val)
        conexionCarga = accessBDD
        conexionCarga.sqlCarga(query)
    print("se cargaron ", val, " registros.")
    strdesc = "se cargaron {} registros".format(val)
    return [{"msg": True, "descripcion": strdesc}]

def getQuery(tmpRow, val):
    query = "insert into alldata (artist
	song,
	duration_ms,
	explicit,
	yearsong,
	popularity,
	danceability,
	energy,
	keysong,
	loudness,
	mode,
	speechiness,
	acousticness,
	instrumentalness,
	liveness,
	valence,
	tempo,
	genre) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(
tmpRow['NOMBRE_CLIENTE'],
tmpRow['CORREO_CLIENTE'],
tmpRow['CLIENTE_ACTIVO'],
tmpRow['FECHA_CREACION'],
tmpRow['TIENDA_PREFERIDA'],
tmpRow['DIRECCION_CLIENTE'],
tmpRow['CODIGO_POSTAL_CLIENTE'],
tmpRow['CIUDAD_CLIENTE'],
tmpRow['PAIS_CLIENTE'],
tmpRow['FECHA_RENTA'],
tmpRow['FECHA_RETORNO'],
tmpRow['MONTO_A_PAGAR'],
tmpRow['FECHA_PAGO'],
tmpRow['NOMBRE_EMPLEADO'],
tmpRow['CORREO_EMPLEADO'],
tmpRow['EMPLEADO_ACTIVO'],
tmpRow['TIENDA_EMPLEADO'],
tmpRow['USUARIO_EMPLEADO'],
tmpRow['CONTRASENA_EMPLEADO'],
tmpRow['DIRECCION_EMPLEADO'],
tmpRow['CODIGO_POSTAL_EMPLEADO'],
tmpRow['CIUDAD_EMPLEADO'],
tmpRow['PAIS_EMPLEADO'],
tmpRow['NOMBRE_TIENDA'],
tmpRow['ENCARGADO_TIENDA'],
tmpRow['DIRECCION_TIENDA'],
tmpRow['CODIGO_POSTAL_TIENDA'],
tmpRow['CIUDAD_TIENDA'],
tmpRow['PAIS_TIENDA'],
tmpRow['TIENDA_PELICULA'],
tmpRow['NOMBRE_PELICULA'],
tmpRow['DESCRIPCION_PELICULA'],
tmpRow['ANO_LANZAMIENTO'],
tmpRow['DIAS_RENTA'],
tmpRow['COSTO_RENTA'],
tmpRow['DURACION'],
tmpRow['COSTO_POR_DANO'],
tmpRow['CLASIFICACION'],
tmpRow['LENGUAJE_PELICULA'].strip(),
tmpRow['CATEGORIA_PELICULA'],
tmpRow['ACTOR_PELICULA'])
    query = query.replace("'-'", "NULL")
    return query


def cargarmodelo():
    with open("scripts/inserts.sql", 'r') as creaciontablas:

        query = creaciontablas.read()
        conexionCarga = accessBDD
        conexionCarga.ejecutarArchivo(query)

    strdesc = "se cargo informacion al modelo"
    return [{"msg": True, "descripcion": strdesc}]