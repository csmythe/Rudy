from UI import *
from connectors.dbConnect import Connection

class LogInScreen(QtGui.QFrame):
    def __init__(self,app):
        
        QtGui.QFrame.__init__(self)
        self.ui = loadUi("LogIn",self)
        
        self.actionLogIn = QtGui.QAction('AttemptLogin',self)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter),self,self.attemptLogIn)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return),self,self.attemptLogIn)
        
        self.app = app
        self.ui.login.clicked.connect(self.attemptLogIn)
        self.ui.cancel.clicked.connect(self.cancelLogIn)
        
    def attemptLogIn(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        Conn = Connection()
        Conn.connect()
        data = Conn.readData("SELECT * FROM [UserParam] WHERE UserName = ? AND Password = ?", [username, password])
        if len(data) > 0:
            self.app.main.activeUser = data.loc[0]
            self.app.main.show()
            self.app.main.showMaximized()
            self.close()
        else:
            alert = QtGui.QMessageBox()
            alert.setText("Wrong Username or Password.")
            alert.setWindowTitle("Login Failed")
            alert.exec_()
            return
        
    def cancelLogIn(self):
        self.close()
        self.app.closeApp()