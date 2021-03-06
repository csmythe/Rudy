from UI import *
from ScreenControl.MainScreen import MainMatterScreen
from ScreenControl.LogIn import LogInScreen
from connectors import *
import sys
# import packaging
# import packaging.version
# import packaging.requirements

# @demo
class MainApp(QtWidgets.QApplication):
    def __init__(self, *args):
        QtWidgets.QApplication.__init__(self, *args)
        
        self.main = MainMatterScreen(self)
        self.login = LogInScreen(self)
        self.login.show()
        
        self.lastWindowClosed.connect(self.closeApp)
    
    def closeApp(self):
        self.exit(0)

def main(args):
    global app
    app = MainApp(args)
    app.exec_()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

    
if __name__ == "__main__":
    sys.excepthook = except_hook
    main(sys.argv)