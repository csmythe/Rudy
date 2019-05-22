from Functions import *

        
def listClients(firstNames, lastNames, addrFilter, cityFilter, stateFilter, contactFilters, deleted):
    v = []
    
    qSearchs = []
    if firstNames != '':
        qSearchs.append( " (ci.firstname LIKE ? OR ci.spousefirstname LIKE ? OR cm.firstname LIKE ? )")
        v.extend(['%'+firstNames+'%','%'+firstNames+'%','%'+firstNames+'%', ])
        
    if lastNames != '':
        qSearchs.append( " ( ci.lastname LIKE ? OR ci.spouselastname LIKE ?  OR cm.lastname LIKE ?)" )
        v.extend(['%'+lastNames+'%','%'+lastNames+'%','%'+lastNames+'%'])
        
    if addrFilter != '':
        qSearchs.append("(ci.Address1 LIKE ? OR ci.Address2 LIKE ? OR cm.BillingAddr1 LIKE ? OR cm.BillingAddr2 LIKE ? )")
        v.extend(['%'+addrFilter+'%','%'+addrFilter+'%','%'+addrFilter+'%','%'+addrFilter+'%'])
    
    if cityFilter != '':
        qSearchs.append(" (ci.City LIKE ? OR cm.BillingCity LIKE ?)")
        v.append("%"+cityFilter+"%")
        v.append("%"+cityFilter+"%")
        
    if stateFilter != '':
        qSearchs.append("(ci.State LIKE ? OR cm.BillingState LIKE ? )")
        v.append("%"+stateFilter+"%")
        v.append("%"+stateFilter+"%")
    
    if contactFilters != '':
        qSearchs.append(" (ci.Phone1 LIKE ? OR ci.Phone2 LIKE ? OR ci.Email LIKE ?) ")
        v.extend(['%'+contactFilters+'%','%'+contactFilters+'%','%'+contactFilters+'%'])
        
    if deleted:
        qSearchs.append(" (ci.Deleted = 1) ")
    else:
        qSearchs.append(" (ci.Deleted <> 1 OR ci.Deleted IS NULL) ")
    
    if len(qSearchs) > 0:
        searches = ' WHERE {} '.format(" AND ".join(qSearchs))
    else:
        searches = ''
    q = """
    SELECT ci.*
    FROM [NortonAbert].[dbo].[ClientInfo] ci
    INNER JOIN (
    SELECT DISTINCT ci.ClientNum
    FROM [NortonAbert].[dbo].[ClientInfo] ci 
        LEFT JOIN [NortonAbert].[dbo].[ClientMatters] cm on ci.ClientNum = cm.ClientNum
    {}
    ) cl on ci.ClientNum = cl.ClientNum
    ORDER BY ci.clientnum asc
    """.format(searches)

    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    return data
    # for r, i in enumerate(data.index):
    #     yield r, data.loc[i]
        
def getNextClientNum():
    q = "SELECT ISNULL(MAX(ClientNum),0) +1  as nextnum FROM [NortonAbert].[dbo].ClientInfo"
    CONN.connect()
    data = CONN.readData(q,[])
    CONN.closecnxn()
    return data
        
def getClientInfo(clientNum):
    q = "SELECT * FROM [NortonAbert].[dbo].ClientInfo WHERE ClientNum = ?"
    v = [str(clientNum)]
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    return data

def compileDupeCheck(clientnum):
    q = """
    SELECT ClientNum
        , FirstName, MiddleInitial, LastName
        , Address1, Address2, City, State, ZipCode
    FROM [NortonAbert].[dbo].ClientInfo
    WHERE ClientNum <> ?
    """
    v= [str(clientnum)]
    CONN.connect()
    data = CONN.readData(q,v)
    CONN.closecnxn()
    
    data['fullname'] = data.firstname + ' ' + data.middleinitial + ' ' + data.lastname
    data['fulladdr'] = data.address1 + ' ' + data.address2 + ' ' + data.city + ' ' + data.state + ' ' + data.zipcode
    
    return data

def compileAdversePartyList():
    q = "SELECT * FROM [NortonAbert].[dbo].AdverseParties"
    v = []
    CONN.connect()
    data = CONN.readData(q,v)
    data['fullname'] = data.firstname + ' ' + data.middlename + ' ' + data.lastname
    CONN.closecnxn()
    return data