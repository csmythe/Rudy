from connectors import *
from pandas.io.sql import read_sql

class Target:
    driver = '{SQL Server}'
    server = r'App1\SQLEXPRESS'
    # driver = '{ODBC Driver 17 for SQL Server}'
    # server = r'system76-pc'
    # server = 'DESKTOP-QGM6LRE\SQLEXPRESS'
    username = 'nortUser'
    pwd = 'nortPassword123'
    database = 'NortonAbert'

class Connection:
    
    is_closed = True
    
    def connect(self, auto_commit = True):
        
        
        if not self.is_closed:
            self.closecnxn()
            
        if DEMO == 1:
            self.cnxn = sqlite3.connect(Target.database)
        else:
            string = "DRIVER="+Target.driver+";SERVER="+Target.server+";DATABASE="+Target.database+";UID="+Target.username+";PWD="+Target.pwd
            self.cnxn = odbc.connect(string,autocommit = auto_commit)
        
    def closecnxn(self):
        self.is_closed = True
        self.cnxn.close()
        
    def writeData(self,query,params):
        
        if self.is_closed == True:
            self.connect()
            
        cursor = self.cnxn.cursor()
        
        query = query
        result = cursor.execute(query,params)
        
        cursor.close()
        self.cnxn.commit()
        return result
        
    def readData(self,query,params = []):
        if self.is_closed == True:
            self.connect()
        
        query = query
        data = read_sql(query,self.cnxn, params = params)
        self.cnxn.cursor().close()
        return data
    
    def saveData(self,data):
        action = data['action']
        if action == 'new':
            q = "INSERT INTO "+data['table']+" ("
            qa = []
            qb = []
            vals = []
            
            for key in data['values'].keys():
                qa.append(key)
                qb.append("?")
                vals.append(str(data['values'][key]))
                
            q += ",".join(qa) + ") VALUES ("
            q += ",".join(qb) +")"
            
        elif action == 'update':
            q = "UPDATE " + data['table'] +" SET "
            qa = []
            vals = []
            for key in data['values'].keys():
                qa.append(str(key) + " = ?")
                vals.append(str(data['values'][key]))
                
            q += ",".join(qa)
            
            qb = []
            for key in data['params'].keys():
                qb.append(str(key)+ " = ?")
                vals.append(str(data['params'][key]))
            q += " WHERE "+ " AND ".join(qb)
            
            
        elif action == 'delete':
            q = "DELETE FROM "+data['table']+" WHERE " + " AND ".join([str(key)+ " = ?" for key in data['params'].keys()])
            
            vals = [str(data['params'][key]) for key in data['params'].keys()]
        
        return self.writeData(q,vals)


if __name__ == '__main__':
    conn = Connection()
    conn.connect()
    conn.closecnxn()