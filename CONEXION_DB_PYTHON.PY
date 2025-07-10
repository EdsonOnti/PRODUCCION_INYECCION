import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine

class ConexionDB:

    #Conexion requisitos 
    def __init__(self, host, user, password, database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.connection=None
        self.cursor=None
    
    #Funcion conexion

    
    def conectar(self):
        
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        return self.connection
    
    def insertar(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Datos insertados correctamente")
        except Error as e:
            print(f"Error al insertar datos: {e}") 

    
    def consulta(self,query,params=None):
        try:
            self.cursor.execute(query,params)if params else self.cursor.execute(query)
            if query.strip().lower().startswith("select"):
                return self.cursor.fetchall()
        except Error as e:
            print(f'Error al ejecutar la consulta {e}')
            return None
        
    def desconectar(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print('Conexion cerrada bye')
    
    def obtener_engine(self):
        """ Devuelve un motor SQLAlchemy para usar con pandas.to_sql() """
        url = f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}"
        return create_engine(url)

