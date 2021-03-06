from UI import *
from functools import partial


class Label(QtWidgets.QLabel):

    @classmethod
    def create_label(cls,text,width = 90):
        inst = cls(width)
        inst.setText(text)
        return inst

    def __init__(self,width):
        super().__init__()
        self.resize(width, 25)

    def paintEvent(self,event):
        painter = QtGui.QPainter(self)

        metrics = QtGui.QFontMetrics(self.font())
        elided = metrics.elidedText(self.text(), QtCore.Qt.ElideRight, self.width())

        painter.drawText(self.rect(), self.alignment(), elided)

    def setText(self, text):
        metrics = QtGui.QFontMetrics(self.font())
        elided_text = metrics.elidedText(text, QtCore.Qt.ElideRight, self.width())
        super().setText(elided_text)


class Alert(QtWidgets.QMessageBox):

    @classmethod
    def create(cls,title,text):
        inst = cls()
        inst.setWindowTitle(title)
        inst.setText(text)
        inst.exec_()


def checkChangesMade(cls):
    if cls.changes == True:
        reply = QtWidgets.QMessageBox.question(cls, "Save Changes?", "Would you like to save your changes?"
                                           ,QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No| QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Yes:
            cls.saveChanges()
            cls.changes = False
            return 0
        elif reply == QtWidgets.QMessageBox.Cancel:
            return 1
        else:
            cls.changes = False
            return 0
    else:   
        cls.changes = False
        return 0
    
def initializeChangeTracking(cls,widget):
    if isinstance(widget,QtWidgets.QLineEdit):
        widget.textEdited.connect(partial(markAsChanged,cls))
    elif isinstance(widget, QtWidgets.QCheckBox):
        widget.clicked.connect(partial(markAsChanged,cls))
    elif isinstance(widget, QtWidgets.QComboBox):
        widget.activated.connect(partial(markAsChanged,cls))
    elif isinstance(widget, QtWidgets.QTextEdit):
        widget.undoAvailable.connect(partial(markAsChanged,cls))
    elif isinstance(widget, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
        widget.valueChanged.connect(partial(markAsChanged, cls))
        

def markAsChanged(cls):
    cls.changes = True

    
def populateTableRow(table, r, cols):
    for c, col in enumerate(cols):
        if isinstance(col, QtWidgets.QTableWidgetItem):
            table.setItem(r,c,col)
        else:
            table.setCellWidget(r,c,col)


def stateGenerator():
    states = """Alabama,AL
Alaska,AK
Arizona,AZ
Arkansas,AR
California,CA
Colorado,CO
Connecticut,CT
Delaware,DE
Washington D.C.,DC
Florida,FL
Georgia,GA
Hawaii,HI
Idaho,ID
Illinois,IL
Indiana,IN
Iowa,IA
Kansas,KS
Kentucky,KY
Louisiana,LA
Maine,ME
Maryland,MD
Massachusetts,MA
Michigan,MI
Minnesota,MN
Mississippi,MS
Missouri,MO
Montana,MT
Nebraska,NE
Nevada,NV
New Hampshire,NH
New Jersey,NJ
New Mexico,NM
New York,NY
North Carolina,NC
North Dakota,ND
Ohio,OH
Oklahoma,OK
Oregon,OR
Pennsylvania,PA
Rhode Island,RI
South Carolina,SC
South Dakota,SD
Tennessee,TN
Texas,TX
Utah,UT
Vermont,VT
Virginia,VA
Washington,WA
West Virginia,WV
Wisconsin,WI
Wyoming,WY""".split("\n")
    for state in states:
        yield state.split(",")