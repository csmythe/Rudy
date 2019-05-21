from UI import *
from ScreenControl import *
from Functions import UserFunctions as UsrFuncs, MatterFunctions as MtrFuncs, CONN
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox
import datetime as dt


class MatterManager(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.ui = loadUi("ManageMatters", self)
#         
        self.ui.newMatter.setIcon(QtGui.QIcon(addIcon))
        self.ui.save.setIcon(QtGui.QIcon(saveIcon))
        self.ui.clear.setIcon(QtGui.QIcon(clearIcon))
        
        self.changes = False
        self.action = None
        
        for i in dir(self.ui):
            if i != 'showInactive':
                exec("initializeChangeTracking(self, self.ui.{})".format(i))

        
        self.lockFields()
        self.listMatters()
        
        self.ui.showInactive.clicked.connect(self.listMatters)
        self.ui.matterList.itemClicked.connect(self.loadMatter)
        self.ui.clear.clicked.connect(self.clearFields)
        self.ui.save.clicked.connect(self.saveChanges)
        self.ui.newMatter.clicked.connect(self.addMatter)
            
        
    def listMatters(self):
        matterTypes = MtrFuncs.listMatters(activeOnly = self.ui.showInactive.checkState() == 0)
        
        self.ui.matterList.clear()
        for i in matterTypes.index:
            mType = matterTypes.loc[i]
            matterLabel = QtWidgets.QLabel(mType.matterdescr)
            matterLabel.mType = mType
            item = QListWidgetItem()
            self.ui.matterList.addItem(item)
            self.ui.matterList.setItemWidget(item, matterLabel)
            
    def loadMatter(self, item):
        reply = checkChangesMade(self)
        if reply == 0:
            self.changes = False
            mType = self.ui.matterList.itemWidget(item).mType
            self.unlockFields()
            self.action = 'update'
            self.ui.matterDescr.typeid = mType.typeid
            self.ui.matterDescr.setText(mType.matterdescr)
            self.ui.inactive.setCheckState(int(mType.inactive) * 2)
            
    def clearFields(self):
        reply = checkChangesMade(self)
        if reply == 0:
            self.changes = False
            self.ui.matterDescr.typeid = None
            self.ui.matterDescr.clear()
            self.ui.inactive.setCheckState(0)
            self.lockFields()
            
    def addMatter(self):
        reply = checkChangesMade(self)
        if reply == 0:
            self.clearFields()
            self.unlockFields()
            self.action = 'new'
            
        
    def lockFields(self):
        self.ui.matterDescr.setReadOnly(True)
        self.ui.inactive.setEnabled(False)
    
    def unlockFields(self):
        self.ui.matterDescr.setReadOnly(False)
        self.ui.inactive.setEnabled(True)
        
        
    def saveChanges(self):
        if self.action is not None:
            if self.ui.matterDescr.text().strip() == '':
                alert = QtWidgets.QMessageBox()
                alert.setWindowTitle("Missing Description")
                alert.setText("Matter needs a description before saving.")
                alert.exec_()
                return
            else:
                data = {'action':self.action,
                        'table':'MatterTypes',
                        'values':{'MatterDescr':str(self.ui.matterDescr.text()),
                                  'Inactive':str(int(self.ui.inactive.checkState()/ 2 ) )
                                  },
                        'params':{}
                        }
                if self.action == 'update':
                    data['params']['TypeID'] = str(self.ui.matterDescr.typeid)
                
                CONN.connect()
                CONN.saveData(data)
                CONN.closecnxn()
                self.changes = False
                self.clearFields()
                self.listMatters()
                
        
class Password(QtWidgets.QFrame):
    def __init__(self,usermgr,action):
        
        QtWidgets.QFrame.__init__(self)
        self.usermgr = usermgr
        self.action = action
        
        self.setWindowTitle("Password")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        
        self.layout = QtWidgets.QFormLayout(self)
        
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.confirm = QtWidgets.QLineEdit()
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.hbox = QtWidgets.QHBoxLayout()
        self.btnSavePassword = QtWidgets.QPushButton('Save')
        self.btnCancelPassword = QtWidgets.QPushButton('Cancel')
        
        self.hbox.addWidget(self.btnSavePassword)
        self.hbox.addWidget(self.btnCancelPassword)
        
        self.layout.addRow(QtWidgets.QLabel("Password: "),self.password)
        self.layout.addRow(QtWidgets.QLabel("Confirm: "),self.confirm)
        self.layout.addRow(None,self.hbox)
        
        self.btnCancelPassword.clicked.connect(self.close)
        self.btnSavePassword.clicked.connect(self.savePassword)
    
    def savePassword(self):
        if self.password.text() != self.confirm.text():
            alert = QtWidgets.QMessageBox()
            alert.setWindowTitle("Password Mismatch")
            alert.setText("Your password does not match the confirmation. Please try again.")
            alert.exec_()
            return
        else:
            self.usermgr.ui.password.pwd = self.password.text()
            self.usermgr.changes = True
            self.close()

class UserManager(QtWidgets.QFrame):
    def __init__(self):
        
        QtWidgets.QFrame.__init__(self)
        self.ui = loadUi("ManageUsers", self)
#         
        self.ui.newUser.setIcon(QtGui.QIcon(addIcon))
        self.ui.save.setIcon(QtGui.QIcon(saveIcon))
        self.ui.clear.setIcon(QtGui.QIcon(clearIcon))

        for i in dir(self.ui):
            if i != 'showInactive':
                exec("initializeChangeTracking(self,self.ui.{})".format(i))

        self.changes = False
        self.lockFields()
        self.listUsers()
        
        self.ui.newUser.clicked.connect(self.startNewUser)
        self.ui.save.clicked.connect(self.saveChanges)
        self.ui.clear.clicked.connect(self.clearFields)
        self.ui.password.clicked.connect(self.setPassword)
        self.ui.userList.itemClicked.connect(self.loadUserDetails)
        self.ui.showInactive.clicked.connect(self.listUsers)
    
    def lockFields(self,):
            
        self.ui.username.setReadOnly(True)
        self.ui.password.setEnabled(False)
        self.ui.fullName.setReadOnly(True)
        self.ui.admin.setEnabled(False)
        self.ui.inactive.setEnabled(False)
            
    def unlockFields(self):
            
        self.ui.username.setReadOnly(False)
        self.ui.password.setEnabled(True)
        self.ui.fullName.setReadOnly(False)
        self.ui.admin.setEnabled(True)
        self.ui.inactive.setEnabled(True)
    
    def listUsers(self):
        userListData = UsrFuncs.getUserList(activeOnly = self.ui.showInactive.checkState() == 0)
        
        self.ui.userList.clear()
        for i in userListData.index:
            item = QListWidgetItem()
            itemLabel = QtWidgets.QLabel(userListData.username[i])
            itemLabel.data = userListData.loc[i]
        
            self.ui.userList.addItem(item)
            self.ui.userList.setItemWidget(item, itemLabel)
            
    def setPassword(self):
        self.pwdWindow = Password(self,self.action)
        self.pwdWindow.show()
    
            
    
    def startNewUser(self):
        self.clearFields()
        self.unlockFields()
        
        self.action = 'new'
    
    def clearFields(self):
        reply = checkChangesMade(self)
        if reply == 0:
            self.lockFields()
            self.ui.username.clear()
            self.ui.password.pwd = None
            self.ui.fullName.clear()
            self.ui.lastSignin.clear()
            self.ui.admin.setCheckState(0)
            self.ui.admin.orig = 0
            self.ui.inactive.setCheckState(0)
            
            self.changes = False
    
    def saveChanges(self):
        
        username = self.ui.username.text()
        password = self.ui.password.pwd
        fullName = self.ui.fullName.text()
        admin = self.ui.admin.checkState() == 2
        inactive = self.ui.inactive.checkState() == 2
        
        checks = UsrFuncs.validateUserChange(username)
        
        alert = QtWidgets.QMessageBox()
        if checks.usrchk[0] > 0 and self.action == 'new':
            alert.setWindowTitle('Invalid Username')
            alert.setText('Username Already Used')
            alert.exec_()
            return
        elif not admin and checks.admchk[0] == 1 and self.ui.admin.orig == 2:
            alert.setWindowTitle('Last Admin')
            alert.setText("This is the last administrator account.")
            alert.exec_()
            return 
        elif inactive and checks.inactivechk[0] == 1 and self.ui.inactive.origInactive == 0:
            alert.setWindowTitle('Last Active Account')
            alert.setText("This is the last active account.")
            alert.exec_()
            return
        elif password is None:
            alert.setWindowTitle('No Password')
            alert.setText("Set your password before saving.")
            alert.exec_()
            return

        data = {'action':self.action,
                'table':'UserParam',
                'values':{'Password':password,
                          'FullName':fullName,
                          'Admin':int(admin),
                          'Inactive':int(inactive)},
                'params':{}
                }
        
        if self.action == 'new':
            key = 'values'
        else:
            key = 'params'
            
        data[key]['Username'] = username
        
        CONN.connect()
        CONN.saveData(data)
        CONN.closecnxn()
        self.changes = False
        self.clearFields()
        self.listUsers()
        
    def loadUserDetails(self,item):
        reply = checkChangesMade(self)
        if reply == 0:
            
            self.clearFields()
            self.unlockFields()
            self.ui.username.setReadOnly(True)
            self.action = 'update'
            
            userData = self.ui.userList.itemWidget(item).data    
            self.ui.username.setText(userData.username)
            self.ui.password.pwd = userData.password
            self.ui.fullName.setText(userData.fullname)
            self.ui.admin.setCheckState(int(userData.admin) * 2)
            self.ui.inactive.setCheckState(int(userData.inactive) * 2)
            
            self.ui.inactive.origInactive = int(userData.inactive) * 2
            self.ui.admin.origAdmin = int(userData.admin) * 2
            

class CleanUp(QtWidgets.QFrame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.ui = loadUi("FileMaintenance", self)
        
        self.ui.delDate.setDate(QtCore.QDate(dt.datetime.today().date() - dt.timedelta(days = 180)))
        
        self.ui.run.clicked.connect(self.startDeleting)
        
    def startDeleting(self):
        reply = QtWidgets.QMessageBox.warning(self, "Caution: Deleting Permanently", "You are about to PERMANENTLY remove accounts and matters and ALL the related saved data.  Are you sure you want to continue?",
                                          QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            delDate = self.ui.delDate.date().toPyDate()
            UsrFuncs.run_database_cleanup(delDate)
            alert = QMessageBox()
            alert.setWindowTitle("Complete")
            alert.setText("Clean up completed")
            alert.exec_()
            return
        
    