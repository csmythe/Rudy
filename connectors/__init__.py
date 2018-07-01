import pypyodbc as odbc
import sqlite3, os

DEMO = 1

def demo(func):
    def initialize(*args, **kwargs): 
        conn = sqlite3.connect('NortonAbert.db')
        cursor = conn.cursor()
        tables = {'UserParam':['username TEXT',
                         'password TEXT',
                         'fullname TEXT',
                         'LastSignedIn DATE',
                         'Inactive INTEGER',
                         'Admin INTEGER'
                           ],
                  'OriginalDocuments':['ClientNum INTEGER',
                                       'MatterNum TEXT',
                                       'DocName TEXT',
                                       'EFileDir TEXT',
                                       'DocID INTEGER PRIMARY KEY'
                                       ],
                  'MatterTypes':['TypeID INTEGER PRIMARY KEY',
                                 'MatterDescr TEXT',
                                 'Inactive INTEGER'],
                  'ClientMatters':['ClientNum INTEGER',
                                   'MatterNum TEXT',
                                   'FirstName TEXT',
                                   'LastName TEXT',
                                   'MiddleInitial TEXT',
                                   'MatterTypeID INTEGER',
                                   'BillingAddr1 TEXT',
                                   'BillingAddr2 TEXT',
                                   'BillingCity TEXT',
                                   'BillingState TEXT',
                                   'BillingZip TEXT',
                                   'DateOpened DATE',
                                   'DateClosed DATE',
                                   'BoxNumber TEXT',
                                   'AttorneyInitials TEXT'
                                   ],
                  'ClientInfo':['ClientNum INTEGER',
                                'FirstName TEXT',
                                'LastName TEXT',
                                'MiddleInitial TEXT',
                                'Address1 TEXT',
                                'Address2 TEXT',
                                'City TEXT',
                                'State TEXT',
                                'ZipCode TEXT',
                                'Married INTEGER',
                                'SpouseFirstName TEXT',
                                'SpouseLastName TEXT',
                                'SpouseMiddleInitial TEXT',
                                'Phone1 TEXT',
                                'Phone2 TEXT',
                                'Email TEXT',
                                'DoNotRep INTEGER',
                                'Notes TEXT'],
                  'AdversParties':['ClientNum INTEGER',
                                   'MatterNum TEXT',
                                   'FirstName TEXT',
                                   'LastName TEXT'
                                   'MiddleName TEXT'
                                   'ReasonDescription TEXT'
                                   'PartyID INTEGER PRIMARY KEY']}
        for table in tables.keys():
            cols = ','.join(tables[table]).lower()
            userTable = "CREATE TABLE IF NOT EXISTS {} ({}) ".format(table,cols)
            cursor.execute(userTable)
            
        conn.commit()
        
        cursor.execute("SELECT * FROM UserParam WHERE username = 'Demo'")
        row = cursor.fetchone()
        
        if row is None:
            user = ['Demo','Demo','DemonstrationUser','2018-06-30','0','1']
            cursor.execute("INSERT INTO UserParam VALUES (?,?,?,?,?,?)",user)
            conn.commit()
            
        result = func(*args,**kwargs)
        return result
    return initialize