from UI import *
from Functions import MatterFunctions as MtrFuncs,CONN, ClientFunctions as ClntFuncs
from ScreenControl import *

from datetime import datetime as dt
from subprocess import Popen
from re import sub
# from os import getcwd
from PyQt4.Qt import QMessageBox

class ClientMatter(QtGui.QMainWindow):
    def __init__(self, client, clientnum, matter = None):
        
        QtGui.QMainWindow.__init__(self)
        self.ui = loadUi("MatterWindow",self)
        
        for c, w in enumerate([50,150,100,50]):
            self.ui.documentList.setColumnWidth(c,w)

        self.ui.actionSave.setIcon(QtGui.QIcon(saveIcon))
        self.ui.actionEdit.setIcon(QtGui.QIcon(editIcon))
        self.ui.actionClose.setIcon(QtGui.QIcon(exitIcon))
        self.ui.attachDocument.setIcon(QtGui.QIcon(addIcon))
        self.ui.apNew.setIcon(QtGui.QIcon(addIcon))
        self.ui.apClear.setIcon(QtGui.QIcon(clearIcon))
        self.ui.apSave.setIcon(QtGui.QIcon(saveIcon))
        self.ui.apDelete.setIcon(QtGui.QIcon(deleteIcon))
        
        self.client = client
        self.clientnum = clientnum
        self.matter = matter
            
        self.changes = False
        self.action = None
        
        self.ui.dateOpened.setDate(QtCore.QDate(dt.today().date()))
        self.ui.dateClosed.setSpecialValueText('Not Closed')
        self.ui.dateClosed.setDate(self.ui.dateClosed.minimumDate())
        
        self.ui.partyList.cellClicked.connect(self.viewAdverseParty)
        
        self.listMatterTypes()
        self.loadStates()
        self.lockWindow()

        if self.matter is None:
            self.newMatter(self.clientnum )
        else:
            self.loadMatter()
            
        for i in dir(self.ui):
            execStr = """
widget = self.ui.{}
if isinstance(widget,(QtGui.QLineEdit, QtGui.QComboBox, QtGui.QCheckBox, QtGui.QDateEdit)):
    if (widget not in list([self.ui.apFirst,self.ui.apLast, self.ui.apMiddle, self.ui.reason,self.ui.setDirectory])): 
        initializeChangeTracking(self,widget)""".format(i)
            exec(execStr)
        
        self.ui.actionClose.triggered.connect(self.closeWindow)
        self.ui.actionEdit.triggered.connect(self.editMatter)
        self.ui.actionSave.triggered.connect(self.saveChanges)
        
        self.ui.useClientAddress.clicked.connect(self.populateClientAddress)
        self.ui.matterNum.textChanged.connect(self.formatMatterNumber)
        
        self.ui.apClear.clicked.connect(self.clearPartyFields)
        self.ui.apSave.clicked.connect(self.saveAdverseParty)
        self.ui.apDelete.clicked.connect(self.removeAdverseParty)
        self.ui.apNew.clicked.connect(self.addAdverseParty)
        self.ui.closed.stateChanged.connect(self.closeMatter)
        
        self.ui.attachDocument.clicked.connect(self.attachDocumentToMatter)
        self.ui.setDirectory.clicked.connect(self.setMatterDirectory)
        
    def formatMatterNumber(self):
        currNum = self.ui.matterNum.text()
        pattern = "[^0-9]"
        newNum = sub(pattern,"",currNum)
        if newNum == "":
            newNum = 0
        else:
            newNum = int(newNum)
        self.ui.matterNum.setText( "00"[:-len(str(newNum))]+str(newNum) )
        
            
    def lockWindow(self ):
        for i in dir(self.ui):
            exec("""self.setLocks(self.ui.{},True)""".format( i ))
    
    def unlockWindow(self ):
        for i in dir(self.ui):
            exec("""self.setLocks(self.ui.{},False)
    """.format( i ))
        
    def setLocks(self,widget,locked):
        
        if isinstance(widget,QtGui.QLineEdit):
            widget.setReadOnly(locked)
        elif isinstance(widget,(QtGui.QComboBox,QtGui.QDateEdit,QtGui.QToolButton, QtGui.QPushButton, QtGui.QCheckBox)):
            widget.setDisabled(locked)
            
    def newMatter(self , clientNum):
        nextMatter = MtrFuncs.nextMatterNum(clientNum)
        self.ui.clientNum.setText(clientNum)
        self.ui.matterNum.setText(nextMatter)
        self.action = 'new'
        self.unlockWindow()
        
        self.ui.clientNum.setReadOnly(False)
        self.ui.attachDocument.setEnabled(False)
        self.ui.apSave.setEnabled(False)
        self.ui.apDelete.setEnabled(False)
        self.ui.apClear.setEnabled(False)
        self.ui.apNew.setEnabled(False)
        
        
        self.ui.apNew.setEnabled(False)
        self.ui.apFirst.setEnabled(False)
        self.ui.apMiddle.setEnabled(False)
        self.ui.apLast.setEnabled(False)
        self.ui.reason.setEnabled(False)
        
    def loadMatter(self):
        self.lockWindow()
        self.ui.clientNum.setText(str(self.matter.clientnum))
        self.ui.matterNum.setText(str(self.matter.matternum))
        
        self.ui.attorneyInitials.setText(self.matter.attorneyinitials)
        matterindex = self.ui.matterType.findData(int(self.matter.mattertypeid))
        if matterindex > 0:
            self.ui.matterType.setCurrentIndex(matterindex)
            
        self.ui.dateOpened.setDate(QtCore.QDate(dt.strptime(str(self.matter.dateopened),"%Y-%m-%d")))
        if self.matter.dateclosed is not None:
            self.ui.closed.setCheckState(2)
            self.ui.dateClosed.setDate(QtCore.QDate(dt.strptime(str(self.matter.dateclosed),"%Y-%m-%d")))
            self.ui.boxNumber.setText(self.matter.boxnumber)
        else:
            self.ui.closed.setCheckState(0)
            self.ui.dateClosed.setDate(self.ui.dateClosed.minimumDate())
            
        self.ui.firstName.setText(self.matter.firstname)
        self.ui.lastName.setText(self.matter.lastname)
        self.ui.middleInitial.setText(self.matter.middleinitial)
        self.ui.addr1.setText(self.matter.billingaddr1)
        self.ui.addr2.setText(self.matter.billingaddr2)
        self.ui.billCity.setText(self.matter.billingcity)
       
        if self.matter.matterdir is not None:
            self.ui.currentDir.setText(self.matter.matterdir)
            
            
        
        stateindex = self.ui.billState.findData(self.matter.billingstate)
        if stateindex > 0:
            self.ui.billState.setCurrentIndex(stateindex)
        
        self.ui.billZip.setText(self.matter.billingzip)
        
        if self.matter.matterdir is not None:
            self.ui.currentDir.setText(self.matter.matterdir)
        
        self.ui.setDirectory.setEnabled(True)
        self.ui.attachDocument.setEnabled(True)
        self.ui.apSave.setEnabled(False)
        self.ui.apDelete.setEnabled(False)
        self.ui.apClear.setEnabled(True)
        self.ui.apNew.setEnabled(True)
        
        self.listDocuments()
        self.listAdverseParties()
        
    def closeMatter(self,state):
        if state ==2:
            if self.matter.dateclosed is None:
                closeDate = dt.today().date()
            else:
                closeDate = dt.strptime(str(self.matter.dateclosed),"%Y-%m-%d")
        else:
            if self.matter.dateclosed is None:
                closeDate = self.ui.dateClosed.minimumDate().toPyDate()
            else:
                reply = QtGui.QMessageBox.question(self, 'Open Matter','This matter has been closed.  Do you want to re-open the matter?',
                                                   QtGui.QMessageBox.Yes, QtGui.QMessageBox.No
                                                )
                if reply == QtGui.QMessageBox.Yes:
                    closeDate = self.ui.dateClosed.minimumDate().toPyDate()
                else:
                    self.ui.closed.setCheckState(2)
                    closeDate = dt.strptime(str(self.matter.dateclosed),"%Y-%m-%d")
        self.ui.dateClosed.setDate(QtCore.QDate(closeDate))
        
    def listDocuments(self):
        docList = MtrFuncs.generateDocumentList(self.ui.clientNum.text(), self.ui.matterNum.text())
        
        self.ui.documentList.setRowCount(0)
        for r, data in docList:
            self.ui.documentList.insertRow(r)
            
            delButton = QtGui.QToolButton()
            delButton.setIcon(QtGui.QIcon(deleteIcon))
            delButton.clicked.connect( partial(self.deleteAttachment, data.efiledir) )
            delButton.setToolTip('Delete Attachment')
            
            viewButton = QtGui.QToolButton()
            viewButton.setText('View')
            viewButton.clicked.connect( partial(self.viewAttachment, data.efiledir) )
            
            cols = [delButton
                    , QtGui.QLabel(str(data.docname))
                    , QtGui.QLabel(str(data.efiledir))
                    , viewButton]
            
            populateTableRow(self.ui.documentList, r, cols)
            
    def setMatterDirectory(self):
        dirpath = QtGui.QFileDialog.getExistingDirectory(parent=self, caption='Set Matter Directory', directory='C:\\')
        
        if dirpath != '':
            self.ui.currentDir.setText(dirpath)
            
            data = {'action':'update',
                    'table':'ClientMatters',
                    'values':{
                              'MatterDir':str(self.ui.currentDir.text())
                              },
                    'params':{}
                    }
            
            data['params']['ClientNum'] = self.ui.clientNum.text()
            data['params']['MatterNum'] = self.ui.matterNum.text()
            
            CONN.connect()
            CONN.saveData(data)
            CONN.closecnxn()
    
    def attachDocumentToMatter(self):
        currentDir = self.ui.currentDir.text()
        if currentDir == '':
            currentDir = 'C:\\'
        fullPathNameList = QtGui.QFileDialog.getOpenFileNames(self,'Attach Document(s)',currentDir ) 
        
        CONN.connect()
        for fullPathName in fullPathNameList:
                
            filename = fullPathName.split("/")[-1]
            if filename != '':
                data = {'action':'new',
                        'table':'OriginalDocuments',
                        'values':{'ClientNum':self.ui.clientNum.text(),
                                  'MatterNum':self.ui.matterNum.text(),
                                  'DocName':str(filename),
                                  'EFileDir':str(fullPathName)},
                        'params':{}
                        }
        
            CONN.saveData(data)
            
        CONN.closecnxn()
        
        self.listDocuments()
        
    def deleteAttachment(self, path):
        reply = QtGui.QMessageBox.question(self, 'Delete Attachment?', 'Would you like to delete this attachment (will not delete from hard drive)?',
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            data = {'action':'delete',
                    'table':'OriginalDocuments',
                    'values':{
                              },
                    'params':{'ClientNum':self.ui.clientNum.text(),
                              'MatterNum':self.ui.matterNum.text(),
                              'EFileDir':str(path)}
                    }
        
            CONN.connect()
            CONN.saveData(data)
            CONN.closecnxn()
            self.listDocuments()
        
    def viewAttachment(self, path):
        Popen([path],shell = True)
        
    def listAdverseParties(self):
        self.clearPartyFields()
        self.ui.partyList.setRowCount(0)
        
        for r, party in MtrFuncs.generateAdverPartyList(self.ui.clientNum.text(), self.ui.matterNum.text()):
            self.ui.partyList.insertRow(r)
            self.ui.partyList.setRowHeight(r,20)
            firstnamelabel = QtGui.QLabel(party.firstname)
            firstnamelabel.partyid = party.partyid
            cols = [firstnamelabel,
                    QtGui.QLabel(party.middlename),
                    QtGui.QLabel(party.lastname),
                    QtGui.QLabel(party.reasondescription)]
            
            populateTableRow(self.ui.partyList, r, cols)
    
    def addAdverseParty(self):
        self.ui.apFirst.action = 'new'
        
        self.ui.apFirst.setReadOnly(False)
        self.ui.apMiddle.setReadOnly(False)
        self.ui.apLast.setReadOnly(False)
        self.ui.reason.setReadOnly(False)
        
        self.ui.apDelete.setEnabled(False)
        self.ui.apSave.setEnabled(True)
    
    def viewAdverseParty(self,row,col):
        firstnamelabel = self.ui.partyList.cellWidget(row,0)
        partyid = firstnamelabel.partyid
        self.ui.apFirst.setText(firstnamelabel.text())
        self.ui.apFirst.action = 'update'
        self.ui.apFirst.partyid = partyid
        
        self.ui.apMiddle.setText(self.ui.partyList.cellWidget(row,1).text())
        self.ui.apLast.setText(self.ui.partyList.cellWidget(row,2).text())
        self.ui.reason.setText(self.ui.partyList.cellWidget(row,3).text())
        
        self.ui.apFirst.setReadOnly(False)
        self.ui.apMiddle.setReadOnly(False)
        self.ui.apLast.setReadOnly(False)
        self.ui.reason.setReadOnly(False)
        
        self.ui.apDelete.setEnabled(True)
        self.ui.apSave.setEnabled(True)
        self.ui.apNew.setEnabled(False)
    
    def removeAdverseParty(self):
        if self.ui.apFirst.partyid is not None:
            self.ui.apFirst.action = 'delete'
            self.saveAdverseParty()
        
    def saveAdverseParty(self):
        firstname = self.ui.apFirst.text()
        lastname = self.ui.apLast.text()
        middleinitial = self.ui.apMiddle.text()
        reasonGiven = self.ui.reason.text()
        
        action = self.ui.apFirst.action
        
        if action is not None:
            partyid = self.ui.apFirst.partyid
            data = {'action':action,
                    'table':'AdverseParties',
                    'values':{'FirstName':firstname,
                              'LastName':lastname,
                              'MiddleName':middleinitial,
                              'ReasonDescription':reasonGiven},
                    'params':{}
                    }
        
            if action == 'new':
                key = 'values'
            else:
                key = 'params'
                data[key]['PartyID'] = partyid
            data[key]['ClientNum'] = self.ui.clientNum.text()
            data[key]['MatterNum'] = self.ui.matterNum.text()
            
            CONN.connect()
            CONN.saveData(data)
            CONN.closecnxn()
            
            self.listAdverseParties()
    
    def clearPartyFields(self):
        self.ui.apFirst.clear()
        self.ui.apFirst.action = None
        self.ui.apFirst.partyid = None
        self.ui.apLast.clear()
        self.ui.apMiddle.clear()
        self.ui.reason.clear()
        
        self.ui.apFirst.setReadOnly(True)
        self.ui.apMiddle.setReadOnly(True)
        self.ui.apLast.setReadOnly(True)
        self.ui.reason.setReadOnly(True)
        
        self.ui.apSave.setEnabled(False)
        self.ui.apDelete.setEnabled(False)
        self.ui.apNew.setEnabled(True)
        self.ui.apClear.setEnabled(True)
            
    def editMatter(self ):
        reply = checkChangesMade(self)
        if reply == 0:
            if self.action is None:
                self.unlockWindow()
                self.action = 'update'
                self.ui.clientNum.setReadOnly(True)
                self.ui.matterNum.setReadOnly(True)
                self.ui.actionEdit.setText('Cancel Edit')
                self.clearPartyFields()
                
            elif self.action == 'update':
                self.action = None
                self.lockWindow()
                self.ui.actionEdit.setText('Edit')
                self.loadMatter()
                self.clearPartyFields()
                
    def saveChanges(self):
        
        alert = QtGui.QMessageBox()
        if self.action is not None:
            if self.ui.matterNum == '':
                alert.setText("Missing Matter Number")
                alert.setWindowTitle('Need Matter Number')
                alert.exec_()
                return
            if self.ui.matterType.currentIndex() == 0:
                alert.setText("Missing Matter Type")
                alert.setWindowTitle("Need Matter Type")
                alert.exec_()
                return
            if self.ui.dateClosed.date().toPyDate() > self.ui.dateClosed.minimumDate().toPyDate() and self.ui.boxNumber.text() == '':
                alert.setText("Closed matters require a box number.")
                alert.setWindowTitle('Box Number Needed')
                alert.exec_()
                return
            if self.action == 'new':
                if MtrFuncs.checkValidMatterNumber(self.ui.clientNum.text(),self.ui.matterNum.text()):
                    alert.setText("Duplicate Matter Number")
                    alert.setWindowTitle('Matter Number already exists. ')
                    alert.exec_()
                    return
            
            mattertype = self.ui.matterType.itemData(self.ui.matterType.currentIndex())
            
            data = {'action':self.action,
                    'table':'ClientMatters',
                    'values':{'FirstName':self.ui.firstName.text(),
                              'LastName':self.ui.lastName.text(),
                              'MiddleInitial':self.ui.middleInitial.text(),
                              'BillingAddr1':self.ui.addr1.text(),
                              'BillingAddr2':self.ui.addr2.text(),
                              'BillingCity':self.ui.billCity.text(),
                              'BillingState':self.ui.billState.currentText(),
                              'BillingZip':self.ui.billZip.text(),
                              'DateOpened':str(self.ui.dateOpened.date().toPyDate()),
                              'AttorneyInitials':self.ui.attorneyInitials.text(),
                              'EstateAssets':str(self.ui.assets.value()),
                              'MatterDir':str(self.ui.currentDir.text()),
                              'MatterTypeID':str(mattertype)
                              },
                    'params':{}
                    }
            
            if self.ui.dateClosed.date().toPyDate() > self.ui.dateClosed.minimumDate().toPyDate():
                data['values']['DateClosed'] = str(self.ui.dateClosed.date().toPyDate())
                data['values']['BoxNumber'] = self.ui.boxNumber.text()
                
            if self.action == 'new':
                key = 'values'
            else:
                key = 'params'
            data[key]['ClientNum'] = self.ui.clientNum.text()
            data[key]['MatterNum'] = self.ui.matterNum.text()
            
            CONN.connect()
            CONN.saveData(data)
            CONN.closecnxn()
            
            self.changes = False
            self.action = None
            self.lockWindow()
            alert.setText("Save Complete")
            alert.setWindowTitle("Save")
            alert.exec_()
            
            self.ui.attachDocument.setEnabled(True)
            self.ui.apSave.setEnabled(True)
            self.ui.apNew.setEnabled(True)
            self.ui.apClear.setEnabled(True)
            self.ui.setDirectory.setEnabled(True)
            
            self.ui.actionEdit.setText('Edit')
            
            self.client.listMatters(self.clientnum)
        
    def populateClientAddress(self):
        clientInfo = ClntFuncs.getClientInfo(self.clientnum)
        
        self.ui.firstName.setText(clientInfo.firstname[0])
        self.ui.lastName.setText(clientInfo.lastname[0])
        self.ui.middleInitial.setText(clientInfo.middleinitial[0])
        self.ui.addr1.setText(clientInfo.address1[0])
        self.ui.addr2.setText(clientInfo.address2[0])
        self.ui.billCity.setText(clientInfo.city[0])
        self.ui.billZip.setText(clientInfo.zipcode[0])

        ind = self.ui.billState.findData(clientInfo.state[0])
        if ind > 0:
            self.ui.billState.setCurrentIndex(ind)
        
    def listMatterTypes(self):
        matterTypes = MtrFuncs.listMatters()
        
        self.ui.matterType.addItem("")
        for i, m in enumerate(matterTypes.index):
            self.ui.matterType.addItem(matterTypes.matterdescr[m])
            self.ui.matterType.setItemData(i+1, int(matterTypes.typeid[m]))
            
    def loadStates(self ):
        
        self.ui.billState.addItem("")
        i = 1
        for name, abbrv in stateGenerator():
            self.ui.billState.addItem(abbrv)
            self.ui.billState.setItemData(i,abbrv)
            i += 1
    
    def closeWindow(self):
        self.close()
    
    def closeEvent(self, *args, **kwargs):
        reply = checkChangesMade(self)
        if reply == 0:
            return QtGui.QMainWindow.closeEvent(self, *args, **kwargs)
            