# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportFrame(object):
    def setupUi(self, ReportFrame):
        ReportFrame.setObjectName("ReportFrame")
        ReportFrame.setWindowModality(QtCore.Qt.ApplicationModal)
        ReportFrame.resize(845, 503)
        ReportFrame.setStyleSheet("\n"
"QFrame#ReportFrame{\n"
"    \n"
"    font: 10pt \"Microsoft Tai Le\";\n"
"    background-color:rgb(226, 226, 226);\n"
"}\n"
"QGroupBox, QToolBox{\n"
"    font: 75 12pt \"Microsoft Tai Le\";\n"
"}\n"
"QPushButton{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QToolButton{\n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"}\n"
"QToolButton#prevPage{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QToolButton#nextPage{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}")
        ReportFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ReportFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(ReportFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(ReportFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resetReport = QtWidgets.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/restart.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetReport.setIcon(icon)
        self.resetReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.resetReport.setObjectName("resetReport")
        self.horizontalLayout.addWidget(self.resetReport)
        self.runReport = QtWidgets.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runReport.setIcon(icon1)
        self.runReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.runReport.setObjectName("runReport")
        self.horizontalLayout.addWidget(self.runReport)
        self.exportReport = QtWidgets.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/excelExport.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportReport.setIcon(icon2)
        self.exportReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.exportReport.setObjectName("exportReport")
        self.horizontalLayout.addWidget(self.exportReport)
        self.clearReport = QtWidgets.QToolButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/clear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearReport.setIcon(icon3)
        self.clearReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clearReport.setObjectName("clearReport")
        self.horizontalLayout.addWidget(self.clearReport)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.toolBox = QtWidgets.QToolBox(self.layoutWidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 535, 397))
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.displayCols = QtWidgets.QTreeWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayCols.sizePolicy().hasHeightForWidth())
        self.displayCols.setSizePolicy(sizePolicy)
        self.displayCols.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.displayCols.setAlternatingRowColors(True)
        self.displayCols.setRootIsDecorated(True)
        self.displayCols.setUniformRowHeights(False)
        self.displayCols.setAnimated(False)
        self.displayCols.setAllColumnsShowFocus(False)
        self.displayCols.setObjectName("displayCols")
        item_0 = QtWidgets.QTreeWidgetItem(self.displayCols)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.displayCols)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.displayCols)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.displayCols)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 535, 397))
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.availableFilters = QtWidgets.QTreeWidget(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableFilters.sizePolicy().hasHeightForWidth())
        self.availableFilters.setSizePolicy(sizePolicy)
        self.availableFilters.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.availableFilters.setAlternatingRowColors(True)
        self.availableFilters.setRootIsDecorated(True)
        self.availableFilters.setUniformRowHeights(False)
        self.availableFilters.setAnimated(False)
        self.availableFilters.setAllColumnsShowFocus(False)
        self.availableFilters.setColumnCount(1)
        self.availableFilters.setObjectName("availableFilters")
        item_0 = QtWidgets.QTreeWidgetItem(self.availableFilters)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.availableFilters)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.availableFilters)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.availableFilters.header().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.availableFilters, 1, 0, 1, 1)
        self.activeFilters = QtWidgets.QTableWidget(self.page_2)
        self.activeFilters.setObjectName("activeFilters")
        self.activeFilters.setColumnCount(4)
        self.activeFilters.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.activeFilters, 1, 1, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.reportResults = QtWidgets.QTableWidget(self.splitter)
        self.reportResults.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reportResults.setAlternatingRowColors(True)
        self.reportResults.setObjectName("reportResults")
        self.reportResults.setColumnCount(0)
        self.reportResults.setRowCount(0)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(ReportFrame)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ReportFrame)

    def retranslateUi(self, ReportFrame):
        _translate = QtCore.QCoreApplication.translate
        ReportFrame.setWindowTitle(_translate("ReportFrame", "Rudy Reporting"))
        self.resetReport.setText(_translate("ReportFrame", "Reset Parameters"))
        self.runReport.setText(_translate("ReportFrame", "Run Report"))
        self.exportReport.setText(_translate("ReportFrame", "Export Report"))
        self.clearReport.setText(_translate("ReportFrame", "Clear Report"))
        self.displayCols.headerItem().setText(0, _translate("ReportFrame", "Table"))
        __sortingEnabled = self.displayCols.isSortingEnabled()
        self.displayCols.setSortingEnabled(False)
        self.displayCols.topLevelItem(0).setText(0, _translate("ReportFrame", "ClientInfo"))
        self.displayCols.topLevelItem(0).child(0).setText(0, _translate("ReportFrame", "ClientNum"))
        self.displayCols.topLevelItem(0).child(1).setText(0, _translate("ReportFrame", "ClientName"))
        self.displayCols.topLevelItem(1).setText(0, _translate("ReportFrame", "ClientMatters"))
        self.displayCols.topLevelItem(1).child(0).setText(0, _translate("ReportFrame", "MatterNum"))
        self.displayCols.topLevelItem(1).child(1).setText(0, _translate("ReportFrame", "MatterTypeID"))
        self.displayCols.topLevelItem(1).child(2).setText(0, _translate("ReportFrame", "Attorney"))
        self.displayCols.topLevelItem(1).child(3).setText(0, _translate("ReportFrame", "TotalAssets"))
        self.displayCols.topLevelItem(2).setText(0, _translate("ReportFrame", "MatterTypes"))
        self.displayCols.topLevelItem(2).child(0).setText(0, _translate("ReportFrame", "MatterTypeID"))
        self.displayCols.topLevelItem(2).child(1).setText(0, _translate("ReportFrame", "MatterDesc"))
        self.displayCols.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("ReportFrame", "Display Columns"))
        self.label.setText(_translate("ReportFrame", "Choose Filter"))
        self.label_2.setText(_translate("ReportFrame", "Active Filters"))
        self.availableFilters.headerItem().setText(0, _translate("ReportFrame", "Table"))
        __sortingEnabled = self.availableFilters.isSortingEnabled()
        self.availableFilters.setSortingEnabled(False)
        self.availableFilters.topLevelItem(0).setText(0, _translate("ReportFrame", "ClientInfo"))
        self.availableFilters.topLevelItem(0).child(0).setText(0, _translate("ReportFrame", "ClientNum"))
        self.availableFilters.topLevelItem(0).child(1).setText(0, _translate("ReportFrame", "ClientName"))
        self.availableFilters.topLevelItem(1).setText(0, _translate("ReportFrame", "ClientMatters"))
        self.availableFilters.topLevelItem(1).child(0).setText(0, _translate("ReportFrame", "MatterNum"))
        self.availableFilters.topLevelItem(1).child(1).setText(0, _translate("ReportFrame", "MatterTypeID"))
        self.availableFilters.topLevelItem(1).child(2).setText(0, _translate("ReportFrame", "Attorney"))
        self.availableFilters.topLevelItem(1).child(3).setText(0, _translate("ReportFrame", "TotalAssets"))
        self.availableFilters.topLevelItem(2).setText(0, _translate("ReportFrame", "MatterTypes"))
        self.availableFilters.topLevelItem(2).child(0).setText(0, _translate("ReportFrame", "MatterTypeID"))
        self.availableFilters.topLevelItem(2).child(1).setText(0, _translate("ReportFrame", "MatterDesc"))
        self.availableFilters.setSortingEnabled(__sortingEnabled)
        item = self.activeFilters.horizontalHeaderItem(1)
        item.setText(_translate("ReportFrame", "Field"))
        item = self.activeFilters.horizontalHeaderItem(2)
        item.setText(_translate("ReportFrame", "Filter"))
        item = self.activeFilters.horizontalHeaderItem(3)
        item.setText(_translate("ReportFrame", "Value"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("ReportFrame", "Report Filters"))


