
# from UI.Icons_rc import *
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.LogIn import Ui_LogIn
from UI.MainWindow import Ui_MainWindow
from UI.ManageMatters import Ui_ManageMatters
from UI.ManageUsers import Ui_ManageUsers
from UI.MatterWindow import Ui_MatterWindow
from UI.ReportWindow import Ui_ReportFrame
from UI.FileMaintenance import Ui_FileMaint
# import os



UIDir = '.\\UI'
icoDir = UIDir+'\\Icons\\'

saveIcon = icoDir+"save.ico"
clearIcon = icoDir+"clear.ico"
addIcon = icoDir+"plus.ico"
exitIcon = icoDir+"arrow-1.ico"
editIcon = icoDir+"note.ico"
deleteIcon = icoDir+"delete.ico"
alertIcon = icoDir+"exclamation.ico"
searchIcon = icoDir+"search.ico"
printIcon = icoDir+"print.ico"
excelIcon = icoDir+"excelExport.ico"
restartIcon = icoDir+"restart.ico"


def loadUi(key,widget):
    ui_dict = {'LogIn':Ui_LogIn,
            'MainWindow':Ui_MainWindow,
            'ManageMatters':Ui_ManageMatters,
            'ManageUsers':Ui_ManageUsers,
            'MatterWindow':Ui_MatterWindow,
            'FileMaintenance':Ui_FileMaint,
            'ReportWindow':Ui_ReportFrame}
    
    widget.ui = ui_dict[key]()
    widget.ui.setupUi(widget)
    return widget.ui
        