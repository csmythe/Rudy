from ScreenControl import *
from UI import *
from Functions import ReportFuncs as rFunc
import xlwt, datetime as dt
from subprocess import Popen
import os
from getpass import getuser

class ReportingControls(QtWidgets.QFrame):
    
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.ui = loadUi('ReportWindow', self)
        
        self.ui.runReport.setIcon(QtGui.QIcon(searchIcon))
        self.ui.exportReport.setIcon(QtGui.QIcon(excelIcon))
        self.ui.clearReport.setIcon(QtGui.QIcon(clearIcon))
        self.ui.resetReport.setIcon(QtGui.QIcon(restartIcon))
        
        self.columns = []
        self.selections = []
        self.reporting = False
        self.data = None
        self.fillTreeWidgets()
        
        self.ui.runReport.clicked.connect(self.runReport)
        self.ui.exportReport.clicked.connect(self.exportReport)
        self.ui.clearReport.clicked.connect(self.clearDisplay)
        self.ui.resetReport.clicked.connect(self.resetParameters)
        
    def resetParameters(self):
        self.columns = []
        self.selections = []
        self.ui.activeFilters.setRowCount(0)
        self.fillTreeWidgets()
        self.clearDisplay()
        
    def clearDisplay(self):
        self.ui.reportResults.clear()
        self.buildReportHeaders()
        self.ui.reportResults.setRowCount(0)
        self.data = None
        self.reporting = False
        
    def fillTreeWidgets(self):
        
        self.ui.displayCols.clear()
        self.ui.availableFilters.clear()
        tableData = rFunc.compileTables()
        
        for data in tableData:
            table, columns, alias = data[0], data[1], data[2]
            displayTopItem = QtWidgets.QTreeWidgetItem()
            displayTopItem.setText(0,table)
            
            self.ui.displayCols.addTopLevelItem(displayTopItem)
            
            filterTopItem = QtWidgets.QTreeWidgetItem()
            filterTopItem.setText(0,table)
            
            self.ui.availableFilters.addTopLevelItem(filterTopItem)
            
            for col in columns:
                
                dispItem = QtWidgets.QTreeWidgetItem(displayTopItem)
                dispSelection = QtWidgets.QCheckBox(col)
                displayTopItem.addChild(dispItem)
                self.ui.displayCols.setItemWidget(dispItem, 0, dispSelection)
                dispSelection.clicked.connect(partial(self.alterColumnHeaders, col, alias, dispItem))
                
                addFilter = QtWidgets.QToolButton()
                addFilter.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
                addFilter.setIcon(QtGui.QIcon(addIcon))
                addFilter.setText(col)
                filtItem = QtWidgets.QTreeWidgetItem(filterTopItem)
                filterTopItem.addChild(filtItem)
                self.ui.availableFilters.setItemWidget(filtItem,0,addFilter)
                addFilter.clicked.connect(partial(self.addFilter, col, alias))
        
    def alterColumnHeaders(self, colName, alias, item):
        state = self.ui.displayCols.itemWidget(item, 0).checkState()
        selection = '{}.{}'.format(alias,colName)
        
        if self.reporting:
            reply = QtWidgets.QMessageBox.question(self, 'Currently Reporting', 'Altering the report columns will clear the report.  Do you want to continue?',
                                               QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.Yes)
            if reply == QtWidgets.QMessageBox.No:
                self.ui.displayCols.itemWidget(item, 0).setCheckState(2)
                return
            else:
                self.clearDisplay()
                
        if state == 2:
            self.columns.append(colName)
            self.selections.append(selection)
        else:
            self.columns.remove(colName)
            self.selections.remove(selection)
        
        self.buildReportHeaders()
        
    def buildReportHeaders(self):
        self.ui.reportResults.setColumnCount(len(self.columns))
        
        for c, col in enumerate(self.columns):
            self.ui.reportResults.setHorizontalHeaderItem(c, QtWidgets.QTableWidgetItem(col))
            
        
    def addFilter(self,colName,alias):
        
        row = self.ui.activeFilters.rowCount()
        
        removeMe = Deleter(self, row)
        
        label = QtWidgets.QLabel(colName)
        label.selection = '{}.{}'.format(alias,colName)
        
        test = ReportTest()
        
        value = QtWidgets.QLineEdit()
        
        cols = [removeMe, label, test, value]
        
        self.ui.activeFilters.insertRow(row)
        for c, col in enumerate(cols):
            self.ui.activeFilters.setCellWidget(row,c,col)

    def removeFilter(self,row):
        self.ui.activeFilters.removeRow(row)
        for newRow in range(self.ui.activeFilters.rowCount()):
            self.ui.activeFilters.cellWidget(newRow,0).updateRow(newRow)
        
    def runReport(self):
        
        if len(self.selections) > 0:
            
            filterList = []
            values = []
            for r in range(self.ui.activeFilters.rowCount()):
                
                label = self.ui.activeFilters.cellWidget(r,1)
                test = self.ui.activeFilters.cellWidget(r,2)
                testSymbol = test.itemData(test.currentIndex())
                value = self.ui.activeFilters.cellWidget(r,3)
                
                filterList.append("{} {} ?".format(label.selection, testSymbol))
                values.append(value.text())
            filters = ' AND '.join(filterList)
            
            if len(filters) > 0:
                filters = "WHERE "+filters
                
            self.data = rFunc.runSearch(self.selections, filters, values)
            
            if len(self.data) == 0:
                alert = QtWidgets.QMessageBox()
                alert.setText('No Results Found')
                alert.setWindowTitle("Empty Search")
                alert.exec_()
                return
            self.reporting = True
            self.ui.reportResults.setRowCount(0)
            self.ui.reportResults.setRowCount(len(self.data))
            
            for r, i in enumerate(self.data.index):
                row = self.data.loc[i]
                for c, col in enumerate(self.columns):
                    itemWidget = QtWidgets.QLabel(str(row[col]))
                    self.ui.reportResults.setCellWidget(r,c,itemWidget)
                    
                
    def exportReport(self):
        if self.data is not None:
            exportDT = str(dt.datetime.today().date())
            if not os.path.isdir('C:\\Users\\{}\\Documents\\RudyExports'.format(getuser())):
                os.makedirs('C:\\Users\\{}\\Documents\\RudyExports'.format(getuser()))
            filename = 'C:\\Users\\{}\\Documents\\RudyExports\\'.format(getuser()) + 'ReportExport_{}.xls'.format(exportDT)
            book = xlwt.Workbook()
            sheet1 = book.add_sheet('Data_Export')
            
            row = sheet1.row(0)
            row.write(0, 'Data Exported: {}'.format(exportDT))
            
            headerRow = sheet1.row(3)
            for c, col in enumerate(self.columns):
                headerRow.write(c,col)
            
            tableStart = 4
            for r, i in enumerate(self.data.index):
                dataSet = self.data.loc[i]
                row = sheet1.row(tableStart + r)
                for c, col in enumerate(self.columns):
                    row.write(c,str(dataSet[col]))
        
            book.save(filename)
            
            Popen([filename], shell=True)
            
