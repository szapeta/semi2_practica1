import config
import psycopg2

def sqlSelect(valores, tabla, condiciones):
    connection = psycopg2.connect(
        user = config.USER, 
        password = config.PASSWORD, 
        host = config.HOST, 
        port = config.PORT, 
        database= config.DATABASE)
    cursor = connection.cursor()

    if(condiciones == ""):
        query = "SELECT "+valores+" FROM "+tabla
    else:
        query = "SELECT "+valores+" FROM "+tabla +  " where " + condiciones

    cursor.execute(query)
    r = [dict((cursor.description[i][0], value) \
            for i, value in enumerate(row)) for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return (r[0] if r else None) if False else r

def sqlSelectCustom(query):
    connection = psycopg2.connect(
        user = config.USER, 
        password = config.PASSWORD, 
        host = config.HOST, 
        port = config.PORT, 
        database= config.DATABASE)
    cursor = connection.cursor()

    if(query != ""):    
        cursor.execute(query)
        r = [dict((cursor.description[i][0], value) \
                for i, value in enumerate(row)) for row in cursor.fetchall()]
        cursor.close()
        connection.close()
    return (r[0] if r else None) if False else r

def sqlCarga(query):
    resp = False
    connection = psycopg2.connect(
        user=config.USER,
        password=config.PASSWORD,
        host=config.HOST,
        port=config.PORT,
        database=config.DATABASE)
    cursor = connection.cursor()
    if query != "":
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    resp = True
    return resp

def sqlDelete(query):
    resp = False
    connection = psycopg2.connect(
        user=config.USER,
        password=config.PASSWORD,
        host=config.HOST,
        port=config.PORT,
        database=config.DATABASE)
    cursor = connection.cursor()
    if query != "":
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    resp = True
    return resp

def ejecutarArchivo(sqlFile):
    resp = False
    connection = psycopg2.connect(
        user=config.USER,
        password=config.PASSWORD,
        host=config.HOST,
        port=config.PORT,
        database=config.DATABASE)
    cursor = connection.cursor()
    if sqlFile != "":
        cursor.execute(sqlFile)
        connection.commit()
        cursor.close()
        connection.close()
    resp = True
    return resp

