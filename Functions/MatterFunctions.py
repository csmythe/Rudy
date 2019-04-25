from Functions import *

def listMatters(activeOnly = True):
   
    if activeOnly:
        where = ' WHERE Inactive = 0'
    else:
        where = ""
    
    q = """
    SELECT * FROM [NortonAbert].[dbo].MatterTypes {}
    """.format(where)
    
    CONN.connect()
    data = CONN.readData(q,[])
    CONN.closecnxn()
    
    return data

def checkValidMatterNumber(clientnum, matternum):
    q = "SELECT * FROM [NortonAbert].[dbo].ClientMatters WHERE ClientNum = ? AND MatterNum = ?"
    v = [str(clientnum),str(matternum)]
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    return len(data) > 0

def generateClientMatters(clientnum, include_deleted):
    q = """SELECT  cm.*, mt.matterdescr
            FROM [NortonAbert].[dbo].ClientMatters cm 
                LEFT JOIN [NortonAbert].[dbo].MatterTypes mt on cm.mattertypeid = mt.typeid 
            WHERE cm.ClientNum = ?"""
    if not include_deleted:
        q += " AND cm.[Delete] = 0"
    v = [str(clientnum)]
    
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    for r, i in enumerate(data.index):
        yield r, data.loc[i]


def get_client_matter(clientnum, matternum):
    q = """SELECT  cm.*, mt.matterdescr
                FROM [NortonAbert].[dbo].ClientMatters cm 
                    LEFT JOIN [NortonAbert].[dbo].MatterTypes mt on cm.mattertypeid = mt.typeid 
                WHERE cm.ClientNum = ? and cm.MatterNum = ?"""
    v = [str(clientnum), str(matternum)]

    CONN.connect()
    data = CONN.readData(q, v)
    CONN.closecnxn()
    return data.loc[0]


def nextMatterNum(clientNum):
    q = """
    SELECT MAX(CAST( MatterNum as INT)) +1 as next_matter
    FROM [NortonAbert].[dbo].ClientMatters
    WHERE ClientNum = ? 
    """
    v = [str(clientNum)]
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    if data.next_matter[0] is None:
        nextNum = '00'
    else:
        numForm = '00'
        number = str(data.next_matter[0])
        nextNum = numForm[:-len(number)]+number
    return nextNum
        
    

def findMatter(matternum):
    q = """SELECT cm.*, mt.matterdescr
            FROM [NortonAbert].[dbo].ClientMatters cm 
                INNER JOIN [NortonAbert].[dbo].MatterTypes mt on cm.mattertypeid = mt.typeid
            WHERE MatterNum = ?"""
    v = [str(matternum)]
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    return data

def generateAdverPartyList(clientnum,matternum):
    q = "SELECT * FROM [NortonAbert].[dbo].AdverseParties WHERE ClientNum = ? AND MatterNum = ?"
    v = [str(clientnum),str(matternum)]
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    for r, i in enumerate(data.index):
        yield r, data.loc[i]
        
def generateDocumentList(clientnum, matternum):
    q = "SELECT * FROM [NortonAbert].[dbo].OriginalDocuments WHERE ClientNum = ? AND MatterNum = ?"
    v = [str(clientnum),str(matternum)]
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    for r, i in enumerate(data.index):
        yield r, data.loc[i]