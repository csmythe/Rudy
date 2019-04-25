from Functions import *

def validateUserChange(username):
    
    q = """ 
    SELECT (SELECT COUNT(username) userck FROM [NortonAbert].[dbo].UserParam WHERE username = ?) as usrchk
        , (SELECT COUNT(1) admins FROM [NortonAbert].[dbo].UserParam WHERE Admin = 1 AND Inactive = 0) as admchk
        , (SELECT COUNT(1) as actives FROM [NortonAbert].[dbo].UserParam WHERE Inactive = 0) inactivechk
    
    """
    v = [username]
    
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    return data

def getUserList(activeOnly = True):
    if activeOnly:
        where = ' WHERE Inactive = 0 '
    else:
        where = ''
    q = "SELECT * FROM [NortonAbert].[dbo].UserParam {} ".format(where)
    
    CONN.connect()
    data = CONN.readData(q,[])
    CONN.closecnxn()
    
    return data

def cleanOutDeletedAccounts(cutoffDate):
    
    q = """
    SELECT ClientNum
    FROM [NortonAbert].[dbo].ClientInfo
    WHERE Deleted = 1 AND DeleteDate <= ?
    """
    v = [str(cutoffDate)]
    
    q1 = "DELETE FROM [NortonAbert].[dbo].OriginalDocuments WHERE ClientNum = ?"
    q2 = "DELETE FROM [NortonAbert].[dbo].ClientMatters WHERE ClientNum = ?"
    q3 = "DELETE FROM [NortonAbert].[dbo].ClientInfo WHERE ClientNum = ?"
    q4 = "DELETE FROM [NortonAbert].[dbo].AdverseParties WHERE ClientNum = ?"
    CONN.connect()
    data = CONN.readData(q,v)
    
    for i in data.index:
        clientnum = [str(data.clientnum[i])]
        CONN.writeData(q1,clientnum)
        CONN.writeData(q2,clientnum)
        CONN.writeData(q3,clientnum)
        CONN.writeData(q4,clientnum)


def cleanout_deleted_matters(cutoff_date):
    q = """
    SELECT ClientNum, MatterNum
    FROM [NortonAbert].[dbo].[ClientMatters]
    WHERE [Delete] = 1 AND DeleteDate <= ?
    """
    v = [str(cutoff_date)]

    q1 = "DELETE FROM [NortonAbert].[dbo].OriginalDocuments WHERE ClientNum = ? AND MatterNum = ?"
    q2 = "DELETE FROM [NortonAbert].[dbo].ClientMatters WHERE ClientNum = ? AND MatterNum = ?"
    q3 = "DELETE FROM [NortonAbert].[dbo].AdverseParties WHERE ClientNum = ? AND MatterNum = ?"

    CONN.connect()
    data = CONN.readData(q, v)

    for i in data.index:
        matter = [str(data.clientnum[i]), str(data.matternum[i])]
        CONN.writeData(q1, matter)
        CONN.writeData(q2, matter)
        CONN.writeData(q3, matter)

        
def run_database_cleanup(cutoff_date):
    cleanOutDeletedAccounts(cutoff_date)
    cleanout_deleted_matters(cutoff_date)
    