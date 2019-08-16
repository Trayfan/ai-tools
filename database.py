import sqlite3


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
    
    def create(self, table_name):
        self.cursor.execute("CREATE TABLE " + table_name + 
                        """ (count integer, name text, lvl integer,
                        cost integer, price integer, nickname text)
                        """)

    def insert(self, table_name, data): 
        # data = [(0,'',0,0,0,'')] for example
        # table_name = 'Lots' for exampple
        self.cursor.executemany("INSERT INTO " + table_name +
                            " VALUES (?,?,?,?,?,?)", data)
        self.conn.commit()
    
    def update(self, table_name, column_name, column_set, where=''):
        self.cursos.execute("UPDATE " + table_name + " SET " +
                            column_name + " = '" + column_set +
                            "' WHERE " + where)
        self.conn.commit()
    
    def delete(self, table_name, where=''):
        self.cursos.execute("DELETE FROM " + table_name +
                            " WHERE " + where)
        self.conn.commit()

    
    def select(self, sql):
        # We use whole sql-select here
        self.cursor.execute(sql)
        return self.cursor.fetchall()
