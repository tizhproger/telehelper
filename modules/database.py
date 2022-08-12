import psycopg2
from psycopg2 import Error

class DB:
    def __init__(self, db_name, address, db_port, login, password):
        try:
            conn = psycopg2.connect(database=db_name, user=login, password=password, host=address, port=db_port)
            curs = conn.cursor()
            self.connection = conn
            self.cursor = curs
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)


    #note functions
    def save(self, name, id, table):
        try:
            query = f"insert into {table} values ('{name}', {id})"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False


    def get(self, name, table):
        try:
            self.cursor.execute(f"select msg_id from {table} where name = '{name}'")
            res = self.cursor.fetchone()
            if not res is None:
                return res[0]
            else:
                return None
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return None
    
    def get_all(self, table):
        try:
            self.cursor.execute(f"select name from {table}")
            return self.cursor.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return None
    
    def noted(self, name, table):
        self.cursor.execute(f"select * from {table} where name='{name}';")
        user = self.cursor.fetchone()
        if user is None:
            return False
        else:
            return True
    

    def deln(self, name, table):
        try:
            self.cursor.execute(f"delete from {table} where name = '{name}'")
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False


    def del_all(self, table):
        try:
            self.cursor.execute(f"delete from {table};")
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False
    

    def add_user(self, id):
        try:
            query = f"insert into Allowed values ('{id}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False
    
    def all_users(self):
        try:
            self.cursor.execute(f"select id from Allowed")
            return self.cursor.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False
    

    def del_user(self, id):
        try:
            self.cursor.execute(f"delete from Allowed where id='{id}';")
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False
    

    def allowed(self, id):
        self.cursor.execute(f"select exists(select 1 from Allowed where id='{id}')")
        user = self.cursor.fetchone()
        return user[0]
        
        #self.cursor.execute(f"select * from Allowed where id='{id}';")
        #user = self.cursor.fetchone()
        #if not user is None:
        #    return True
        #else:
        #    return False


    def addword(self, word):
        try:
            query = f"insert into Banwords values ('{word}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL ", error)
            return False
    
    
    def delword(self, word):
        try:
            self.cursor.execute(f"delete from Banwords where word = '{word}';")
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL ", error)
            return False
    
    
    def checkword(self, word):
        self.cursor.execute(f"select exists(select 1 from Banwords where word='{word}')")
        data = self.cursor.fetchone()
        return data[0]
    
    
    def getwords(self):
        try:
            self.cursor.execute(f"select word from Banwords;")
            return self.cursor.fetchall()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False
    
    
    def checkmode(self, chat_id, mode_name):
        self.cursor.execute(f"select exists(select 1 from Modes where {mode_name}=true and chat_id = '{chat_id}')")
        data = self.cursor.fetchone()
        return data[0]
    
    
    def checkchat(self, chat_id):
        self.cursor.execute(f"select exists(select 1 from Modes where chat_id = '{chat_id}')")
        data = self.cursor.fetchone()
        return data[0]
        
    
    def addmode(self, chat_id, mode_name, state):
        try:
            query = f"select exists(select 1 from information_schema.columns where table_schema='public' and table_name='modes' and column_name='{mode_name}');"
            self.cursor.execute(query)
            if not self.cursor.fetchone()[0]:
                return False

            prepare = f"INSERT INTO Modes (chat_id) VALUES ('{chat_id}') ON CONFLICT (chat_id) DO UPDATE SET mutepolitics = false, autoban = false, autowarn = false;"
            self.cursor.execute(prepare)
            self.connection.commit()
    
            query = f"INSERT INTO Modes (chat_id, {mode_name}) VALUES ('{chat_id}', {state}) ON CONFLICT (chat_id) DO UPDATE SET {mode_name} = {state};"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL ", error)
            return False
    
    
    def getmodes(self, chat_id):
        try:
            self.cursor.execute(f"select * from Modes where chat_id = '{chat_id}';")
            return self.cursor.fetchone()
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False