class ReportFilter(QtWidgets.QFrame):
    
    def __init__(self, parent, columnName, item, alias):
        QtWidgets.QFrame.__init__(self)
        self.layout = QtWidgets.QHBoxLayout(self)
        
        self.parent = parent
        self.item = item
        
        self.removeMe = QtWidgets.QToolButton()
        self.removeMe.setIcon(QtGui.QIcon(deleteIcon))
        
        self.label = QtWidgets.QLabel(columnName)
        self.label.selection = '{}.{}'.format(alias,columnName)
        self.compareBox = QtWidgets.QComboBox()
        compares = ['=','<>','>','>=','<','<=', 'LIKE','NOT LIKE']
        for i in compares:
            self.compareBox.addItem(i)
            
        self.value = QtWidgets.QLineEdit()
        
        self.layout.addWidget(self.removeMe)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.compareBox)
        self.layout.addWidget(self.value)
        
        self.removeMe.clicked.connect(self.removeFilter)
        
    def removeFilter(self):
        row = self.parent.ui.activeFilters.row(self.item)
        taken = self.parent.ui.activeFilters.takeItem(row)
        del(taken)
        
class Deleter(QtWidgets.QToolButton):
    def __init__(self,parent,row):
        QtWidgets.QToolButton.__init__(self)
        self.row = row
        self.parent = parent
        
        self.setIcon(QtGui.QIcon(deleteIcon))
        
        self.clicked.connect(self.removeFilter)
        
    def updateRow(self,newRow):
        self.row = newRow
        
    def removeFilter(self):
        self.parent.removeFilter(self.row)
        
        
class ReportTest(QtWidgets.QComboBox):
    
    def __init__(self):
        QtWidgets.QComboBox.__init__(self)
        
        compares = [['Equal To','='],
                    ['Not Equal To','<>'],
                    ['Greater Than', '>'],
                    ['Grtr. Than or Equal', '>='],
                    ['Less Than', '<'],
                    ['Less Than or Equal', '<='],
                    ['Text Contains','LIKE'],
                    ['Text Does Not Contain','NOT LIKE']]
        for n, ij in enumerate(compares):
            i, j = ij[0],ij[1]
            self.addItem(i)
            self.setItemData(n, j)
        